"""
builpy
"""

import os

from _builpy.cli import DEBUG


BASEDIR = os.getcwd()


def dbg(msg):
    if DEBUG:
        print("DEBUG: " + str(msg))


def goto_pkgdir(pkgname):
    dbg("Changing to package directory: " + pkgname)
    pkg = os.path.join(BASEDIR, pkgname)

    if os.access(pkg, os.W_OK):
        os.chdir(pkg)
    else:
        raise OSError("Package directory not accessible or non-existent.")

def goto_srcdir(pkgname, srcname):
    dbg("Changing to source directory: " + pkgname + "/" + srcname)
    src = os.path.join(BASEDIR, pkgname, srcname)

    if os.access(src, os.W_OK):
        os.chdir(src)
    else:
        raise OSError("Source directory not accessible or non-existent.")

def goto_basedir():
    dbg("Changing to base directory: " + BASEDIR)
    if os.access(BASEDIR, os.W_OK):
        os.chdir(BASEDIR)
    else:
        raise OSError("Base directory not writable or vanished.")

