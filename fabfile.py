# this should be fun
from __future__ import with_statement
from fabric.api import *

env.hosts = ['deploy@hammer.wallrazer.com']
env.working_dir = ''
env.build_dir = ''
env.deploy_dir = ''

from pystatsd import Client


def prod():
    env.working_dir = "/tmp/wallrazer.com"
    env.build_dir = "/tmp/wallrazer.com/_site"
    env.deploy_dir = "/var/www/default"


def stage():
    env.working_dir = "/tmp/hammer.wallrazer.com"
    env.build_dir = "/tmp/hammer.wallrazer.com/_site"
    env.deploy_dir = "/var/www/hammer"


def record(millis):
    c = Client('hammer.wallrazer.com', 8125)
    print "recording...\n"
    c.increment('wallrazer.deploys')
    c.timing('wallrazer.deploys.time', millis)


def generate():
    local('jekyll')


def pack():
    generate()
    local('tar czf ~/tmp/wr_site.tgz _site')


def deploy():
    from datetime import datetime
    start = datetime.now()

    with cd(env.working_dir):
        run('git pull')
        run('. /var/lib/gems/1.8/bin/jekyll')
        run('cp -R %s/* %s' % (env.build_dir, env.deploy_dir))
    end = datetime.now()
    dur = (end - start).microseconds / 1000

    record(dur)
