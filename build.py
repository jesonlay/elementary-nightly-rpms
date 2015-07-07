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

	if not debug:
		subprocess.call(["bzr", "pull", "--quiet"])
	else:
		subprocess.call(["bzr", "pull"])
	
	rev_new = subprocess.check_output(["bzr", "revno"])
	
	if rev_new != rev_old:
		return rev_new
	else:
		return -1


def check_update_git():
	rev_old = subprocess.check_output(["git", "rev-parse", "HEAD"])
	
	if not debug:
		subprocess.call(["git", "pull", "--rebase", "--quiet"])
	else:
		subprocess.call(["git", "pull", "--rebase"])
	
	rev_new = subprocess.check_output(["git", "rev-parse", "HEAD"])
	
	if rev_new != rev_old:
		return rev_new
	else:
		return -1


# check_update: goes to usual vcs subdirectory, checks for updates.
# argument name is supposed to be a string (name of package / directory)
# returns True if there are remote changes, returns False if not
def check_update(name):
	assert type(name) is str
	
	basedir = os.getcwd()
	pkg_dir = basedir + "/" + name
	os.chdir(pkg_dir)
	
	if not os.access(name + ".conf", os.W_OK):
		os.chdir(basedir)
		raise(OSError(name + ".conf could not be found or is not writable."))
	
	dbg("Reading package " + name + " configuration file.")
	pkgconfig = configparser.ConfigParser()
	pkgconfig.read(name + ".conf")

	srcname = pkgconfig["source"]["name"]
	os.chdir(srcname)
	
	if os.access(".bzr", os.W_OK):
		dbg("Checking bzr repo for updates.")
		update = check_update_bzr()
		os.chdir(basedir)
		return update
	
	# check if the directory is a git repo
	elif os.access(".git", os.W_OK):
		dbg("Checking git repo for updates.")
		update = check_update_git()
		os.chdir(basedir)
		return update
	
	# directory does not contain a supported VCS (bzr or git)
	else:
		os.chdir(basedir)
		dbg(name + ": " + "Not a supported VCS repository.")
		return False


argparser = argparse.ArgumentParser()
argparser.add_argument("--debug", "-d", action='store_const', const=True, default=False)
args = argparser.parse_args()

debug = args.debug


packages = ["audience", "contractor", "footnote", "gala", "granite", "gsignond", "libgsignon-glib", "noise", "slingshot", "switchboard", "vocal"]

dbg("Checking only for audience at this point in time.")
update = check_update("audience")

