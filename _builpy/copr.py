"""
builpy.copr
"""

import os
import subprocess

from _builpy import goto_basedir
from _builpy.conf import get_pkgcopr, get_coprrepo
from _builpy.rpm import RPMBUILD_DIR, check_rpmbuild


RPMBUILD_SRPMS = os.path.join(RPMBUILD_DIR, "SRPMS")


def copr_build(pkgname):
    """
    builpy.copr.copr_build()
    uploads and builds all srpms in rpmbuild directory
    """
    check_rpmbuild()

    pkgcopr = get_pkgcopr(pkgname)

    if not pkgcopr:
        return None

    coprrepo = get_coprrepo(pkgname)

    os.chdir(RPMBUILD_SRPMS)
    dircontents = subprocess.check_output(["ls"]).decode().split()

    for dir_file in dircontents:
        subprocess.call(["copr-cli", "build", "--nowait", coprrepo, dir_file])

    goto_basedir()

