"""
builpy.git
"""

import subprocess

from _builpy import dbg, DEBUG, get_date
from _builpy import goto_basedir, goto_pkgdir, goto_srcdir

from _builpy.conf import get_srcname


def format_version_git(ver, rev):
    """
    builpy.git.format_version_git()
    function that returns the package version in a standard format
    """
    assert isinstance(ver, str)
    assert isinstance(rev, str)
    date = get_date()

    return ver + "~git" + date + "-" + rev


def get_srcrev_git(pkgname, srcname):
    """
    builpy.git.get_srcrev_git()
    function that returns the current commit id of the repository
    """
    goto_srcdir(pkgname, srcname)
    rev = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode()
    rev = rev.rstrip('\r\n')[0:8]
    goto_basedir()

    dbg(pkgname + " repo is at commit: " + rev)
    return rev

def get_source_git(pkgname, orig, dest, keep=False):
    """
    builpy.git.get_source_git()
    function that downloads the specified git repository (whole or shallow)
    """
    srcname = get_srcname(pkgname)
    dbg("Checking out git repository " + orig + " to directory " + dest + ".")

    quietstr = "--quiet"
    if DEBUG:
        quietstr = "--verbose"

    cmdstr = "clone --depth=1"
    if keep:
        cmdstr = "clone"

    goto_pkgdir(pkgname)
    subprocess.call(["git", cmdstr, quietstr, orig, dest])
    goto_basedir()

    dbg("Checkout to " + dest + " successful.")
    rev = get_srcrev_git(pkgname, srcname)
    dbg("Revision of checkout: " + rev)

    return rev

def src_update_git(pkgname, srcname):
    """
    builpy.git.src_update_git()
    function that updates the specified git repository
    """
    cmdstr = "pull --rebase --quiet"
    if DEBUG:
        cmdstr = "pull --rebase"

    rev_old = get_srcrev_git(pkgname, srcname)

    goto_srcdir(pkgname, srcname)
    subprocess.call(["git", cmdstr])
    goto_basedir()

    rev_new = get_srcrev_git(pkgname, srcname)

    if rev_new != rev_old:
        return rev_new
    else:
        return 0

def src_export_git(pkgname, srcname, pkgvers):
    """
    builpy.git.src_export_git()
    function that exports the specified git repository
    """
    rev = get_srcrev_git(pkgname, srcname)

    strvers = format_version_git(pkgvers, rev)
    strpkgv = pkgname + "-" + strvers

    cmdstr = "archive --format=tar.gz --prefix=" + \
             strpkgv + "/ HEAD > ../" + strpkgv + ".tar.gz"

    goto_srcdir(pkgname, srcname)
    subprocess.call(["git", cmdstr])
    goto_basedir()

    dbg("Export to ../" + strpkgv + ".tar.gz successful.")

