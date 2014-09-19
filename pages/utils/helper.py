# -*- coding: utf-8 -*-

import os
import subprocess

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

