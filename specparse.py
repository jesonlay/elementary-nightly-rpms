#!/usr/bin/env python3

import os
import subprocess


tag_dict = dict()
tag_dict["name"] = "Name"
# "summary", "version", "release", ...]


"""
def macro_proc(string):
	if "%define" is in string:
		return value
	elif "%description" is in string:
		return READ MORE LINES
	else:
		split at " "
		return value
"""

"""
def tag_proc(string):
	tpl = split at ":"
	if tpl[0].tolower() is not in tag_dict.keys():
		raise(RpmError("This Tag is not supported (yet)."))
	
	return (tpl[0].tolower(), tpl[1])

"""

class Source:
	def __init__(self):
		self.num = ""
		self.str = ""

class Patch:
	def __init__(self):
		self.num = ""
		self.str = ""


class Package:
	def __init__(self):
		self.package = ""
		self.summary = ""
		self.bldreqs = ""
		self.require = ""
		self.filecmd = ""			# e.g. for -f package.lang
		self.filelst = list()


class RpmSpec(Package):
	def __init__(self):
		super().__init__()
		self.defines = list()
		
		self.package = ""
		self.summary = ""
		self.version = ""
		self.release = ""
		self.license = ""
		self.url = ""
		
		self.sources = list()
		self.patches = list()
		self.description = list()
		self.subpkgs = list()
		self.newpkgs = list()
		
		self.prep_cmds = list()
		self.build_cmds = list()
		self.inst_cmds = list()
		self.post_cmds = list()
		self.postun_cmds = list()
		self.check_cmds = list()
		
		self.changelog = list()
	
	
	def read(self, path):
		assert type(path) is str
		
		if not os.access(path, os.R_OK):
			raise(OSError("Specified file cound not be opened."))
		
		specfile = open(path, encoding="utf-8")
		
		line = str()
		tags = dict()
		
		while line is not ""
			line = specfile.readline()
			
			if line[0] is "%":
				tpl = macro_process(line)
				tags[tpl[1]] = tpl[2]
			else if ":" is in line:
				tpl = tag_process(line)
				tags[tpl[1]] = tpl[2]
		
