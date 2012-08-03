---
layout: post
title: "A Pushcode Story"
---

*Fact: Pushcode is the result of a failed job interview.*

I started planning Pushcode after I failed an interview process for a *dream* position with [Mozilla's Web Team](http://blog.mozilla.org/webdev/). I was thrilled to get the interview, and I talked to a couple manager and several members of the team. After many years building web solutions in multiple CMSes (dating back to Dave Winer's [Frontier](http://frontier.userland.com/), but including [Wordpress](http://wordpress.org), [Movable Type](http://www.movabletype.org/), and a few less-well-known systems) my lack of experience in "full-stack" development made for an ill fit. While disappointed, I couldn't really disagree with them. I also decided that Mozilla or no, I needed to branch out, and I was going to get the experience I lacked.

This was at the end of 2010, and the continuous deployment / #[devops](https://twitter.com/#!/search/realtime/%23devops) movement was growing out of work that [Flickr](http://flickr.com)'s ops team (and their transplanted engineers at [Etsy](http://etsy.com)) had done, and I was fascinated. I needed a project, and I decided that I was going to try my hand at building a simple deployment tool. I'd build it from the the ground up (sort of, I wanted to use [Django](http://djangoproject.org) rather than a more bare-bones framework) and teach myself about all the bits and bobs I hadn't explored before.

The first version of Pushcode was code-named "Make it Goo", an inside joke from the internal Six Apart IRC channel that dated to before my time there - and no one ever explained it to me - but I liked the sound if it.

![make it goo](https://img.skitch.com/20110408-xn8m6u9kmdqnwuh15w2m6u44yf.png)

Working on Pushcode has been exactly the process I intended it to be at the beginning, though it's taken longer than I imagined it would. :-) It's not a hugely complicated app (~14k lines of python, html, css, and javascript) but it's big enough that I've delved deeper into various persistence options, worker queues, caching, several 3rd party apis, and so forth.

And I'm a better engineer today than I was when I blew that Mozilla interview. :-)