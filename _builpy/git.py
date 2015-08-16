"""
builpy.git
"""

import subprocess

from _builpy import dbg, DEBUG
from _builpy import goto_basedir, goto_pkgdir, goto_srcdir

from _builpy.conf import get_srcname


def get_srcrev_git(pkgname, srcname):
    """
    builpy.git.get_srcrev_git()
    function that returns the current commit id of the source clone
    """
    goto_srcdir(pkgname, srcname)
    rev = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode()
    goto_basedir()

    dbg(pkgname + " repo is at commit: " + rev)
    return rev

def get_source_git(pkgname, orig, dest, keep=False):
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
    rev = get_srcrev_git(pkgname, srcname)

    strvers = pkgvers + "~rev" + rev
    strpkgv = pkgname + "-" + strvers

    cmdstr = "archive --format=tar.gz --prefix=" + \
             strpkgv + "/ HEAD > ../" + strpkgv + ".tar.gz"

    goto_srcdir(pkgname, srcname)
    subprocess.call(["git", cmdstr])
    goto_basedir()

    dbg("Export to ../" + strpkgv + ".tar.gz successful.")
