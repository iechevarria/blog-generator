---
title: April 2021
date: 2021-05-02
---

I started my new job at [Ladder](https://www.ladderlife.com/) (obligatory mention that [we’re hiring](https://www.ladderlife.com/careers)) at the beginning of April, and I spent most of the month getting settled at work and unpacking/reorganizing after a recent move. I still found some time to read, though!

#### Reading

I finally finished [Money: 5000 Years of Debt and Power](https://www.versobooks.com/books/2738-money) by Michel Aglietta. It was a slog – I’m not sure if it was the original French or the English translation that made it so grueling. I think it was worthwhile, though. What I enjoyed most was Aglietta’s description of spontaneous centralization in multiple contexts: from clearing houses acting as lenders of last resort before central banks existed, to international industries using a single currency to maintain competitiveness, to individuals accepting a currency on the basis that others will accept it in turn.

Since I’m now working at a life insurance company, I decided to learn a bit about the industry the best way I know how: by reading some sociology. [Morals & Markets](http://cup.columbia.edu/book/morals-and-markets/9780231183352) by Viviana A. Rotman Zelizer is about the emergence of life insurance in the United States, and it pays special attention to how culture shaped and was shaped by this new market. I don’t think I can recommend Morals & Markets until I read [Investing in Life](https://jhupbooks.press.jhu.edu/title/investing-life) by Sharon Ann Murphy which apparently “directly challenges the conclusions of previous scholars who have dismissed the importance of the earliest industry innovators while exaggerating clerical opposition to life insurance” – a not-even-trying-to-be-subtle jab at Zelizer and the sources she relied on.

[Debt is Coming](https://alexdanco.com/2020/02/07/debt-is-coming/) by [Alex Danco](https://alexdanco.com/) is an excellent take on the coming wave of debt in the tech industry. When I was reading Hyman Minsky’s *John Maynard Keynes*, I was astonished at how closely it hewed to my personal experience working at startups, specifically his description of how an investment boom unfolds. Except for one thing: a lot of what Minsky describes pivots around debt, and I don’t see much debt in my vicinity. This article helped me understand why that is, and why that’s going to change in the future.

#### Listening

I’ve been listening to [OTTO](https://www.instagram.com/wnoadiarwb/)’s recent releases with [PLZ Make It Ruins](https://plz.world/
), Vegyn’s label. His stuff is just fantastic, and it has a crazy range, from the muted ambient track Microplastics in My Bloodstream 

<iframe style="border: 0; width: 100%; height: 42px;" class="bandcamp-player" src="https://bandcamp.com/EmbeddedPlayer/album=2350244153/size=small/bgcol=ffffff/linkcol=0687f5/track=72478192/transparent=true/" seamless><a href="https://plzmakeitruins.bandcamp.com/album/clam-day">Clam Day by OTTO</a></iframe>

… to pop-y weirdness in Dairy Adventure 

<iframe style="border: 0; width: 100%; height: 42px;" class="bandcamp-player" src="https://bandcamp.com/EmbeddedPlayer/album=2350244153/size=small/bgcol=ffffff/linkcol=0687f5/track=173418513/transparent=true/" seamless><a href="https://plzmakeitruins.bandcamp.com/album/clam-day">Clam Day by OTTO</a></iframe>

… to the intricate, Aphex Twin-like Bathroom On The Bus

<iframe style="border: 0; width: 100%; height: 42px;" class="bandcamp-player" src="https://bandcamp.com/EmbeddedPlayer/album=965744653/size=small/bgcol=ffffff/linkcol=0687f5/track=3256920498/transparent=true/" seamless><a href="https://plzmakeitruins.bandcamp.com/album/world-greetings">World Greetings by OTTO</a></iframe>

#### Programming

I started another course at [Bradfield](https://bradfieldcs.com/) – this time it’s Operating Systems. Like Computer Architecture, which I took in January, this class is fantastic. I’m only two weeks in, but I already have a far stronger understanding of how Unix-based operating systems work and the historical context behind why they work the way they do. Go 

I’m using Clojure daily at my new job, and I’m starting to develop some opinions about it. On the good side, it’s just pleasant to use, and it lets you pack a lot of meaning into relatively few lines while still making that meaning understandable. Because the vast majority of Clojure functions are pure functions, I’ve found it very easy to jump into files and figure out how data is flowing. If you need some data in a function, you pass it in explicitly – it’s refreshing to have everything as function arguments.

On the bad side, I’ve never felt farther from the hardware. While Clojure is faster than Python, I at least understand what makes Python slow – Python data structure *x* is actually data structure *y* in C, and so you get lots of cache misses or what have you. With Clojure, there’s more to know: Clojure has special, optimized data structures, and it also has a lot of interop with Java, so you should really know Java, and then Clojure runs on the JVM, so you should have a handle on the JVM, which is its own whole thing. Not that any of that knowledge is essential, but if performance is a concern (it is for me), you have a few more layers to wade through to understand what’s happening on the hardware.
