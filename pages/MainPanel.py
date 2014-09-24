# -*- coding: utf-8 -*-

import _extend
import WebReleaseFrame

class MainPanel(_extend.MainPanel):
	def __init__(self, parent):
		super(MainPanel, self).__init__(parent)

	def _OnClickHotFix( self, event ):
		event.Skip()
		self.GetParent().ShowGitBranchPanel()

	def _OnClickSyncSvnToGit( self, event ):
		event.Skip()
		self.GetParent().ShowSvnToGitPanel()

	def _OnClickWebRelease( self, event):
		event.Skip()
		m = WebReleaseFrame.WebReleaseFrame(self)
		m.Show()
