# -*- coding: utf-8 -*-

import _extend

import utils
import os

class SvnToGitPanel(_extend.SvnToGitPanel):
	def __init__(self, parent):
		super(SvnToGitPanel, self).__init__(parent)

	def LoadPath(self):
		artPath = utils.path.GetDesignAfcPath()
		if artPath and os.path.exists(artPath):
			self.afcGit = utils.Git(artPath)
			assert(self.afcGit.IsGitPath())
			current_branch, branches, stdout = self.afcGit.GetBranches()
			for b in branches:
				self.m_ArtBranchList.Append(b)
		svnPath = utils.path.GetSVNPath()
		if svnPath and os.path.exists(svnPath):
			self.m_ArtPicker.SetPath(svnPath)

	# Virtual event handlers, overide them in your derived class
	def _OnClickConfirm( self, event ):
		event.Skip()
