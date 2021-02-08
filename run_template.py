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


def generate_blog(input_dir="blog_md", output_dir="blog"):
    """Generates posts for blog"""
    
    post_metadatas = []

    _, post_dirs, _ = next(os.walk(input_dir))
    for post_dir in post_dirs:
        # copy non-post directory contents over
        _, _, files = next(os.walk(os.path.join(input_dir, post_dir)))
        relevant_files = [f for f in files if f != "index.md"]
        for f in relevant_files:
            shutil.copyfile(
                os.path.join(input_dir, post_dir, f),
                os.path.join(output_dir, post_dir, f)
            )

        # convert markdown to html
        post = frontmatter.load(os.path.join(input_dir, post_dir, "index.md"))
        html = markdown(post.content)
        out_path = os.path.join(output_dir, post_dir, "index.html")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w+") as f:
            f.write(BLOG_TEMPLATE.render(content=html, **post.metadata))                

        # get metadata from post
        post_metadatas.append(
            {"title": post["title"], "url": out_path, "date": post["date"]}
        )

    # reverse chronological order for blog index page
    post_metadatas = sorted(
        post_metadatas, key=lambda x: x["date"], reverse=True
    )
    with open(os.path.join(output_dir, "index.html"), "w+") as f:
        f.write(
            BLOG_LIST_TEMPLATE.render(posts=post_metadatas, title="writing")
        )


if __name__ == "__main__":
    generate_blog()
