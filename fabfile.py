# this should be fun
from __future__ import with_statement
from fabric.api import *

env.hosts = ['monkinetic@monkinetic.com']

from pystatsd import Client

def record(millis):
    c = Client('rayners.org',8125)
    print "recording...\n"
    c.increment('wallrazer.deploys')
    c.timing('wallrazer.deploys.time',millis)

def generate():
    local('jekyll')

def pack():
    generate()
    local('tar czf ~/tmp/wr_site.tgz _site')

def deploy():
    from datetime import datetime
    start = datetime.now()
    pack()
    put ('~/tmp/wr_site.tgz','tmp')
    with cd('wallrazer.com'):
        run ('tar xzf ~/tmp/wr_site.tgz')
    end = datetime.now()
    dur = (end-start).microseconds/1000
    record(dur)