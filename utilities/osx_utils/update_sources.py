#!/usr/bin/python

#
#	Updates source repos by executing 'git pull'
#

import os, sys, getopt, subprocess, json
from subprocess import call
config = json.loads(open('./config.json').read())

def main(argv):
	targetDir = '.' if len(argv) == 0 else argv[0];

	for repo in config['repos']:
		subprocess.call(['git','pull'], cwd = config['sourcesdir']+'/'+repo['name'])

	print 'All geppetto repos updated'

if __name__ == "__main__":
	main(sys.argv[1:])
