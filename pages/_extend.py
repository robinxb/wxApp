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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"爱琴海综合工具", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar2 = wx.MenuBar( 0 )
		self.m_menu4 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"主界面", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem2 )

		self.m_menu4.AppendSeparator()

		self.m_menuItemInitDesignGit = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"初始化", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItemInitDesignGit )

		self.m_menuItem3 = wx.MenuItem( self.m_menu4, wx.ID_ANY, u"设置", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu4.AppendItem( self.m_menuItem3 )

		self.m_menubar2.Append( self.m_menu4, u"操作" )

		self.SetMenuBar( self.m_menubar2 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.ShowMainPanel, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.ShowInitPanel, id = self.m_menuItemInitDesignGit.GetId() )
		self.Bind( wx.EVT_MENU, self.ShowConfigPanel, id = self.m_menuItem3.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ShowMainPanel( self, event ):
		event.Skip()

	def ShowInitPanel( self, event ):
		event.Skip()

	def ShowConfigPanel( self, event ):
		event.Skip()


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

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnConfirm( self, event ):
		event.Skip()


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

	def _OnClickSyncSvnToGit( self, event ):
		event.Skip()


###########################################################################
## Class SvnToGitPanel
###########################################################################

class SvnToGitPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText16 = wx.StaticText( self, wx.ID_ANY, u"SVN美术目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		bSizer24.Add( self.m_staticText16, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_ArtPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer24.Add( self.m_ArtPicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer24, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"选择美术分支", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		bSizer25.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		m_ArtBranchListChoices = []
		self.m_ArtBranchList = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ArtBranchListChoices, 0 )
		bSizer25.Add( self.m_ArtBranchList, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		bSizer23.Add( bSizer25, 1, wx.EXPAND, 5 )

		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"将SVN的美术资源同步至Git", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_button37, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer23.Add( bSizer26, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer23 )
		self.Layout()

		# Connect Events
		self.m_button37.Bind( wx.EVT_BUTTON, self._OnClickConfirm )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnClickConfirm( self, event ):
		event.Skip()


###########################################################################
## Class InitPanel
###########################################################################

class InitPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Step1: 请选择待存放美术资源的目录(Git)(路径不能有中文)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer7.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"请选择文件夹", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer7.Add( self.m_dirPicker1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Step2: 点击按钮", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button26 = wx.Button( self, wx.ID_ANY, u"点我从服务器获取美术资源", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_button26, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		# Connect Events
		self.m_button26.Bind( wx.EVT_BUTTON, self._OnConfirmBtnClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnConfirmBtnClick( self, event ):
		event.Skip()


###########################################################################
## Class ErrorDialog
###########################################################################

class ErrorDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 400,100 ), wx.ALIGN_CENTRE )
		self.m_staticText6.Wrap( -1 )
		bSizer8.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button29.Bind( wx.EVT_BUTTON, self._Close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _Close( self, event ):
		event.Skip()


###########################################################################
## Class ConfigPanel
###########################################################################

class ConfigPanel ( wx.Panel ):

	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"美术资源路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer15.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_ArtPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer15.Add( self.m_ArtPicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"程序资源路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer16.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_CodePicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer16.Add( self.m_CodePicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( bSizer16, 1, wx.EXPAND, 5 )

		bSizer162 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText101 = wx.StaticText( self, wx.ID_ANY, u"SVN资源路径", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )
		bSizer162.Add( self.m_staticText101, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )

		self.m_SVNPicker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer162.Add( self.m_SVNPicker, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( bSizer162, 1, wx.EXPAND, 5 )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_button35 = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_button35, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer14.Add( bSizer161, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer14 )
		self.Layout()

		# Connect Events
		self.m_button35.Bind( wx.EVT_BUTTON, self._OnSave )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnSave( self, event ):
		event.Skip()


