---
title: An interesting way to pack bytes into a MIDI SysEx message
date: 2021-12-21
---

Here’s a little thought experiment: how would you transmit 8-bit bytes via messages that let you encode only 7 bits at a time?

The engineers at [DigiTech](https://www.digitech.com/) handled this exact problem on their DHP-55 effects unit in the 1990s. They needed to transmit 8-bit bytes to the unit via a MIDI SysEx message. Every byte in a SysEx message must have its most significant bit set to 0, so there are only 7 bits available per byte for sending data.

This is how they describe their approach in the DHP-55 manual:

![todo2](blog/midi-sysex/scan1.png)


(For clarity, I'm going to call the 8-bit bytes we want to transmit the "real" bytes and the bytes with 7 bits available that we have to use the "send" bytes.)

The engineers chose to do the following: pack 7 "real" bytes into 8 "send" bytes at a time. Take the most significant bit of each of the "real" bytes and put them into the first "send" byte. Then take the remaining 7 bits of each of the "real" bytes and put them in each of the remaining "send" bytes.

I've illustrated an example of this packing below:

![todo](blog/midi-sysex/midi-bits.svg)
<div class="img-caption">
  <li>
    <b>Left</b>: The 7 (8-bit) "real" bytes we want to transmit
  </li>
  <li>
    <b>Right</b>: The 8 "send" bytes. The first byte contains 0 and the most significant bit of each of the 7 "real" bytes. The following 7 "send" bytes contain 0 and the 7 remaining bits of each of the 7 "real" bytes.
  </li>
</div>

I find this a pretty interesting solution to the problem. It's not my first instinct – I would have just mashed the bytes together instead of sending the most significant bits separately.

So why the engineers at DigiTech separate the most significant bits? One reason might be that it makes hex dumps a lot easier to read.

If you take a look at the manual, you can see that much of the data that's being transmitted is small integers (less than 128) where the most significant bit is already 0. This means that many of the "send" bytes will have identical values to those in the "real" bytes.

Bank number, preset number, number of effects, effect number, number of parameters, effect version – all of these will likely be less than 128.

![todo3](blog/midi-sysex/scan2.png)


If the DigiTech engineers had gone with my approach, "send" bytes would not resemble "real" bytes, and they wouldn't be able to use hex dumps for spot checks.

_If you know another reason, please reach out!_
