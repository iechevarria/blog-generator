---
title: This blog is now statically generated
date: 2021-02-17
---

Before today, I hand-wrote all my blog posts in HTML. I’ve always known this isn’t ideal, but until a year ago, I wasn’t writing much. It didn’t seem worthwhile to invest the time and effort in setting up static site generation.

Since I’ve been writing monthly updates, though, the manual work and boilerplate has been wearing on me. In addition, I started to fear changing my site layout at all since that would mean going back through every page I’ve created and changing each of them manually.

For these reasons, I’ve now set this blog up to be generated statically - I now write the content of my blog posts as [Markdown](https://daringfireball.net/projects/markdown/), a text format that's a lot easier to write than HTML, and I use a script to turn them into HTML pages on my site.

### Why not use a framework?

There are [plenty](https://jekyllrb.com/) [of](https://gohugo.io/) [frameworks](https://hexo.io/) for static site generation, but I decided to write a script myself for two main reasons. First, my situation was unique - I already had a blog, and it was plain HTML. I liked the way it looked. All I needed to do was make some templates and then populate them with content. I didn’t need the extra configurability or pre-made themes that these frameworks provide.

Second, I try to spend time and effort learning things that generalize. I’d rather learn something new about programming than learn about the idiosyncrasies of a specific piece of software, in this case a static site generator, that I doubt I’ll use in any other context. (Jonathan Blow mentions the scourge of trivial knowledge about tools in his talk [Preventing the Collapse of Civilization](https://youtu.be/pW-SOdj4Kkk?t=2756) around the 46 minute mark.)

### Results

So I went ahead and wrote a quick, simple Python script that uses [Jinja2](https://jinja.palletsprojects.com/) templates and Markdown files to generate this blog. I spent probably about the same amount of time writing the script as it would have taken me to get a static site generator configured to my liking. The script is crappy, but it’s totally adequate!  Both this [website](https://github.com/iechevarria/iechevarria.github.io) and the [script](https://github.com/iechevarria/blog-generator) are up on GitHub.

This is the first blog post I’ve written in Markdown, and it was a much better experience than hand-writing HTML. I’m glad I made the switch.
