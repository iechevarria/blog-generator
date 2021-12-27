---
title: Consistent daily price oscillations on the Steam Community Market
date: 2021-12-26
---

<a href="blog/cs-go-price-oscillation/steam.png">
  <img class="img-really-no-pad" src="blog/cs-go-price-oscillation/steam.png" alt="chart of CS:GO Operation Riptide Case median sales prices on Steam Community Market"/>
</a>
<div class="img-note">click the image above to see a full-size version</div>

This is a chart of median sale prices of the most-sold item on the [Steam Community Market](https://steamcommunity.com/market/), an [Operation Riptide Case](https://steamcommunity.com/market/listings/730/Operation%20Riptide%20Case) for Counter-Strike: Global Offensive (CS:GO).

The extremely regular oscillations in price jumped out to me immediately. You don't typically see this in other markets because it's a sign that money is being left on the table.

My first instinct was that this pattern was somehow related to CS:GO player count, so I pulled historical price and volume data from Steam and historical player counts from [steamcharts.com](https://steamcharts.com/) to made this chart:

<a href="blog/cs-go-price-oscillation/chart.svg">
  <img class="img-really-no-pad" src="blog/cs-go-price-oscillation/chart.svg" alt="chart of CS:GO Operation Riptide Case median sales prices on Steam Community Market, player count, and transaction count"/>
</a>
<div class="img-note">click the image above to see a full-size version</div>
<div class="img-caption">
  <li>
    <b>Top</b>: median sale price in dollars
  </li>
  <li>
    <b>Middle</b>: CS:GO player count
  </li>
  <li>
    <b>Bottom</b>: count of Operation Riptide Cases sold
  </li>
</div>

It does look like it has something to do with player count. So what's happening? These cases are randomly given to players when they play the game, and some players immediately sell their cases for cash at market price. (If sellers cared about making a few extra cents, they could submit offers to sell above the current market price instead of selling at market price when prices are low.)

I suspect the oscillations are caused by different regions buying/selling/keeping cases at different rates. To illustrate, it might be the case that players in Europe sell more cases and buy fewer cases than players in the Americas, so the market price for cases is lower during European hours than American hours.

I don't see the same pattern in other CS:GO items. Only the Operation Riptide Case exhibits it, and that makes sense because it's the only item that is currently being distributed to players for simply playing the game.

But why aren't there other market participants who flatten these oscillations out? Someone could buy cases cheap during European hours and sell for a profit during American hours.

The culprit here is fees on Steam Community Market transactions. CS:GO items on the Community Market are subject to a 15% fee on every transaction: 5% for Steam plus 10% for CS:GO specifically. This means that you can only make money on price swings greater than 15%.

If you look at the actual price daily swings, they're typically smaller than 15%.

<img class="img-really-no-pad" src="blog/cs-go-price-oscillation/percents.svg" alt="Percentage difference between minimum hourly median and maximum hourly median sale price by day"/>
<div class="img-note">
    Percentage difference between minimum hourly median and maximum hourly median sale price by day
</div>

On some days, the percentage approaches 15%. I suspect that on these days, there _are_ some market participants buying cheap, holding for a few hours, selling high, and making a cent or two per case after fees.

Note that the min and max values used in the chart are median hourly sale price, so some transactions happened at higher/lower values. Therefore individual cases may have been bought and then sold profitably after fees.
