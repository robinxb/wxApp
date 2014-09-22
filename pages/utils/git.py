# -*- coding: utf-8 -*-

import os
import re
import path
import helper

class Git(object):
	def __init__(self, path):
		super(Git, self).__init__()
		self.path = path

	def IsGitPath(self):
		if not os.path.isdir(self.path):
			return False
		cmd = helper.Command("git status", self.path)
		cmd.execute()
		for line in cmd.proc.stderr:
			if "fatal: Not a git repository" in line:
				return False
		return True

	def GetBranches(self):
		cmd = helper.Command("git branch -a", self.path)
		cmd.execute()

		stdout = ""
		current = None
		branchList = []
		for line in cmd.proc.stdout:
			stdout += line.rstrip() + "\n"
			br = re.match(r".*(remotes/origin/\w+)", line)
			if not current:
				cbr = re.match(r"\*\ (\w+)", line)
				if cbr:
					current = cbr.groups()[0]
			if br and br.groups()[0][-4:]!= "HEAD":
				branchList.append(br.groups()[0])
		return current, branchList, stdout

	def Checkout(self, branchStr):
		self._command(["git clean -df", "git checkout .", "git checkout %s"%branchStr], self.path)

	def Pull(self):
		self._command("git pull", self.path)

	def Commit(self, args = ""):
		self._command("git commit %s"%args)

	def Add(self, files = "."):
		self._command("git add %s"%files)

	def Fetch(self):
		pass

	def _command(self, cmdList, cwd = None):
		if type(cmdList) is list or type(cmdList) is tuple:
			seq = []
			for s in cmdList:
				assert(type(s) is str or type(s) is unicode)
				seq.append(helper.Command(s, cwd=cwd))
			helper.CommandSequence(seq).execute()
		elif type(cmdList) is str:
			return self._command([cmdList], cwd)
		else:
			raise NameError, "cmd must be list, there is a " + str(type(cmdList))

	def InitWithArtGit(self):
		cmd = helper.Command("git clone ssh://git@oa.ejoy.com/afc.git %s"%(self.path.split(os.sep)[-1]), os.path.dirname(r"%s"%self.path))
		cmd.execute()

		stderr = ""
		for line in cmd.proc.stderr:
			if "Cloning" not in line:
				stderr += line
		if stderr != "":
			return False, stderr
		else:
			stdout = ""
			for line in cmd.proc.stdout:
				stdout += line
			return True, stdout

	def GetPath(self):
		return self.path
