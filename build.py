#!/usr/bin/env python3

import os
import argparse
import subprocess
import configparser

debug = bool()


def dbg(msg):
    assert type(msg) is str
    if debug:
        print("DEBUG: " + msg)


def check_update_bzr():
	rev_old = subprocess.check_output(["bzr", "revno"])
	subprocess.call(["bzr", "pull"])
	rev_new = subprocess.check_output(["bzr", "revno"])
	return (rev_new != rev_old)

def check_update_git():
	rev_old = subprocess.check_output(["git", "rev-parse", "HEAD"])
	subprocess.call(["git", "pull", "--rebase"])
	rev_new = subprocess.check_output(["git", "rev-parse", "HEAD"])
	return (rev_new != rev_old)

# check_update: goes to usual vcs subdirectory, checks for updates.
# argument name is supposed to be a string (name of package / directory)
# returns True if there are remote changes, returns False if not
def check_update(name):
	assert type(name) is str
	
	basedir = os.getcwd()
	
	vcsdir = basedir + "/" + name + "/" + name
	
	os.chdir(vcsdir)
	
	if os.access(".bzr", os.W_OK):
		updates = check_update_bzr()
		os.chdir(basedir)
		return updates
	
	# check if the directory is a git repo
	elif os.access(".git", os.W_OK):
		updates = check_update_git()
		os.chdir(basedir)
		return updates
	
	# directory does not contain a supported VCS (bzr or git)
	else:
		os.chdir(basedir)
		print("Not a supported VCS repository.")
		return False


argparser = argparse.ArgumentParser()
argparser.add_argument("--debug", "-d", action='store_const', const=True, default=False)
args = argparser.parse_args()

debug = args.debug

dbg("This is a test for the debug message printer.")
