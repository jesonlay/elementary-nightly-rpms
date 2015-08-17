"""
builpy.rpm
"""

import os
import shutil
import subprocess

from _builpy import dbg, HOME, BASEDIR
from _builpy import goto_basedir
from _builpy.check import home_check


RPMBUILD_DIR = os.path.join(HOME, "rpmbuild")
RPMBUILD_OLD = os.path.join(HOME, "rpmbuild_old")
RPMBUILD_SPECS = os.path.join(RPMBUILD_DIR, "SPECS")
RPMBUILD_SOURCES = os.path.join(RPMBUILD_DIR, "SOURCES")


def check_rpmbuild():
    """
    builpy.rpm.check_rpmbuild()
    function that checks $HOME/rpmbuild, rpmbuild/SOURCES and rpmbuild/SPECS
    for existence and writability
    """
    home_check()
    dbg("Checking for writable HOME directory.")

    if not os.access(RPMBUILD_DIR, os.W_OK):
        raise OSError("rpmbuild directory not existent or not writable.")
    if not os.access(RPMBUILD_SOURCES, os.W_OK):
        raise OSError("rpmbuild SOURCES directory not existent or not writable.")
    if not os.access(RPMBUILD_SPECS, os.W_OK):
        raise OSError("rpmbuild SPECS directory not existent or not writable.")

def rpmbuild_create_dirs():
    """
    builpy.rpm.rpmbuild_create_dirs()
    function that creates neccessary directories for rpmbuild:
    $HOME/rpmbuild/SOURCES, $HOME/rpmbuild/SPECS
    moves away pre-existing rpmbuild directory to rpmbuild_old
    """
    home_check()
    dbg("Checking for writable HOME directory.")

    if os.path.exists(RPMBUILD_DIR):
        shutil.move(RPMBUILD_DIR, RPMBUILD_OLD)
        dbg("Moved old rpmbuild directory away.")

    os.mkdir(RPMBUILD_DIR)
    os.mkdir(RPMBUILD_SPECS)
    os.mkdir(RPMBUILD_SOURCES)
    dbg("Changed to new rpmbuild directory and creating SOURCES and SPECS.")

def rpmbuild_remove_dirs():
    """
    builpy.rpm.rpmbuild_remove_dirs()
    function that removes temporary directories for rpmbuild
    moves back pre-existing rpmbuild directory to rpmbuild_old
    """
    home_check()
    dbg("Checking for writable HOME directory.")

    if os.path.exists(RPMBUILD_DIR):
        shutil.rmtree(RPMBUILD_DIR)
        dbg("Removed temporary rpmbuild directory.")

    if os.path.exists(RPMBUILD_OLD):
        shutil.move(RPMBUILD_OLD, RPMBUILD_DIR)
        dbg("Moved old rpmbuild backup back into original place.")

def rpmbuild_copy_sources(pkgname):
    """
    builpy.rpm.rpmbuild_copy_sources()
    function that copies sources and spec files to rpmbuild directory
    """
    check_rpmbuild()

    pkgdir = os.path.join(BASEDIR, pkgname)
    pkgdir_content = subprocess.check_output(["ls", pkgdir]).decode()
    patches = ".patch" in pkgdir_content

    if patches:
        os.system("cp " + pkgdir + r"/*.patch " + RPMBUILD_SOURCES + "/")

    os.system("cp " + pkgdir + r"/*.tar.gz " + RPMBUILD_SOURCES + "/")
    os.system("cp " + pkgdir + r"/*.conf " + RPMBUILD_SOURCES + "/")
    os.system("cp " + pkgdir + r"/*.spec " + RPMBUILD_SPECS + "/")

def rpmbuild_build_srpm(pkgname):
    """
    builpy.rpm.rpmbuild_build_srpm()
    function that builds srpm in rpmbuild/SRPMS
    prerequisite: execution of rpmbuild_copy_sources()
    """
    check_rpmbuild()

    os.chdir(RPMBUILD_SPECS)
    subprocess.call(["rpmbuild", "-bs", "./" + pkgname + ".spec"])
    goto_basedir()

