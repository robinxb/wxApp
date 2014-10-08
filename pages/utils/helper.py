# -*- coding: utf-8 -*-

import os
import subprocess
import re

class Command( object ):
	def __init__(self, text, cwd = None):
		self.text = text
		self.cwd = cwd

	def execute(self):
		self.proc = subprocess.Popen(self.text,
			shell=True,
			cwd=self.cwd,
			stdout=subprocess.PIPE,
			stdin=subprocess.PIPE,
			stderr=subprocess.PIPE)
		self.proc.wait()

	def SetCWD(self, cwd):
		self.cwd = cwd

class CommandSequence(Command):
	def __init__(self, steps):
		self.steps = steps

	def execute(self):
		for s in self.steps:
			s.execute()

	def SetCWD(self, cwd):
		for s in self.steps:
			s.SetCWD(cwd)

def GetArtGitBranchs(sshObj):
	(sshin, sshout, ssherr) = sshObj.exec_command('cd ~/project/aegean/client/ArtGit && git fetch && git branch -a')
	current = None
	branchList = []
	while True:
		line = sshout.readline()
		if line != '':
			out = line.rstrip('\n')
			br = re.match(r".*(remotes/origin/\w+)", out)
			if not current:
				cbr = re.match(r"\*\ (\w+)", out)
				if cbr:
					current = cbr.groups()[0]
			if br and br.groups()[0][-4:]!= "HEAD":
				branchList.append(br.groups()[0].split("/")[-1])
		else:
			break
	return current, branchList, sshout


def GetCodeGitBranchs(sshObj):
	(sshin, sshout, ssherr) = sshObj.exec_command('cd ~/project/aegean/ && git fetch && git branch -a')
	current = None
	branchList = []
	while True:
		line = sshout.readline()
		if line != '':
			out = line.rstrip('\n')
			br = re.match(r".*(remotes/origin/\w+)", out)
			if not current:
				cbr = re.match(r"\*\ (\w+)", out)
				if cbr:
					current = cbr.groups()[0]
			if br and br.groups()[0][-4:]!= "HEAD":
				branchList.append(br.groups()[0].split("/")[-1])
		else:
			break
	return current, branchList, sshout
