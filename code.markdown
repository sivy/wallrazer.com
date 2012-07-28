---
layout: post
title: Code @ Wallrazer
---

## We Love Statsd

At Wallrazer we've really begun to love [Etsy](http://www.etsy.com)'s [StatsD](https://github.com/etsy/statsd) server, and we've been writing client code to talk to the server.

### Python

Our first client was written in Python (first ported from the Etsy's sample PHP code, then rolled up as a proper module).

* [pystatsd](https://github.com/sivy/py-statsd) &mdash; pystatsd is available from Github and [Pypi](pypi.python.org/pypi/pystatsd/), and includes both a client implementation Steve wrote and a server implementation by Josh Frederick.

### Perl

A second client, written in Perl; We've done a ton of perl code for Movable Type, and figured one day we'd this.

* [Net::StatsD::Client](https://github.com/sivy/statsd-client) &mdash; Once I get the packaging right you'll be able to get it from the [CPAN](http://cpan.org).

### Node.js

No, we don't actually have any Node projects going, but it's fun to code for, so here's a client for node.

* [node-statsd](https://github.com/sivy/node-statsd)