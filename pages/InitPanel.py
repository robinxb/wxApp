# -*- coding: utf-8 -*-

import _extend

import utils
import os
import wx

class InitPanel(_extend.InitPanel):
	def __init__(self, parent):
		super(InitPanel, self).__init__(parent)

	def _OnConfirmBtnClick( self, event ):
		event.Skip()

		cur_path = utils.path.GetDesignAfcPath()
		if cur_path != None and cur_path != "" and os.path.exists(cur_path):
			tmpGit = utils.Git(cur_path)
			if tmpGit.IsGitPath():
				wx.MessageBox(u"你已经初始化过了: %s"%cur_path, u'错误', wx.OK | wx.ICON_ERROR)
				return

		if cur_path != None and cur_path != "" and not os.path.exists(cur_path):
			utils.path.SetDesignAfcPath(None)

		path = self.m_dirPicker1.GetPath()
		if not os.path.isabs(path):
			wx.MessageBox(u"路径名无效: %s"%path, u'错误', wx.OK | wx.ICON_ERROR)
			return

		git = utils.Git(path)
		if git.IsGitPath():
			wx.MessageBox(u"此路径已存在git,请选择另外的文件夹", u'错误', wx.OK | wx.ICON_ERROR)
			return

		ret = git.InitWithArtGit()
		if ret:
			utils.path.SetDesignAfcPath(path)