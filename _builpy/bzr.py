"""
builpy.bzr
"""

import subprocess

from _builpy import dbg, DEBUG
from _builpy import goto_basedir, goto_pkgdir, goto_srcdir

from _builpy.conf import get_srcname


def format_version_bzr(ver, rev):
    """
    builpy.bzr.format_version_bzr()
    function that returns the package version in a standard format
    """
    assert isinstance(ver, str)
    assert isinstance(rev, str)
    return ver + "~rev" + rev


def get_srcrev_bzr(pkgname, srcname):
    """
    builpy.bzr.get_srcrev_bzr()
    function that returns the current revision number of the source branch
    """
    goto_srcdir(pkgname, srcname)
    rev = subprocess.check_output(["bzr", "revno"]).decode().rstrip('\n\r')
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

    cmdstr = "branch"

#    optstr = ""
#    if not keep:
#        cmdstr = "checkout"
#        optstr = "--lightweight"

    goto_pkgdir(pkgname)
    dbg("bzr" + " " + cmdstr + " " + quietstr + " " + orig + " ./" + dest)
    subprocess.call(["bzr", cmdstr, quietstr, orig, "./" + dest])
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
    quietstr = "--quiet"
    if DEBUG:
        quietstr = ""

    rev_old = get_srcrev_bzr(pkgname, srcname)

    goto_srcdir(pkgname, srcname)
    subprocess.call(["bzr", "pull", quietstr])
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

    strvers = format_version_bzr(pkgvers, rev)
    strpkgv = pkgname + "-" + strvers

    filename = "../" + strpkgv + ".tar.gz"

    goto_srcdir(pkgname, srcname)
    subprocess.call(["bzr", "export", filename])
    goto_basedir()

    dbg("Export to ../" + strpkgv + ".tar.gz successful.")

