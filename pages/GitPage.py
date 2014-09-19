# -*- coding: utf-8 -*-

import wx
import wx.xrc
import utils


class GitBranchPanel ( wx.Panel ):

    def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

		self.gitBranchSizer = wx.BoxSizer( wx.VERTICAL )

		self._LoadGit()

		self.SetSizer( self.gitBranchSizer )
		self.Layout()

    def __del__( self ):
        pass

    def _LoadGit(self):
        self.git = utils.Git()
        current_branch, banches, stdout = self.git.GetBranches()

        self.gitBranchSizer = wx.BoxSizer(wx.VERTICAL)
        self.m_Title = wx.StaticText( self, wx.ID_ANY, u"请选择要发布的分支", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_Title.Wrap( -1 )
        self.gitBranchSizer.Add( self.m_Title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        for b in banches:
            btn = wx.Button( self, wx.ID_ANY, b, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.gitBranchSizer.Add(btn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
            self.Bind(wx.EVT_BUTTON, lambda event, branch=b: self.OnClickBranchBtn(event, branch), btn)

        self.SetSizer( self.gitBranchSizer )
        self.Layout()

    def OnClickBranchBtn(self, event, branch):
    	self._cb(branch)

    def SetClickFunc(self, cb):
    	self._cb = cb

    def HotFixBranch(self, branchStr):
    	# checkout to this branch
    	branch = branchStr.split("/")[-1]
    	self.git.Checkout(branch)

    	# get current version
    	cur_script_version, cur_major_version = utils.cfg.GetVersion(branch)

    	# prepare for generate hotfix files
    	with utils.path.GetNewTempDir() as temp_dir:
    		print("*** Generate HotFix file in --> %s \n"%temp_dir)

