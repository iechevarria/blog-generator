---
title: "Bradfield School of Computer Science is phenomenal"
date: 2022-02-06
---

_Nobody asked me to write this, and I don't benefit materially from you joining._

Choosing to take courses at [Bradfield School of Computer Science](https://bradfieldcs.com/) is probably the best decision I've made for my career and my craft. If you're a software engineer, you should consider applying.

This is a loose collection of thoughts about my time in the [Computer Science Intensive (CSI)](https://bradfieldcs.com/csi/) and at Bradfield generally. I wrote this to make a slightly more personal case for taking courses at Bradfield and to fill in some gaps in existing information. If you're totally unfamiliar with Bradfield, go read the [official site](https://bradfieldcs.com/) first.

Contents:

- [My background and why I started taking Bradfield courses](blog/bradfield-is-phenomenal/index.html#my-background-and-why-i-started-taking-bradfield-courses)
- [Who takes Bradfield courses?](blog/bradfield-is-phenomenal/index.html#who-takes-bradfield-courses)
- [Quality of instruction](blog/bradfield-is-phenomenal/index.html#quality-of-instruction)
- [Workload](blog/bradfield-is-phenomenal/index.html#workload)
- [Value in interviews](blog/bradfield-is-phenomenal/index.html#value-in-interviews)
- [Value on the job](blog/bradfield-is-phenomenal/index.html#value-on-the-job)
- [Community](blog/bradfield-is-phenomenal/index.html#community)
- [Money](blog/bradfield-is-phenomenal/index.html#money)
- [Accreditation](blog/bradfield-is-phenomenal/index.html#accreditation)
- [Other students' reviews of Bradfield](blog/bradfield-is-phenomenal/index.html#other-students-reviews-of-bradfield)
- [Closing thoughts](blog/bradfield-is-phenomenal/index.html#closing-thoughts)

## My background and why I started taking Bradfield courses

I studied computer science and math at [William & Mary](https://www.wm.edu/), a public university in Virginia. I did well in school – I graduated _summa cum laude_, was inducted into Phi Beta Kappa, and got a computer science department award.

But I graduated with a lot of gaps in my computer science knowledge. I couldn't tell you how a computer physically operated, or how a database worked, or what an operating system's responsibilities were, or anything at all about computer networks. Some of this was because I was unlucky with course selection. The bigger reason is that I didn't absorb as much because I was learning to program at the same time I was learning computer science. These are different skills. Fighting to get a grip on language syntax and conventions occupied most of my attention.

After a few years of work, I was a much better programmer, but I started feeling the gaps in my computer science knowledge more acutely. I wondered why my code was slow and didn't have a good answer. I found out about Bradfield, and I signed up for a standalone course. It was more than I hoped it would be. I’ve now taken three standalone courses, and as of writing, I'm three modules into the CSI (about 1/3 of the way through). 

## Who takes Bradfield courses?

Students at Bradfield come from a broad range of backgrounds. Most are people who did coding bootcamps and have been working for at least a few years. Others studied computer science at university – some of my classmates at Bradfield have undergraduate degrees from the best computer science departments in the world. All of my classmates have gotten enormous value from Bradfield, I think in approximately equal measure.

## Quality of instruction

Oz and Elliott, the instructors at Bradfield, are phenomenal teachers. Their knowledge of the subject matter is encyclopedic, but they also take teaching seriously as its own skill. Oz seems to read a lot of pedagogical theory (though he says not *too much* [[1]](blog/bradfield-is-phenomenal/index.html#note)), and Elliott continuously hones his courses. 

The most important thing that Oz and Elliott teach is a mindset: that everything on a computer is knowable with a bit of effort. Need to figure out what's going on with a network? Open [Wireshark](https://www.wireshark.org/) and capture some packets. Not sure what a certain system call is doing? Check the [man page](https://en.wikipedia.org/wiki/Man_page). Don't know how to use a protocol? Read the [RFC](https://www.rfc-editor.org/). Want to figure out how this language feature works? Go to the source code. When a student asks something and the instructor says "huh, I don't know," they find out and in the process show the rest of us how to answer our own questions.

A small list of other things I like about instruction at Bradfield:

- A strong emphasis on learning by doing. Most class pre-work involves a hands-on exercise.
- Historical motivation as a teaching method. The instructors will take us back to a historical context and ask us how we'd solve a problem to help us understand how the world ended up as it is.
- Tangents/rants. Get ready to hear about how programmers ought to be more like woodworkers and make more of their own tools, why the space / time complexity tradeoff is kind of a lie, and why microservices are not a great fit for most organizations.

## Workload

The CSI workload is heavy, there's no getting around that. You have two to three hour classes twice a week plus optional hour-long check-ins. Every class has pre-work. Expect to spend ten hours a week on CSI at minimum.

Should you join CSI, you should expect to fall behind at some point. Don't let it psych you out. Keep showing up to class. Oz and Elliott won't get mad at you.

If you're thorough, you can easily spend as much time on Bradfield as you do at a full-time job. It's absolutely not necessary, though – I only say this because some people in my cohort did this for a few months.

## Value in interviews

Taking Bradfield courses makes you a stronger candidate when interviewing for jobs. Some of my classmates have interviewed for jobs at level _X_ and done so well that they received offers at level _X_ + 1. I got offers that previously would have been unattainable.

An example: I interviewed at an autonomous vehicle company last year. One of my interviewers was clearly perplexed when our session started and said outright that someone must have made a mistake. I had professionally only worked with Python, and his interview was about high-performance systems. "What's a Python programmer doing here," he said.

I said that while my experience was only Python and that I liked Python, I did care about performance and I understood why Python was slow. He said, fine, explain. So I used what I learned in Bradfield: I talked about how cache utilization in Python is bad for a few reasons (pointer-heavy data structures, everything is an object so takes more space, etc.). I was able to rattle off latency numbers to argue why this was so harmful.

My interviewer’s demeanor changed completely. “It’s unusual for a Python programmer to think about caches at all.” He tested my knowledge a bit more, but the rest of the interview felt more like a friendly conversation than an interrogation. I had a great time, and I ended up with a good offer.

I don’t think I would have passed this interview if not for my time at Bradfield. I was able to speak comfortably and confidently because I put the work in at Bradfield. I did the reading, and more importantly, the exercises, and that gave me a strong intuition for this stuff.

None of this is to say that you can just sign up for Bradfield and never have to study Leetcode-style problems again, but it makes you a lot stronger for everything else.

## Value on the job

Bradfield's biggest benefit for me on the job has been simply having confidence that everything on a computer is knowable with a bit of effort. I can't give a dramatic example like I can with interviewing because real work isn't like interviewing, but I can tell you I'm faster and more capable, and that I have stronger engineering instincts.

There are some benefits more immediately related to class material. Just last week, I debugged some microservices by reading network activity directly. One of my classmates sped up a critical process by at least a factor of 2 (maybe a lot more?) by applying knowledge straight from a course. Another upgraded his whole company from HTTP/1.1 to HTTP/2.

## Community

Bradfield is the community of programmers I've been searching for. Students at Bradfield are serious in a low-ego, genuinely-trying-to-help-each-other way. It's energizing to be around other people with so much enthusiasm for the subject matter. I like being around everyone in my cohort without exception.

I've tried joining other programming communities in the past, but they weren't what I was looking for. I found an undercurrent of insecurity and sweat that ruined the vibes for me. There's none of that at Bradfield.

## Money

The year-long CSI is $19,500. The shorter 9-week course, [Software Systems: Behind the Abstractions](https://bradfieldcs.com/courses/ssba/), is $3,600. Either is worth it, easily. Sure, that's nothing to sneeze at, but it's cheap for what you get.

I'm confident that if the CSI's price tag feels like too much, the program can get you to a place career-wise where it doesn't. Many students in CSI cohorts switch jobs, and some make twice as much as they did before. Recently, one quadrupled his income. I paid for CSI with a fraction of the signing bonus I got when I joined my current employer – a job I got thanks in large part to Bradfield courses.

Obligatory disclaimer: the labor market is unusually hot right now so maybe don't count on doubling your income next year, but maybe don't count it out either.

## Accreditation

Bradfield is not an accredited school. I think you can get a certificate of completion if you ask for one? I don't know, whatever. That's not why you do Bradfield. You do Bradfield to attain mastery, to actually get better in real life. You do Bradfield because [this stuff works](https://twitter.com/oznova_/status/1479254530470518786).

Seriously, though, we're lucky to work in an industry that [cares less about credentials than most others](https://ozwrites.com/masters/). There's some advantage to having a formal degree in computer science, but that largely ends after you get your first job.

## Other students' reviews of Bradfield

You don't just take it from me that Bradfield is great – other students have written even more thorough accounts of their time at Bradfield:

- Rohan wrote [My experience of the Bradfield Computer Science Intensive](https://gist.github.com/RP-3/67c77a81274ba6ad4db9e27af8d014cc)
- Julius wrote [My Thoughts on Bradfield](https://gist.github.com/rouxcaesar/9eced2261681efc268789f3fb2c8f958)
- Clifford wrote [My Experience at Bradfield CS](https://gist.github.com/cliffordfajardo/03e580083a3b497e48fa52bfe3d6c04b)

## Closing thoughts

If you're a software engineer, you'll likely benefit tremendously from courses at Bradfield. This stuff works.

If you have questions about Bradfield, you should reach out to them via their contact information on the [Bradfield website](https://bradfieldcs.com/). If you're looking for a student perspective, I'm happy to answer any questions via email at [ivan@echevarria.io](mailto:ivan@echevarria.io).

<br>
<br>

[1]<i id="note">
Oz disputes that he read a lot on pedagogy: "[F]or the record, I don’t read up a whole bunch on pedagogy (some people \*really\* go overboard) but I do read some and do try to get actively better at teaching so I guess it’s the same sentiment :)"
</i>
