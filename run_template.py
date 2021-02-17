import os
import shutil
from collections import namedtuple

import frontmatter
from markdown import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape


ENV = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape("html"),
)
BLOG_TEMPLATE = ENV.get_template("blog.html")
BLOG_LIST_TEMPLATE = ENV.get_template("blog_list.html")
BOOK_TEMPLATE = ENV.get_template("books.html")
BOOK_LIST_TEMPLATE = ENV.get_template("book_list.html")


def generate_blog(
    source_dir="blog", dest_dir="../iechevarria.github.io"
):
    """Generates posts for blog"""
    
    post_metas = []

    _, post_dirs, _ = next(os.walk(source_dir))
    for post_dir in post_dirs:
        if not os.path.exists(os.path.join(dest_dir, source_dir, post_dir)):
            os.makedirs(os.path.join(dest_dir, source_dir, post_dir))
        # copy non-post directory contents over
        _, _, files = next(os.walk(os.path.join(source_dir, post_dir)))
        non_post_files = [f for f in files if f != "index.md"]
        for f in non_post_files:
            shutil.copyfile(
                os.path.join(source_dir, post_dir, f),
                os.path.join(dest_dir, source_dir, post_dir, f)
            )

        # convert markdown to html
        post = frontmatter.load(os.path.join(source_dir, post_dir, "index.md"))
        html = markdown(post.content)
        local_path = os.path.join(source_dir, post_dir, "index.html")
        with open(os.path.join(dest_dir, local_path), "w+") as f:
            f.write(BLOG_TEMPLATE.render(
                content=html, base_href="../../", **post.metadata)
            )

        # get metadata from post
        post_metas.append(
            {"title": post["title"], "url": local_path, "date": post["date"]}
        )

    # reverse chronological order for blog index page
    post_metas = sorted(
        post_metas, key=lambda x: x["date"], reverse=True
    )
    with open(os.path.join(dest_dir, source_dir, "index.html"), "w+") as f:
        f.write(BLOG_LIST_TEMPLATE.render(
            posts=post_metas, base_href="../", title="writing"
        ))


def generate_reading(
    source_dir="reading", dest_dir="../iechevarria.github.io"
):
    """Generates posts for book reviews"""
    
    book_metas = []

    _, _, books = next(os.walk(source_dir))
    for book in books:
        # convert markdown to html
        post = frontmatter.load(os.path.join(source_dir, book))
        html = markdown(post.content)
        out_path = os.path.join(
            dest_dir, source_dir, f"{book.split('.')[0]}.html"
        )
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w+") as f:
            f.write(BOOK_TEMPLATE.render(
                content=html, base_href="../", **post.metadata
            ))

        # get metadata from book
        book_metas.append(
            {
                "title": post["title"],
                "author": post["author"],
                "date": post["date"],
                "rating": post["rating"],
                "url": out_path,
            }
        )

    # reverse chronological order for blog index page
    book_metas = sorted(
        book_metas, key=lambda x: x["date"], reverse=True
    )
    with open(os.path.join(dest_dir, source_dir, "index.html"), "w+") as f:
        f.write(BOOK_LIST_TEMPLATE.render(
            posts=book_metas, base_href="../", title="reading"
        ))


if __name__ == "__main__":
    generate_blog()
    generate_reading()
