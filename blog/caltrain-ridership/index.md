---
title: Caltrain ridership
date: 2023-02-20
---

Caltrain's ridership numbers are a pain to get a hold of, so I made [caltrainridership.com](https://caltrainridership.com).

If you go to Caltrain's official [ridership page](https://web.archive.org/web/20220629064038/https://www.caltrain.com/about-caltrain/statistics-reports/ridership), you get links to three different sources, only one of which, the Caltrain Board of Directors monthly meeting agendas, is up-to-date. Each agenda PDF has at most a year of ridership numbers, but some only have the actual average weekday ridership number for that specific month. The format has changed several times, so it's not even doable to programmatically extract ridership numbers. It shouldn't be this hard.

So I read through old meeting agendas and found individual months' average weekday ridership back to July 2017. I dropped these numbers in a CSV which you can go get for yourself in the [project GitHub repo](https://github.com/iechevarria/caltrain-ridership). And I picked up the [caltrainridership.com](https://caltrainridership.com) domain and made a little site with graphs and a table.

It took effort to collect these numbers in the real world – distributing them should be the easy part. If Caltrain won't, I will.
