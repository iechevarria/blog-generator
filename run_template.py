#!/usr/bin/python3

import os
import re
import shutil
from datetime import datetime
from email import utils
from xml.sax.saxutils import escape as xml_escape

import frontmatter
from markdown import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape


# Set up Jinja2 environment and templates
ENV = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape("html"),
)
BLOG_TEMPLATE = ENV.get_template("blog.html")
BLOG_LIST_TEMPLATE = ENV.get_template("blog_list.html")
BOOK_TEMPLATE = ENV.get_template("books.html")
BOOK_LIST_TEMPLATE = ENV.get_template("book_list.html")
HOME_TEMPLATE = ENV.get_template("home.html")
RSS_TEMPLATE = ENV.get_template("rss.xml")


def generate_blog(source_dir="blog", dest_dir="../iechevarria.github.io"):
    """Generate HTML blog posts from markdown files.
    
    Args:
        source_dir: Directory containing blog post markdown files
        dest_dir: Output directory for generated HTML
        
    Returns:
        List of dicts containing metadata for each post
    """
    post_metas = []

    # Process each post directory
    _, post_dirs, _ = next(os.walk(source_dir))
    for post_dir in post_dirs:
        post_dest = os.path.join(dest_dir, source_dir, post_dir)
        os.makedirs(post_dest, exist_ok=True)

        # Copy supporting files (images, etc)
        post_files = os.listdir(os.path.join(source_dir, post_dir))
        non_post_files = [f for f in post_files if f != "index.md"]
        image_files = [f for f in post_files if f.lower().endswith(('jpg', 'png', 'jpeg'))]
        
        for file in non_post_files:
            shutil.copyfile(
                os.path.join(source_dir, post_dir, file),
                os.path.join(post_dest, file)
            )

        # Convert markdown to HTML
        post = frontmatter.load(os.path.join(source_dir, post_dir, "index.md"))
        html = markdown(post.content, extensions=["toc"])
        
        # Handle featured image for social media previews
        if "image" in post:
            image = post["image"]
            if image not in image_files:
                raise ValueError(f"Image {image} not found in post directory")
            post["image"] = f"https://www.echevarria.io/{source_dir}/{post_dir}/{image}"

        # Write HTML file
        local_path = os.path.join(source_dir, post_dir, "index.html").replace("\\", "/")
        with open(os.path.join(dest_dir, local_path), "w", encoding="utf-8") as f:
            f.write(BLOG_TEMPLATE.render(
                content=html,
                base_href="../../",
                **post.metadata
            ))

        # Store post metadata
        post_metas.append({
            "title": post["title"],
            "url": local_path,
            "date": post["date"],
            "content": html,
        })

    # Generate blog index page
    post_metas.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
    with open(os.path.join(dest_dir, source_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(BLOG_LIST_TEMPLATE.render(
            posts=post_metas,
            base_href="../",
            title="writing",
            page="blog_list"
        ))

    return post_metas


def generate_reading(source_dir="reading", dest_dir="../iechevarria.github.io"):
    """Generate HTML pages for book reviews.
    
    Args:
        source_dir: Directory containing book review markdown files
        dest_dir: Output directory for generated HTML
        
    Returns:
        List of dicts containing metadata for each book review
    """
    book_metas = []

    # Process each book review
    _, _, books = next(os.walk(source_dir))
    for book in books:
        # Convert markdown to HTML
        post = frontmatter.load(os.path.join(source_dir, book))
        html = markdown(post.content)
        
        # Write HTML file
        out_path = os.path.join(dest_dir, source_dir, f"{book.split('.')[0]}.html")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(BOOK_TEMPLATE.render(
                content=html,
                base_href="../",
                **post.metadata
            ))

        # Store book metadata
        book_metas.append({
            "title": post["title"],
            "author": post["author"],
            "date": post["date"],
            "rating": post["rating"],
            "url": out_path,
        })

    # Generate reading list index page
    book_metas.sort(key=lambda x: x["date"], reverse=True)
    with open(os.path.join(dest_dir, source_dir, "index.html"), "w") as f:
        f.write(BOOK_LIST_TEMPLATE.render(
            posts=book_metas,
            base_href="../",
            title="reading",
            page="book_list"
        ))

    return book_metas


def generate_home(post_metas, book_metas, n=10, dest_dir="../iechevarria.github.io"):
    """Generate home page showing recent posts and book reviews.
    
    Args:
        post_metas: List of blog post metadata
        book_metas: List of book review metadata
        n: Number of recent items to show
        dest_dir: Output directory for generated HTML
    """
    recent_posts = post_metas[:n]
    recent_books = book_metas[:n]

    with open(os.path.join(dest_dir, "index.html"), "w") as f:
        f.write(HOME_TEMPLATE.render(
            posts=recent_posts,
            books=recent_books,
            title="home",
            page="home"
        ))


def generate_rss(post_metas, dest_dir="../iechevarria.github.io"):
    """Generate RSS feed for blog posts.
    
    Args:
        post_metas: List of blog post metadata
        dest_dir: Output directory for generated RSS
    """
    recent_posts = post_metas[:10]
    
    for post in recent_posts:
        # Format date for RSS
        d = post["date"]
        post["pub_date"] = utils.format_datetime(datetime(d.year, d.month, d.day))

        # Convert relative URLs to absolute        
        hrefs = (
            re.findall(r'href=["\'](.+?)["\']', post["content"]) +
            re.findall(r'src=["\'](.+?)["\']', post["content"])
        )
        
        replacements = {
            href: f"https://www.echevarria.io/{href}"
            for href in hrefs
            if not href.startswith("http")
        }
        
        for old, new in replacements.items():
            post["content"] = post["content"].replace(old, new)

        post["content"] = xml_escape(post["content"])

    with open(os.path.join(dest_dir, "rss.xml"), "w") as f:
        f.write(RSS_TEMPLATE.render(posts=recent_posts))


if __name__ == "__main__":
    post_metas = generate_blog()
    book_metas = generate_reading()
    generate_home(post_metas, book_metas)
    generate_rss(post_metas)
