"""
builpy.bzr
"""

import subprocess

from _builpy import dbg, DEBUG
from _builpy import goto_basedir, goto_pkgdir, goto_srcdir

from _builpy.conf import get_srcname


def get_srcrev_bzr(pkgname, srcname):
    """
    builpy.bzr.get_srcrev_bzr()
    function that returns the current revision number of the source branch
    """
    goto_srcdir(pkgname, srcname)
    rev = subprocess.check_output(["bzr", "revno"]).decode()
    goto_basedir()

    dbg(pkgname + " repo is at revno: " + rev)
    return rev

def get_source_bzr(pkgname, orig, dest, keep=True):
    """
    builpy.bzr.get_source_bzr()
    function that downloads the specified bzr branch or lightweight checkout
    """
    srcname = get_srcname(pkgname)
    dbg("Checking out bzr repository " + orig + " to directory " + dest + ".")

    quietstr = "--quiet"
    if DEBUG:
        quietstr = "--verbose"

    cmdstr = "checkout --lightweight"
    if keep:
        cmdstr = "branch"

    goto_pkgdir(pkgname)
    subprocess.call(["bzr", cmdstr, quietstr, orig, dest])
    goto_basedir()

    dbg("Checkout to " + dest + " successful.")
    rev = get_srcrev_bzr(pkgname, srcname)
    dbg("Revision number of checkout: " + rev)

    return rev

def src_update_bzr(pkgname, srcname):
    """
    builpy.bzr.src_update_bzr()
    function that updates the specified bzr branch or lightweight checkout
    """
    cmdstr = "pull --quiet"
    if DEBUG:
        cmdstr = "pull"

    rev_old = get_srcrev_bzr(pkgname, srcname)

    goto_srcdir(pkgname, srcname)
    subprocess.call(["bzr", cmdstr])
    goto_basedir()

    rev_new = get_srcrev_bzr(pkgname, srcname)

    if rev_new != rev_old:
        return rev_new
    else:
        return 0

def src_export_bzr(pkgname, srcname, pkgvers):
    """
    builpy.bzr.src_export_bzr()
    function that exports the specified bzr branch or lightweight checkout
    to a .tar.gz archive
    """
    rev = get_srcrev_bzr(pkgname, srcname)

    strvers = pkgvers + "~rev" + rev
    strpkgv = pkgname + "-" + strvers

    cmdstr = "export ../" + strpkgv + ".tar.gz"

    goto_srcdir(pkgname, srcname)
    subprocess.call(["bzr", cmdstr])
    goto_basedir()

    dbg("Export to ../" + strpkgv + ".tar.gz successful.")

