#!/usr/bin/env python3

import os
import argparse
import subprocess
import configparser

DEBUG = bool()


def dbg(msg):
    if DEBUG:
        print("DEBUG: " + str(msg))

def get_pkgversion(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    pkgversion = pkgconfig["package"]["version"]
    return pkgversion

def get_pkgcopr(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    pkgcopr = bool(pkgconfig["package"]["copr"])
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

def get_srcorig(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srcorig = pkgconfig["source"]["origin"]
    return srcorig

def get_srckeep(pkgname):
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    srckeep = bool(pkgconfig["source"]["keep"])
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

def check_conffile(pkgname):
    return os.access(pkgname + ".conf", os.R_OK)

def check_source(srcname):
    return os.access(srcname, os.W_OK)


def get_srcrev_bzr(srcname):
    cwddir = os.getcwd()
    srcdir = os.path.join(cwddir, dest)
    
    os.chdir(srcdir)
    rev = subprocess.check_output(["bzr", "revno"])
    os.chdir(cwddir)
    
    return rev

def get_srcrev_git(srcname):
    cwddir = os.getcwd()
    srcdir = os.path.join(cwddir, dest)

    os.chdir(srcdir)
    rev = subprocess.check_output(["git", "rev-parse", "HEAD"])
    os.chdir(cwddir)

    return rev

def get_srcrev(srcname, srctype):
    if srctype is "bzr":
        return get_srcrev_bzr(srcname)
    elif srctype is "git":
        return get_srcrev_git(srcname)
    else:
        return None


def get_source_bzr(orig, dest, keep=True):
    dbg("Checking out bzr repository " orig " to directory " dest ".")

    quietstr = "--quiet"
    if DEBUG:
        quietstr="--verbose"

    cmdstr = "checkout --lightweight"
    if keep:
        cmdstr = "branch"

    subprocess.call(["bzr", cmdstr, quietstr, orig, dest])

    if check_source(dest):
        dbg("Checkout to " dest " successful.")
        rev = get_srcrev_bzr(dest)
        dbg("Revision number of checkout: " rev)
        return rev

    else:
        raise OSError("Checkout directory could not be read.")


def get_source_git(orig, dest, keep=False):
    dbg("Checking out git repository " orig " to directory " dest ".")
    
    quietstr = "--quiet"
    if DEBUG:
        quietstr = "--verbose"
    
    cmdstr = "clone --depth=1"
    if keep:
        cmdstr = "clone"

    subprocess.call(["git", cmdstr, quietstr, orig, dest])

    if check_source(dest):
        dbg("Checkout to " dest " successful.")
        rev = get_srcrev_git(dest)
        dbg("Revision of checkout: " rev)
        return rev

    else:
        raise OSError("Checkout directory could not be read.")


def get_source_url(orig, dest=None, keep=True):
    if dest != None:
        dbg("Downloading source tarball " orig " to " dest ".")
        subprocess.call(["wget", orig, "-O", dest])
    else:
        dbg("Downloading source tarball " orig ".")
        subprocess.call(["wget", orig])
    return -1


def get_source(srctype, srcorig, srckeep):
    if srctype is "bzr":
        get_source_bzr(srcorig, srcdest, srckeep)
    elif srctype is "git":
        get_source_git(srcorig, srcdest, srckeep)
    elif srctype is "url":
        get_source_url(srcorig, srcdest)
    else:
        dbg("Source type is not supported.")


def check_update_bzr():
    rev_old = subprocess.check_output(["bzr", "revno"])

    if not DEBUG:
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

    if not DEBUG:
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
def check_update(pkgname):
    assert isinstance(pkgname, str)
    cwddir = os.getcwd()

    pkgdir = os.path.join(cwddir, pkgname)

    if !check_pkgdir(pkgdir):
        raise OSError("Package directory" pkgdir "could not be opened.")

    dbg("Changing to package directory.")
    os.chdir(pkgdir)

    if !check_conffile(name):
        raise OSError("Configuration file " name ".conf could not be opened.")

    dbg("Reading from configuration file: source directory")
    srcname = get_srcname(pkgname)
    srcdir = os.path.join(pkgdir, srcname)

    dbg("Checking for source existence.")
    if !check_srcdir(srcdir):
        dbg("Sources not found, will be downloaded.")
        dbg("Reading from configuration file: source type")
        srctype = get_srctype(pkgname)
        dbg("Reading from configuration file: source origin")
        srcorig = get_srcorig(pkgname)
        dbg("Reading from configuration file: source keeping")
        srckeep = get_srckeep(pkgname)
        get_source(srctype, srcorig, srckeep)

    dbg("Changing to source directory."
    os.chdir(srcdir)

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

DEBUG = args.debug or args.verbose
pkgnames = args.package

dbg("packages specified: ")
for i in pkgnames:
    dbg(i)

for package in pkgnames:
    dbg("Updating (not really): " + package)

