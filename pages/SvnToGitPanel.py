# -*- coding: utf-8 -*-

import _extend

import utils
import os
import SvnToGitProcess
import wx
import threading
import shutil

# SRC DEST
COPY_INFO = [
	("convert", os.path.join("common", "convert")),
	(os.path.join("resource", "res"), "res"),
	(os.path.join("resource", "res_bin"), "res_bin"),
	(os.path.join("resource", "audio"), "audio"),
	(os.path.join("resource", "script_bin"), "script_bin"),
	(os.path.join("resource", "launcher"), os.path.join("common", "launcher")),
]

class SvnToGitPanel(_extend.SvnToGitPanel):
	def __init__(self, parent):
		super(SvnToGitPanel, self).__init__(parent)

	def LoadPath(self):
		self.m_ArtBranchList.Clear()
		artPath = utils.path.GetDesignAfcPath()
		if artPath and os.path.exists(artPath):
			self.afcGit = utils.Git(artPath)
			assert(self.afcGit.IsGitPath())
			current_branch, branches, stdout = self.afcGit.GetBranches()
			for b in branches:
				self.m_ArtBranchList.Append(b)
		svnPath = utils.path.GetSVNPath()
		if svnPath and os.path.exists(svnPath):
			self.m_ArtPicker.SetPath(svnPath)

	# Virtual event handlers, overide them in your derived class
	def _OnClickConfirm( self, event ):
		event.Skip()
		self._CopyFiles()

	#### STEP 1
	def _CopyFiles(self):
		self.m_ToCopyList = COPY_INFO[:]
		if self._CheckTrans(self.m_ArtBranchList.GetStringSelection()):
			self.m_ProcessBar = SvnToGitProcess.SvnToGitProcess(self)
			self.m_ProcessBar.Show()
			self.m_ProcessBar.m_Text.Clear()
			self.m_ProcessBar.m_Text.Enable(False)
			self.m_ProcessBar.m_Text.AppendText(u"正在计算大小\n")
			self._StartTrans()

	def _CheckTrans(self, gitbranch):
		if not gitbranch or gitbranch == "":
			wx.MessageBox(u"请选择美术分支", u'错误', wx.OK | wx.ICON_ERROR)
			return False
		self.afcGit = utils.Git(utils.path.GetDesignAfcPath())
		if not self.afcGit.IsGitPath():
			wx.MessageBox(u"Git路径不对，请在配置中设置为正确的路径", u'错误', wx.OK | wx.ICON_ERROR)
			return False
		self.afcGit.Checkout(gitbranch.split("/")[-1])
		self.afcSVN = utils.SVN(utils.path.GetSVNPath())
		if not self.afcSVN.IsSVNPath():
			wx.MessageBox(u"SVN路径不对，请在配置中设置为正确的路径", u'错误', wx.OK | wx.ICON_ERROR)
			return False
		return True

	def _StartTrans(self):
		info = self.m_ToCopyList.pop(0)
		src, dest = info[0], info[1]
		self.Bind(utils.evtdef.EVT_COPY_COUNT, self._OnCopyCount)
		self.Bind(utils.evtdef.EVT_COPY_END, self._OnCopyEnd)
		t = CopyThread(self, os.path.join(self.afcSVN.GetPath(), src), os.path.join(self.afcGit.GetPath(), dest))
		t.start()

	def _OnCopyCount(self, evt):
		self.m_ProcessBar.m_Text.AppendText(u'copy %s\n'%evt.GetDestFile())
		self.m_ProcessBar.m_gauge1.SetRange(evt.GetFileCount())
		self.m_ProcessBar.m_gauge1.SetValue(evt.GetCopied())

	def _OnCopyEnd(self, evt):
		totalFileCnt = evt.GetTotal()
		if len(self.m_ToCopyList) > 0:
			self._StartTrans()
		else:
			self._CommitToGit()

	#### STEP 2
	def _CommitToGit(self):
		self.m_ProcessBar.m_Text.AppendText(u"正在提交至服务器\n")
		self.afcGit.Add()
		self.afcGit.Commit('-a -m "update from svn"')
		self.m_ProcessBar.m_Finished = True
		self.m_ProcessBar.m_Text.AppendText(u"完成\n")

class CopyThread(threading.Thread):
	def __init__(self, parent, src, dest):
		super(CopyThread, self).__init__()
		self.parent = parent
		self.src = src
		self.dest= dest

	def countFile(self, src):
		files = []
		if os.path.isdir(src):
			for path, dirs, filenames in os.walk(src):
				files.extend(filenames)
		return len(files)

	def makedirs(self, path):
		if not os.path.exists(path):
			os.makedirs(path)

	def run(self):
		self._copyWithProgress(self.src, self.dest)

	def _copyWithProgress(self, src, dest):
		numFiles = self.countFile(src)
		if numFiles > 0:
			self.makedirs(dest)
			numCopied = 0
			for path, dirs, filenames in os.walk(src):
				filenames = [f for f in filenames if not f[0] == '.']
				dirs[:] = [d for d in dirs if not d[0] == '.']
				for directory in dirs:
					destDir = path.replace(src, dest)
					self.makedirs(os.path.join(destDir, directory))

				for sfile in filenames:
					srcFile = os.path.join(path, sfile)
					destFile = os.path.join(path.replace(src, dest), sfile)
					shutil.copy(srcFile, destFile)
					numCopied += 1
					evt = utils.evtdef.EventCopyCount(utils.evtdef.myEVT_COPY_COUNT, -1, numCopied, destFile, numFiles)
					wx.PostEvent(self.parent, evt)

		evt = utils.evtdef.EventCopyEnd(utils.evtdef.myEVT_COPY_END, -1, numFiles)
		wx.PostEvent(self.parent, evt)
