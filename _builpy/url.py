"""
builpy.url
"""

import subprocess

from _builpy import dbg, DEBUG
from _builpy import goto_basedir, goto_pkgdir


def format_version_url(ver):
    """
    builpy.url.format_version_url()
    function that returns the package version in a standard format (trivial here)
    """
    assert isinstance(ver, str)
    return ver


def get_source_url(pkgname, orig, dest=None):
    """
    builpy.url.get_source_url()
    function that downloads a file via the specified url (wget)
    curl could also be supported in the future
    """
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

