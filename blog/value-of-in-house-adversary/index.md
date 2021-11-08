---
title: The value of an in-house adversary
date: 2021-11-06
---

_This is written with the assumption that you know what a market maker is and what an order book is. For a solid primer, check out the [first three sections of this opinion piece](https://a16z.com/2021/02/17/payment-for-order-flow/)._

_If I should make any corrections to this post, please reach out._

#### Market making versus liquidity taking

High frequency trading (HFT) firms run strategies that broadly fall into two categories: making and taking. Market making strategies add bids and asks to trading venues’ order books, making it possible for other market participants to quickly convert a security into cash and vice-versa. Conversely, liquidity-taking strategies execute on existing bids or asks, removing them from order books.

When you make markets, one of your biggest risks is failing to cancel stale quotes. If the price of the security moves, your offers to sell could now be too low, or your quotes to buy could now be too high. Then when someone executes against those stale quotes, you lose money, and they make some. This is called being “picked off.” When you’re running a taking strategy, you’re actively looking for quotes that you can pick off: too-high bids and too-low asks are what you want to execute against.

This is why speed matters so much in HFT: if you’re a market maker and you don’t cancel your stale quotes fast enough, a liquidity taker will execute on them and eat your lunch.

#### Building the adversary in-house

Other than raw speed, how else can makers avoid getting picked off by takers? One interesting answer is that HFT firms doing market making should also have an in-house team running a taking strategy.

The taking team hunts for stale quotes from any market participant. When they find a quote they can pick off for a profit, and it comes from outside the firm, they execute against the order and make some money. If the quote comes from inside the firm, they tell the market making team to cancel it so it won’t be picked off by a competitor [[1]](blog/value-of-in-house-adversary/index.html#note). 

[Donald MacKenzie](https://www.sps.ed.ac.uk/staff/donald-mackenzie) describes the (unintended) results of such an approach in his book [Trading at the Speed of Light](https://press.princeton.edu/books/hardcover/9780691211381/trading-at-the-speed-of-light) (p 195):

<p class="quote">
“Attempts to take ... had the unintended, emergent consequence of increasing the profitability of the firm's market making algorithms. The latter would be to a degree protected from taking algorithms in the wider market by the fact that one of the firm's own taking algorithms might well cause the cancellation of a making order before it could be picked off"
</p>

The taking team protected the whole firm’s profitability not by directly looking for flaws in the making team’s strategy – it was a black box to them – but simply by trying to pick off any market participant. Having a taking mindset and taking incentives helped the team find and plug holes in the firm’s making strategy that the making team didn’t know about.

The HFT maker/taker relationship is inherently adversarial, and having both sides within the same firm partially insulates it from outside competitors.

<br>
<br>

[1]<i id="note">
This is a slightly inaccurate simplification – I didn’t want to muddy the explanation. The taking team doesn’t directly tell the making team to cancel their order because the taking team doesn't actually know which orders belong to them. The taking team just sees an order they want to execute against and a separate system within the firm decides whether to execute against it (another firm’s order) or cancel it (the firm's order).
</i>
