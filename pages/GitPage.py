# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import utils
import os

from ErrorDialog import ErrorDialog

###########################################################################
## Class GitBranchPanel
###########################################################################

class GitBranchPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"选择代码分支", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer10.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_listCodeChoices = []
		self.m_listCode = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listCodeChoices, 0 )
		bSizer10.Add( self.m_listCode, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"选择美术分支", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer11.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_listArtChoices = []
		self.m_listArt = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listArtChoices, 0 )
		bSizer11.Add( self.m_listArt, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( bSizer11, 1, wx.EXPAND, 5 )


		bSizer12.Add( bSizer9, 1, wx.EXPAND, 5 )

		self.m_button30 = wx.Button( self, wx.ID_ANY, u"尝试合并", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button30, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		# Connect Events
		self.m_button30.Bind( wx.EVT_BUTTON, self._OnConfirm )

		self._LoadGit()

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnConfirm( self, event ):
		event.Skip()
		artBranchStr, codeBranchStr = self.m_listArt.GetStringSelection(), self.m_listCode.GetStringSelection()
		self.HotFixBranch(artBranchStr, codeBranchStr)

	def _LoadGit(self):
		artGitPath, afcGitPath = utils.path.GetDesignAfcPath(), utils.path.GetCodeGitPath()
		if not os.path.exists(artGitPath) or not os.path.exists(afcGitPath):
			d = ErrorDialog(self)
			d.m_staticText6.SetLabel(u"请先在设置中设置路径")
			d.Show()
			return
		self.artGit = utils.Git(artGitPath)
		self.codeGit = utils.Git(afcGitPath)
		if not self.artGit.IsGitPath():
			d = ErrorDialog(self)
			d.m_staticText6.SetLabel(u"美术资源路径无效")
			d.Show()
			return
		if not self.codeGit.IsGitPath():
			d = ErrorDialog(self)
			d.m_staticText6.SetLabel(u"程序资源路径无效")
			d.Show()
			return

		current_branch, branches, stdout = self.artGit.GetBranches()
		for b in branches:
			self.m_listArt.Append(b)

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

