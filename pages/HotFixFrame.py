# -*- coding: utf-8 -*-

import _extend
import utils
import paramiko
import base64
import pickle
import json
import wx

LOG_FORMAT = """* %s %s ( %s %s )\n"""

class SimpleBranchDetail(object):
	def __init__(self):
		super(SimpleBranchDetail, self).__init__()
		self.name = None
		self.version = None
		self.codeBranch = None
		self.artBranch = None
		self.uuid = None

class HotFixFrame(_extend.HotFixFrame):
	def __init__(self, parent):
		super(HotFixFrame, self).__init__(parent)
		ip = utils.path.GetBuilderIP()
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		conn = self.ssh.connect(ip, username = 'farmbuilder', password = "farm")
		print '===== SSH connected to %s ====='%(ip)
		self._loadAll()

	def _loadAll(self):
		self.branches = []
		cfgList = self._getValidCfg()
		print cfgList
		for cfg in cfgList:
			obj = SimpleBranchDetail()
			obj.name = cfg[u'name']
			obj.version = cfg[u'version']
			obj.codeBranch = cfg[u'codeBranch']
			obj.artBranch = cfg[u'artBranch']
			obj.uuid = cfg[u'uuid']
			self.branches.append(obj)
		self.m_branchList.Clear()
		for obj in self.branches:
			self.m_branchList.Append(obj.name)

	def __del__(self):
		self.ssh.close()
		print '===== SSH close ====='

	def _getDiffLog(self, isCodePath):
		(sshin, sshout, ssherr) = self.ssh.exec_command('cd ~/project/branch && python hotfix.py difflog %s HEAD dev'%(isCodePath and "True" or "False"))

		ret = ""
		while True:
			line = sshout.readline()
			if line != '':
				ret += line.rstrip('\n')
			else:
				break
		info = base64.b64decode(ret)
		return pickle.loads(info)

	def _getValidCfg(self):
		(sshin, sshout, ssherr) = self.ssh.exec_command('cd ~/project/branch && python hotfix.py getvalidcfg')

		ret = ""
		while True:
			line = sshout.readline()
			if line != '':
				ret += line.rstrip('\n')
			else:
				break
		info = base64.b64decode(ret)
		js = pickle.loads(info)
		ret = []
		for string in js:
			cfg = json.loads(string)
			ret.append(cfg)
		return ret

	def _OnClickBranch( self, event ):
		event.Skip()
		selectId = self.m_branchList.GetSelection()
		if selectId == wx.NOT_FOUND:
			return
		obj = self.branches[selectId]
		self.m_Version.SetValue(obj.version)
		self.m_CodeBranch.SetValue(obj.codeBranch)
		self.m_ArtBranch.SetValue(obj.artBranch)

	def _OnClickHotFix( self, event ):
		event.Skip()
		self.m_diffLog.Clear()
		selectId = self.m_branchList.GetSelection()
		if selectId == wx.NOT_FOUND:
			return
		obj = self.branches[selectId]
		(sshin, sshout, ssherr) = self.ssh.exec_command('cd ~/project/branch && python hotfix.py update %s'%obj.uuid)
		ret = ""
		while True:
			line = sshout.readline()
			if line != '':
				ret += line.rstrip('\n')
				self.m_diffLog.AppendText(line)
			else:
				break

	def _OnClickDiffLog( self, event ):
		event.Skip()
		self.m_diffLog.Clear()
		self.m_diffLog.AppendText(u'正在获取分支log信息，请稍候...')
		logInfo = self._getDiffLog(True)
		self.m_diffLog.Clear()
		for info in logInfo:
			log = LOG_FORMAT%(info['message'].decode('utf-8'), info['hash'], info['date'], info['author'])
			self.m_diffLog.AppendText(log)

