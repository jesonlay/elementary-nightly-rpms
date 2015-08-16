"""
builpy.vcs
"""


from _builpy import dbg

from _builpy.bzr import get_srcrev_bzr, get_source_bzr
from _builpy.bzr import src_update_bzr, src_export_bzr

from _builpy.git import get_srcrev_git, get_source_git
from _builpy.git import src_update_git, src_export_git

from _builpy.url import get_source_url

from _builpy.conf import get_pkgvers, get_srcname, get_srctype


def get_srcrev(pkgname):
    dbg("Checking revision number / commit id.")
    srcname = get_srcname(pkgname)
    srctype = get_srctype(pkgname)

    if srctype == "bzr":
        return get_srcrev_bzr(pkgname, srcname)
    elif srctype == "git":
        return get_srcrev_git(pkgname, srcname)
    else:
        return None

def get_source(pkgname, srctype, srcorig, srcdest, srckeep):
    if srctype is "bzr":
        get_source_bzr(pkgname, srcorig, srcdest, srckeep)
    elif srctype is "git":
        get_source_git(pkgname, srcorig, srcdest, srckeep)
    elif srctype is "url":
        get_source_url(pkgname, srcorig, srcdest)
    else:
        dbg("Source type is not supported.")

def src_update(pkgname):
    srcname = get_srcname(pkgname)
    srctype = get_srctype(pkgname)

    dbg("Checking " + srcname + " " + srctype + " repo for updates.")

    if srctype == "bzr":
        src_update_bzr(pkgname, srcname)
    elif srctype == "git":
        src_update_git(pkgname, srcname)
    elif srctype == "url":
        pass
    else:
        dbg("Source type is not supported.")

def src_export(pkgname):
    pkgvers = get_pkgvers(pkgname)
    srcname = get_srcname(pkgname)
    srctype = get_srctype(pkgname)

    dbg("Exporting " + pkgname + "VCS sources to tarball for use in packaging.")

    if srctype == "bzr":
        src_export_bzr(pkgname, srcname, pkgvers)
    elif srctype == "git":
        src_export_git(pkgname, srcname, pkgvers)
    elif srctype == "url":
        pass
    else:
        dbg("Source type is not supported.")

