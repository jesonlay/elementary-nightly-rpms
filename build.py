#!/usr/bin/env python3

import os
import subprocess


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


basedir = os.getcwd()
print(basedir)
