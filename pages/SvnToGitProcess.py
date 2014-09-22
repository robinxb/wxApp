# -*- coding: utf-8 -*-

import _extend

class SvnToGitProcess(_extend.SvnToGitProcess):
	def __init__(self, parent):
		super(SvnToGitProcess, self).__init__(parent)
		self.m_Finished = False

	def OnTryClose( self, event ):
		if getattr(self, "m_Finished", False) == True:
			event.Skip()
		else:
			event.Veto()
