# -*- coding: utf-8 -*-

import _extend

import utils
import os
from ErrorDialog import ErrorDialog

class InitPanel(_extend.InitPanel):
	def __init__(self, parent):
		super(InitPanel, self).__init__(parent)

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