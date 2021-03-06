# -*- coding: utf-8 -*-

import os
import re
import path
import helper
import subprocess
import contextlib

newlines = ['\n', '\r\n', '\r']
def unbuffered(proc, stream='stdout'):
    stream = getattr(proc, stream)
    with contextlib.closing(stream):
        while True:
            out = []
            last = stream.read(1)
            if last == '' and proc.poll() is not None:
                break
            while last not in newlines:
                if last == '' and proc.poll() is not None:
                    break
                out.append(last)
                last = stream.read(1)
            out = ''.join(out)
            yield out

def _progress(cmd, fn = None, cwd = None):
    cmd = ['git'] + cmd + ["--progress"]
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        cwd = cwd
    )
    for line in unbuffered(proc):
    	print(line)
    	if fn:
	        fn(line)


class Git(object):
	def __init__(self, path):
		super(Git, self).__init__()
		self.path = path

	def Clone(self, repo, cb):
		_progress(["clone", repo], fn = cb, cwd = self.path)

	def Push(self, cb):
		_progress(["push",], fn = cb, cwd = self.path)

	def Push(self, cb):
		_progress(["push",], fn = cb, cwd = self.path)

	def AddAll(self):
		proc = subprocess.Popen(["git", "add", "."],
			cwd=self.path
			)
		proc.wait()

	def AllCommit(self, text = "Auto commit"):
		proc = subprocess.Popen(["git", "commit", "--all", "-m", text],
			cwd=self.path
			)
		proc.wait()

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
		self._command(["git reset --hard HEAD", "git clean -df", "git checkout %s"%branchStr], self.path)

	def Pull(self):
		self._command("git pull", self.path)

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
