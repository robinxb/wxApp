# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import pages

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"爱琴海综合工具", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu4 = wx.Menu()
		self.m_menuItemInitDesignGit = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"初始化", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItemInitDesignGit )

		self.m_menubar2.Append( self.m_menu4, u"操作" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )
		self.Show()

		# Connect Events
		self.Bind( wx.EVT_MENU, self.ShowInitPanel, id = self.m_menuItemInitDesignGit.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ShowInitPanel( self, event ):
		event.Skip()
		self.app.ShowInitPanel()


class AFC_APP (wx.App):
	def __init__(self, parent = False):
		wx.App.__init__(self, parent)
		self.mainFrame = MainFrame(None)
		self.mainFrame.app = self

	def __del__(self):
		wx.App.__del__(self)

	def HideAllPanel(self):
		for s in ("MainPanel","GitBranchPanel"):
			p = getattr(self, s, None)
			if p:
				p.Hide()

	def ShowMainFrame(self):
		self.HideAllPanel()
		if hasattr(self, "MainPanel"):
			self.MainPanel.Show()
		else:
			panel = pages.MainPanel(self.mainFrame)
			panel.SetHotfixCB(self._OnClickHotFix)
			self.MainPanel = panel

	def ShowGitBranches(self):
		self.HideAllPanel()
		self.GitBranchPanel = pages.GitBranchPanel(self.mainFrame)
		self.GitBranchPanel.SetClickFunc(self._OnClickBranch)

	def ShowInitPanel(self):
		self.HideAllPanel()
		self.InitPanel = pages.InitPanel(self.mainFrame)

	#function for buttons
	def _OnClickBranch(self, branchString):
		self.GitBranchPanel.HotFixBranch(branchString)

	def _OnClickHotFix(self):
		self.ShowGitBranches()


if __name__ == "__main__":
	mainApp = AFC_APP()
	mainApp.ShowMainFrame()
	mainApp.MainLoop()

