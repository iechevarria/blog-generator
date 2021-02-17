---
title: A sorting visualization
date: 2019-12-16
---

I was recently re-reading [Mike Bostock](https://bost.ocks.org/mike/)'s excellent 2014 post [Visualizing Algorithms](https://bost.ocks.org/mike/algorithms/#sorting) when his [static quicksort visualization](https://bl.ocks.org/mbostock/6dcc9a177065881b1bc4) (based on [Aldo Cortesi](https://corte.si/)'s 2007 [work](https://corte.si/posts/code/visualisingsorting/index.html)) caught my eye. In this visualization, each row represents the state of an array after a swap operation is performed. I thought it would be an interesting exercise to reproduce it, so I wrote a quick proof-of-concept. The following is some example output from my first attempt:

![sorting visualization proof-of-concept](blog/a-sorting-visualization/proof_of_concept.svg)

It's clear that this version doesn't look nearly as nice as Mike Bostock's. The main issue aside from color is that the swap paths in mine lack curvature on their outer corners. I considered reproducing this using lines with round ends, but hubris got the best of me, and I decided I could do even better.

Instead of just having a curve on the outer corner of the swaps paths, I thought I could use arcs to get curves on both the inside and outside of the swap paths. After a bit of experimentation, I found that the shape I wanted to use could be defined by arcs on the surface of two circles connected by an inner tangent line between the two circles. The following is some output for validation from when I was writing code to make the swap paths:

![Quicksort using the Hoare partition scheme](blog/a-sorting-visualization/tangent_test.svg)

I spent some time tuning the curvature of the swap connections by fiddling with the radius of the circles used to define the arcs. I couldn't find a radius that looked right or worked for all the connections - radii that made swaps between distant indices work looked too sharp for the close swaps. Meanwhile, radii that looked great for close swaps completely broke the math for the long swaps. Eventually, I landed on a solution: varying the radii of the circles that defined the arcs based on the distance between the indices of the elements being swapped.

I'm pleased with the final product. The resulting images are less vertically compact than they would be with sharp corners, but I think the tradeoff is worthwhile. Swaps between nearby indices make an especially pleasing braid-like pattern.

The source (Python) is on [GitHub](https://github.com/iechevarria/sorting-visualizations). The code is not my best, but it works. Here's an example of visualization for quicksort:

![Quicksort using the Hoare partition scheme](blog/a-sorting-visualization/quicksort_hoare.svg)
