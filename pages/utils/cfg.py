# -*- coding: utf-8 -*-

import os
import re
import ConfigParser
import path

__ALL__ = ["GetBranchCfg"]

BRANCH_CFG_NAME = "branch.cfg"
BRANCH_CFG_CONTENT_INIT = """
[version]
script-version = 0
major-version = 0

[login]
login-notify-content = 　《我的爱琴海》删档测试将于9月4日（今晚）24点结束。
	　
	　　衷心感谢大家的包容、投入、建议！
	　
	　　让我们期待下次测试，更多信息敬请关注《我的爱琴海》陌陌吧。

login-notify-title = 温馨提示
forbid-login = 0

"""

class BranchConfig(object):
	"""config object for branch.cfg """

	def __init__(self, path):
		super(BranchConfig, self).__init__()
		self.path = path
		with open(path) as fp:
			self.config = ConfigParser.ConfigParser()
			self.config.readfp(fp)

	def GetScriptVersion(self):
		return self.config.getint("version", "script-version")

	def GetMajorVersion(self):
		return self.config.getint("version", "major-version")

	def IncScriptVersion(self):
		self.config.set("version", "script-version", str(self.GetScriptVersion() + 1))
		self._writeToCfg()
		return self.GetScriptVersion()

	def IncMajorVersion(self):
		self.config.set("version", "script-version", str(self.GetMajorVersion() + 1))
		self._writeToCfg()
		return self.GetMajorVersion()

	def _writeToCfg(self):
		with open(self.path, "w") as fp:
			self.config.write(fp)

def GetBranchCfg(branch):
	cfgpath = path.GetHotFixBasePath() + os.sep + branch + os.sep + BRANCH_CFG_NAME
	basedir = os.path.dirname(cfgpath)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	if not os.path.isfile(cfgpath):
		with open(cfgpath, "w+") as f:
			f.write(BRANCH_CFG_CONTENT_INIT)
			f.close()

	return BranchConfig(cfgpath)

def GetScriptVersion(branch):
	return GetBranchCfg(branch).GetScriptVersion()

def GetMajorVersion(branch):
	return GetBranchCfg(branch).GetMajorVersion()

def IncScriptVersion(branch):
	return GetBranchCfg(branch).IncScriptVersion()

def IncMajorVersion(branch):
	return GetBranchCfg(branch).IncMajorVersion()

def GetVersion(branch):
	cfg = GetBranchCfg(branch)
	return cfg.GetScriptVersion(), cfg.GetMajorVersion()