---
layout: post
title: Code @ Wallrazer
---

## We Love Statsd

I've really begun to love [Etsy](http://www.etsy.com)'s [StatsD](https://github.com/etsy/statsd) server. I've have a couple of client projects that I'm going to be using it for, so I've been writing client code to talk to the server.

### Python

My first client was written in Python (first I ported the sample PHP code that Etsy provided, then I rolled a proper module).

* [pystatsd](https://github.com/sivy/py-statsd) &mdash; pystatsd is available from Github and [Pypi](pypi.python.org/pypi/pystatsd/), and includes both a client implementation from myself and a server implementation by Josh Frederick.

### Perl

My second client was written in Perl; I do a ton of perl coding for Movable Type, and one day I'm going to want this.

* [Net::StatsD::Client](https://github.com/sivy/statsd-client) &mdash; Once I get the packaging right you'll be able to get it from the [CPAN](http://cpan.org).

### Node.js

No, I don't actually have any Node projects going, but it's fun to code for, so here's a client for node.

* [node-statsd](https://github.com/sivy/node-statsd)