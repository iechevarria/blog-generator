---
title: The Mighty pushback isn't all about Mighty
date: 2021-07-05
---

Two months ago, [Mighty](https://www.mightyapp.com/) launched with its [plan to “reignite the future of desktop computing”](https://blog.mightyapp.com/mightys-secret-plan-to-invent-the-future-of-computing/). This vision of the future got a lot of pushback.

<a href="https://twitter.com/cmuratori/status/1387126330961981441">
    <img
        src="blog/the-mighty-pushback-isnt-all-about-mighty/cmuratori_tweet.png"
        alt="@cmuratori: Running a browser to connect to the cloud to run a browser to connect to the cloud to retrieve the contents of a single 2D page to recompress and send back to the original browser is now &quotthe future of computing&quot."
    />
</a>

There are many, many other critical tweets and comments, but I think this one is fairly representative.

Venture capitalist and Mighty backer [Paul Graham](http://paulgraham.com/index.html) wrote an thinly-veiled response, [Crazy New Ideas](http://paulgraham.com/newideas.html), in which he argues that Mighty’s critics are stuck in a conventional way of thinking. This is true for some of Mighty’s critics, but there are others who are instead raging against the status quo of bad web performance. For them, this fight isn't really about Mighty.

There’s a faction of developers – many of whom make games – who love to talk about how bad modern web performance is. (For what it’s worth, I largely agree with this crowd even though I work on web stuff.) When you look at what they do, it’s easy to see why. Game developers push hardware to its limits: they’re rendering high resolution frames with hundreds of thousands to millions of triangles, with enormous textures, with complex lighting, with all sorts of post-processing – and they’re often doing this for 60+ frames every second.

<img class="img-really-no-pad" src="blog/the-mighty-pushback-isnt-all-about-mighty/screenshot.jpg" alt="screenshot of the witness"/>
<div class="img-note" style="margin-top: 0.5em;">
    screenshot of <a href="http://the-witness.net/">The Witness</a>
</div>

To hit these targets, game developers need to have a strong understanding of computer architecture, and they need to have access to their hardware at a low level. They optimize data layout on disk to make reads faster, and they pack data in memory as densely as possible to minimize cache misses.

When someone works with these standards, and they see a website that’s just text and images but takes a full second to render, they’re understandably incredulous. 1000 ms to do a 2D page layout? What kind of idiot needs 1000 ms to render a 2D image? [How many web developers understand that a low-end integrated GPU on a laptop can draw full 4k screens of pixels at 3000 frames per second?](https://twitter.com/Jonathan_Blow/status/1387520980029829120)

So with all this in mind, let’s take a look at what [Jonathan Blow](https://twitter.com/Jonathan_Blow), creator of [Braid](http://braid-game.com/) and [The Witness](http://the-witness.net/), has to say about Mighty:

<a href="https://twitter.com/Jonathan_Blow/status/1387094702139142145">
    <img
        src="blog/the-mighty-pushback-isnt-all-about-mighty/jonathan_blow_tweet.png"
        alt="@Jonathan_Blow: Very hard to describe how embarrassing this is for everyone involved in the Web and, sort of, software more generally."
    />
</a>

Okay, so in context, this is a clear indictment of web stuff and low software quality in general more than it is condemnation of Mighty. “Look at how terrible the web is,” the games crowd says. “Their ecosystem is so bad that they need to stream 2D pages on powerful computers to make them usable.”

And I’m far from the only one who saw this! Web developers understood that they were the target. Here’s [Tom MacWright](https://macwright.com) addressing the games crowd the day Mighty discourse hit its peak:

<a href="https://twitter.com/tmcw/status/1387105535376314373">
    <img
        src="blog/the-mighty-pushback-isnt-all-about-mighty/tmcw_tweet.png"
        alt="@tmcw: game developers dunking on web performance is, ahem, not great. 1. if everyone browsed the web on PS5 hardware, it'd be pretty good. game consoles are powerful and fairly homogenous! 2. the web solves for instant distribution + security for untrusted code. no other platform does"
    />
</a>

Tom is half right here – the web makes distribution easy. But PC is not a homogenous target. It might be more homogenous than the sum of all web targets, but it can’t be called homogenous in any absolute way – PC game developers work hard to target a huge range of hardware. I played Jonathan Blow’s The Witness on a laptop-grade machine and found that it ran at 60 frames per second (though at low resolution).

This cuts to the heart of the issue: it *is* possible to make software that runs well on heterogenous hardware. Mighty's existence, on the other hand, shows that web software is slow. In the eyes of the games crowd, so accustomed to stringent performance targets, this amounts to total failure.

<br>

*In the future, I'm going to write about the pushback against Mighty that really is about Mighty as a product and about why Mighty could really work.*
