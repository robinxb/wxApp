# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

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

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"美术使用" ), wx.VERTICAL )

		self.m_btnNewBranch = wx.Button( self, wx.ID_ANY, u"同步当前SVN至制定美术分支", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_btnNewBranch, 0, wx.ALIGN_CENTER|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer22.Add( sbSizer1, 1, wx.EXPAND, 5 )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"程序使用" ), wx.VERTICAL )

		self.m_btnClientHotFix = wx.Button( self, wx.ID_ANY, u"客户端热更新", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_btnClientHotFix, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"网页分支发布设置", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.m_button7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer22.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		# Connect Events
		self.m_btnNewBranch.Bind( wx.EVT_BUTTON, self._OnClickSyncSvnToGit )
		self.m_btnClientHotFix.Bind( wx.EVT_BUTTON, self._OnClickHotFix )
		self.m_button7.Bind( wx.EVT_BUTTON, self._OnClickWebRelease )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnClickSyncSvnToGit( self, event ):
		event.Skip()

	def _OnClickHotFix( self, event ):
		event.Skip()

	def _OnClickWebRelease( self, event ):
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
## Class SvnToGitProcess
###########################################################################

class SvnToGitProcess ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"请等待", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_StepDesc = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_StepDesc.Wrap( -1 )
		bSizer20.Add( self.m_StepDesc, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 300,-1 ), wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer20.Add( self.m_gauge1, 0, wx.ALL, 5 )

		self.m_Text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,300 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer20.Add( self.m_Text, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()
		bSizer20.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnTryClose )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnTryClose( self, event ):
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

		bSizer1611 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"BuilderIP地址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer1611.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_BuilderIP = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		bSizer1611.Add( self.m_BuilderIP, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer14.Add( bSizer1611, 1, wx.EXPAND, 5 )

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


###########################################################################
## Class WebReleaseFrame
###########################################################################

class WebReleaseFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"分支发布页面", pos = wx.DefaultPosition, size = wx.Size( 500,700 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )

		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Step1: 选择或创建分支" ), wx.HORIZONTAL )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		m_BranchListChoices = []
		self.m_BranchList = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_BranchListChoices, 0 )
		bSizer26.Add( self.m_BranchList, 0, wx.ALL, 5 )

		self.m_AddButton = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.m_AddButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		sbSizer13.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_propertyGrid2 = pg.PropertyGrid(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_DEFAULT_STYLE|wx.propgrid.PG_SPLITTER_AUTO_CENTER)
		self.m_propertyGrid2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		self.m_propertyGridItem11 = self.m_propertyGrid2.Append( pg.PropertyCategory( u"Web分支设置", u"Web分支设置" ) )
		self.m_ItemBranchName = self.m_propertyGrid2.Append( pg.StringProperty( u"分支名", u"分支名" ) )
		self.m_ItemDesc = self.m_propertyGrid2.Append( pg.StringProperty( u"Desc", u"Desc" ) )
		self.m_ItemIsIos = self.m_propertyGrid2.Append( pg.BoolProperty( u"iOS分支", u"iOS分支" ) )
		self.m_ItemAppName = self.m_propertyGrid2.Append( pg.StringProperty( u"(iOS)app_name", u"(iOS)app_name" ) )
		self.m_ItemBundleID = self.m_propertyGrid2.Append( pg.StringProperty( u"(iOS)bundle_id", u"(iOS)bundle_id" ) )
		self.m_propertyGridItem10 = self.m_propertyGrid2.Append( pg.PropertyCategory( u"服务器设置", u"服务器设置" ) )
		self.m_ItemServerName = self.m_propertyGrid2.Append( pg.StringProperty( u"服务器名字", u"服务器名字" ) )
		self.m_ItemServerIP = self.m_propertyGrid2.Append( pg.StringProperty( u"服务器IP", u"服务器IP" ) )
		self.m_ItemVersion1 = self.m_propertyGrid2.Append( pg.IntProperty( u"主版本号", u"主版本号" ) )
		self.m_ItemVersion2 = self.m_propertyGrid2.Append( pg.IntProperty( u"子版本号", u"子版本号" ) )
		self.m_ItemVersion3 = self.m_propertyGrid2.Append( pg.IntProperty( u"修订版本号", u"修订版本号" ) )
		bSizer25.Add( self.m_propertyGrid2, 1, wx.ALL|wx.EXPAND, 5 )


		sbSizer13.Add( bSizer25, 1, wx.EXPAND, 5 )


		bSizer24.Add( sbSizer13, 1, wx.EXPAND, 5 )

		sbSizer14 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Step2: 选择美术与程序分支" ), wx.HORIZONTAL )

		sbSizer16 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"美术分支" ), wx.VERTICAL )

		m_ArtBranchChoices = []
		self.m_ArtBranch = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ArtBranchChoices, 0 )
		sbSizer16.Add( self.m_ArtBranch, 0, wx.ALL, 5 )


		sbSizer14.Add( sbSizer16, 1, wx.EXPAND, 5 )

		sbSizer17 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"程序分支" ), wx.VERTICAL )

		m_CodeBranchChoices = []
		self.m_CodeBranch = wx.ListBox( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_CodeBranchChoices, 0 )
		sbSizer17.Add( self.m_CodeBranch, 0, wx.ALL, 5 )


		sbSizer14.Add( sbSizer17, 1, wx.EXPAND, 5 )


		bSizer24.Add( sbSizer14, 1, wx.EXPAND, 5 )

		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Step3: 执行" ), wx.VERTICAL )

		self.m_ExecuteButton = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer15.Add( self.m_ExecuteButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer24.Add( sbSizer15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer24 )
		self.m_scrolledWindow1.Layout()
		bSizer24.Fit( self.m_scrolledWindow1 )
		bSizer22.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_BranchList.Bind( wx.EVT_LISTBOX, self._OnSelectItem )
		self.m_AddButton.Bind( wx.EVT_BUTTON, self._OnClickAddButton )
		self.m_ExecuteButton.Bind( wx.EVT_BUTTON, self._OnClickExecute )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _OnSelectItem( self, event ):
		event.Skip()

	def _OnClickAddButton( self, event ):
		event.Skip()

	def _OnClickExecute( self, event ):
		event.Skip()


