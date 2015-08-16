#!/usr/bin/env python3

import os
import argparse
import subprocess
import configparser

debug = bool()


def dbg(msg):
    if debug:
        print("DEBUG: " + str(msg))

def get_pkgversion(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    pkgversion = pkgconfig["package"]["version"]
    return pkgversion

def get_pkgcopr(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    pkgcopr = pkgconfig["package"]["copr"]
    return pkgcopr

def get_srcname(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srcname = pkgconfig["source"]["name"]
    return srcname

def get_srctype(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srctype = pkgconfig["source"]["type"]
    return srctype

def get_srcdest(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srcdest = pkgconfig["source"]["dest"]
    return srcdest

def get_srckeep(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srckeep = pkgconfig["source"]["keep"]
    return srckeep

def get_copruser(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    copruser = pkgconfig["copr"]["user"]
    return copruser

def get_coprrepo(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    coprrepo = pkgconfig["copr"]["repo"]
    return coprrepo

def check_pkgdir(pkgname):
    return os.access(pkgname, os.W_OK)

def check_srcdir(srcname):
    return os.access(srcname, os.W_OK)


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
        return 0


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
        return 0


# check_update: goes to usual vcs subdirectory, checks for updates.
# argument name is supposed to be a string (name of package / directory)
# returns revno if there are remote changes, returns None if not
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
        return None



argparser = argparse.ArgumentParser(description="Update, build, upload pkgs.")
argparser.add_argument(
        "-d",
        "--debug",
        action="store_const",
        const=True,
        default=False,
        help="enable debug output")
argparser.add_argument(
        "-v",
        "--verbose",
        action="store_const",
        const=True,
        default=False,
        help="enable verbose output")
argparser.add_argument(
        "package",
        action="store",
        nargs="+",
        type=str,
        help="package name")

args = argparser.parse_args()

debug = args.debug or args.verbose
pkgnames = args.package

dbg("packages specified: ")
for i in pkgnames:
    dbg(i)

# update = check_update("audience")










