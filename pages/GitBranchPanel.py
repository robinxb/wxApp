# -*- coding: utf-8 -*-

import _extend
import utils
import os
import wx

class GitBranchPanel ( _extend.GitBranchPanel ):
	def __init__(self, parent = None):
		super(GitBranchPanel, self).__init__(parent)

	def _OnConfirm( self, event ):
		event.Skip()
		artBranchStr, codeBranchStr = self.m_listArt.GetStringSelection(), self.m_listCode.GetStringSelection()
		self.HotFixBranch(artBranchStr, codeBranchStr)

	def LoadGit(self):
		artGitPath, afcGitPath = utils.path.GetDesignAfcPath(), utils.path.GetCodeGitPath()
		if not os.path.exists(artGitPath) or not os.path.exists(afcGitPath):
			wx.MessageBox(u"请先在设置中设置路径", u'错误', wx.OK | wx.ICON_INFORMATION)
			return
		self.artGit = utils.Git(artGitPath)
		self.codeGit = utils.Git(afcGitPath)
		if not self.artGit.IsGitPath():
			wx.MessageBox(u"美术资源路径无效", u'错误', wx.OK | wx.ICON_ERROR)
			return
		if not self.codeGit.IsGitPath():
			wx.MessageBox(u"程序资源路径无效", u'错误', wx.OK | wx.ICON_ERROR)
			return

		self.m_listArt.Clear()
		current_branch, branches, stdout = self.artGit.GetBranches()
		for b in branches:
			self.m_listArt.Append(b)

		self.m_listCode.Clear()
		current_branch, branches, stdout = self.codeGit.GetBranches()
		for b in branches:
			self.m_listCode.Append(b)

	def HotFixBranch(self, artBranch, codeBranch):
		# checkout to this branch
		artBranch = artBranch.split("/")[-1]
		self.artGit.Checkout(artBranch)

		codeBranch = codeBranch.split("/")[-1]
		self.codeGit.Checkout(codeBranch)

		# get current version
		cur_script_version, cur_major_version = utils.cfg.GetVersion(codeBranch)

		# # prepare for generate hotfix files
		with utils.path.GetNewTempDir() as temp_dir:
			print("*** Generate HotFix file in --> %s \n"%temp_dir)
