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

		cur_path = utils.path.GetDesignAfcPath()
		if cur_path != None and cur_path != "" and os.path.exists(cur_path):
			tmpGit = utils.Git(cur_path)
			if tmpGit.IsGitPath():
				d = ErrorDialog(self)
				d.m_staticText6.SetLabel(u"你已经初始化过了: %s"%cur_path)
				d.Show()
				return

		if cur_path != None and cur_path != "" and not os.path.exists(cur_path):
			utils.path.SetDesignAfcPath(None)

		path = self.m_dirPicker1.GetPath()
		if not os.path.isabs(path):
			d = ErrorDialog(self)
			d.m_staticText6.SetLabel(u"路径名无效: %s"%path)
			d.Show()
			return

		git = utils.Git(path)
		if git.IsGitPath():
			d = ErrorDialog(self)
			d.m_staticText6.SetLabel(u"此路径已存在git,请选择另外的文件夹")
			d.Show()
			return

		ret = git.InitWithArtGit()
		if ret:
			utils.path.SetDesignAfcPath(path)
