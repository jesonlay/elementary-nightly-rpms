"""
builpy.check
"""

import os

from _builpy.conf import get_srcname


def pkg_check(pkgname):
    confpath = os.path.join(BASEDIR, pkgname, pkgname + ".conf")

    if not os.access(pkgname, os.W_OK):
        raise OSError("Package directory does not exist or is inaccessible.")

    if not os.access(confpath, os.R_OK):
        raise OSError("Package .conf does not exist or is inaccessible.")

def src_check(pkgname):
    srcname = get_srcname(pkgname)
    srcdir = os.path.join(BASEDIR, pkgname, srcname)

    if not os.access(srcdir, os.W_OK):
        raise OSError("Source directory does not exist or is inaccessible.")

