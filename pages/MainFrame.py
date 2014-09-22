# -*- coding: utf-8 -*-

from _extend import MainFrame
import MainPanel
import InitPanel
import ConfigPanel
import SvnToGitPanel
import GitBranchPanel

class MainFrame(MainFrame):
	def __init__(self, parent = None):
		super(MainFrame, self).__init__(parent)
		self.m_Panels = {}

		self.m_Panels["MainPanel"] = MainPanel.MainPanel(self)
		self.m_Panels["InitPanel"] = InitPanel.InitPanel(self)
		self.m_Panels["ConfigPanel"] = ConfigPanel.ConfigPanel(self)
		self.m_Panels["SvnToGitPanel"] = SvnToGitPanel.SvnToGitPanel(self)
		self.m_Panels["GitBranchPanel"] = GitBranchPanel.GitBranchPanel(self)

		self.HideAll()
		self.m_Panels["MainPanel"].Show()
		self.Fit()

	def ShowMainPanel( self, event ):
		event.Skip()
		self.HideAll()
		self.m_Panels["MainPanel"].Show()
		self.Fit()

	def ShowInitPanel( self, event ):
		event.Skip()
		self.HideAll()
		self.m_Panels["InitPanel"].Show()
		self.Fit()

	def ShowConfigPanel( self, event ):
		event.Skip()
		self.HideAll()
		self.m_Panels["ConfigPanel"].Show()
		self.m_Panels["ConfigPanel"].LoadConfig()
		self.Fit()

	# Custom Functions Start

	def HideAll(self):
		for v in self.m_Panels.values():
			v.Hide()

	def ShowGitBranchPanel(self):
		self.HideAll()
		self.m_Panels["GitBranchPanel"].Show()
		self.m_Panels["GitBranchPanel"].LoadGit()
		self.Fit()

	def ShowSvnToGitPanel(self):
		self.HideAll()
		self.m_Panels["SvnToGitPanel"].Show()
		self.m_Panels["SvnToGitPanel"].LoadPath()
		self.Fit()
