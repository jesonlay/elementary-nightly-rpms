"""
builpy.conf
"""

import configparser

from _builpy import dbg
from _builpy import goto_basedir, goto_pkgdir


def get_confval(pkgname, section, key):
    dbg("Getting value from config file: [" + section + "]: " + key)
    assert isinstance(section, str)
    assert isinstance(key, str)

    goto_pkgdir(pkgname)
    pkgconfig = configparser.ConfigParser()
    pkgconfig.read(pkgname + ".conf")
    value = pkgconfig[section][key]
    goto_basedir()

    dbg("Got value from config file: [" + section + "]: " + key + ": " + value)
    return value


def get_pkgvers(pkgname):
    return get_confval(pkgname, "package", "version")

def get_pkgcopr(pkgname):
    return bool(get_confval(pkgname, "package", "copr"))

def get_srcname(pkgname):
    return get_confval(pkgname, "source", "name")

def get_srctype(pkgname):
    return get_confval(pkgname, "source", "type")

def get_srcorig(pkgname):
    return get_confval(pkgname, "source", "origin")

def get_srckeep(pkgname):
    return bool(get_confval(pkgname, "source", "keep"))

def get_copruser(pkgname):
    return get_confval(pkgname, "copr", "user")

def get_coprrepo(pkgname):
    return get_confval(pkgname, "copr", "repo")

