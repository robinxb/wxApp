# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_btnClientHotFix = wx.Button( self, wx.ID_ANY, u"客户端热更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_btnClientHotFix, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_btnNewBranch = wx.Button( self, wx.ID_ANY, u"同步当前SVN至制定美术分支", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_btnNewBranch, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		# Connect Events
		self.m_btnClientHotFix.Bind( wx.EVT_BUTTON, self.OnClickHotFix )
		self.m_btnNewBranch.Bind( wx.EVT_BUTTON, self._OnClickSyncSvnToGit )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClickHotFix( self, event ):
		event.Skip()
		self.OnClickHotFixFunction()

	def SetHotfixCB(self, cb):
		self.OnClickHotFixFunction = cb

	def _OnClickSyncSvnToGit(self, event):
		self.OnClickSyncSvnToGitFunction()

	def SetSyncSvnToGitFunction(self, cb):
		self.OnClickSyncSvnToGitFunction = cb
