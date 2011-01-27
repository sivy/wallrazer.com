# this should be fun
from __future__ import with_statement
from fabric.api import *

env.hosts = ['monkinetic@monkinetic.com']

def generate():
	local('jekyll')

def pack():
	local('tar czf ~/tmp/wr_site.tgz _site')

def deploy():
	pack()
	put ('~/tmp/wr_site.tgz','tmp')
	with cd('wallrazer.com'):
		run ('tar xzf ~/tmp/wr_site.tgz')