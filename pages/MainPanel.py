# -*- coding: utf-8 -*-

import _extend

class MainPanel(_extend.MainPanel):
	def __init__(self, parent):
		super(MainPanel, self).__init__(parent)

	def OnClickHotFix( self, event ):
		event.Skip()
		self.GetParent().ShowGitBranchPanel()

	def _OnClickSyncSvnToGit( self, event ):
		event.Skip()
		self.GetParent().ShowSvnToGitPanel()
