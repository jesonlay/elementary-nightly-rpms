"""
builpy.url
"""

import subprocess

from _builpy import dbg, DEBUG
from _builpy import goto_basedir, goto_pkgdir


def get_source_url(pkgname, orig, dest=None):
    quietstr = "--quiet"
    if DEBUG:
        quietstr = "--verbose"

    goto_pkgdir(pkgname)
    if dest != None:
        dbg("Downloading source tarball " + orig + " to " + dest + ".")
        subprocess.call(["wget", quietstr, orig, "-O", dest])
    else:
        dbg("Downloading source tarball " + orig + ".")
        subprocess.call(["wget", quietstr, orig])
    goto_basedir()
    return -1

#def get_update_url(): would need some additional work
# - version comparison between .conf file and downloaded tarball

