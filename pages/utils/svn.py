# -*- coding: utf-8 -*-

import os
import re
import path
import helper

class SVN(object):
	def __init__(self, path):
		super(SVN, self).__init__()
		self.path = path

	def IsSVNPath(self):
		if not os.path.isdir(self.path):
			return False
		cmd = helper.Command("svn status", self.path)
		cmd.execute()
		for line in cmd.proc.stderr:
			if "W155007" in line:
				return False
		return True

	def GetPath(self):
		return self.path

