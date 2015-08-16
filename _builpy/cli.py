"""
builpy.cli
"""

import argparse


CLIPARSER = argparse.ArgumentParser(description="Update, build, upload pkgs.")
CLIPARSER.add_argument(
    "-d",
    "--debug",
    action="store_const",
    const=True,
    default=False,
    help="enable debug output")
CLIPARSER.add_argument(
    "-v",
    "--verbose",
    action="store_const",
    const=True,
    default=False,
    help="enable verbose output")
CLIPARSER.add_argument(
    "package",
    action="store",
    nargs="+",
    type=str,
    help="package name")

CLI_ARGS = CLIPARSER.parse_args()

DEBUG = CLI_ARGS.debug or CLI_ARGS.verbose
PACKAGES = CLI_ARGS.package

