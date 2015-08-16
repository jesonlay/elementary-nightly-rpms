"""
builpy.cli
"""

import argparse


argparser = argparse.ArgumentParser(description="Update, build, upload pkgs.")
argparser.add_argument(
    "-d",
    "--debug",
    action="store_const",
    const=True,
    default=False,
    help="enable debug output")
argparser.add_argument(
    "-v",
    "--verbose",
    action="store_const",
    const=True,
    default=False,
    help="enable verbose output")
argparser.add_argument(
    "package",
    action="store",
    nargs="+",
    type=str,
    help="package name")

args = argparser.parse_args()

DEBUG = args.debug or args.verbose
PACKAGES = args.package

