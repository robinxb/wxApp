# -*- coding: utf-8 -*-

import _extend

import utils
import os

class ConfigPanel(_extend.ConfigPanel):
	def __init__(self, parent):
		super(ConfigPanel, self).__init__(parent)

	def LoadConfig(self):
		artGitPath, afcGitPath, svnPath, builderIP = utils.path.GetDesignAfcPath(),\
							utils.path.GetCodeGitPath(),\
							utils.path.GetSVNPath(),\
							utils.path.GetBuilderIP()
		if artGitPath != None and os.path.exists(artGitPath):
			self.m_ArtPicker.SetPath(artGitPath)
		if afcGitPath != None and os.path.exists(afcGitPath):
			self.m_CodePicker.SetPath(afcGitPath)
		if svnPath != None and os.path.exists(svnPath):
			self.m_SVNPicker.SetPath(svnPath)
		if builderIP != None and builderIP != "":
			self.m_BuilderIP.SetValue(builderIP)

	def _OnSave(self, event):
		if not os.path.exists(self.m_ArtPicker.GetPath()):
			self.m_ArtPicker.SetPath("")
			return
		if not os.path.exists(self.m_CodePicker.GetPath()):
			self.m_CodePicker.SetPath("")
			return
		if not os.path.exists(self.m_SVNPicker.GetPath()):
			self.m_SVNPicker.SetPath("")
			return
		utils.path.SetDesignAfcPath(self.m_ArtPicker.GetPath())
		utils.path.SetCodeGitPath(self.m_CodePicker.GetPath())
		utils.path.SetSVNPath(self.m_SVNPicker.GetPath())
		utils.path.SetBuilderIP(self.m_BuilderIP.GetValue())

