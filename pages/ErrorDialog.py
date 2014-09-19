# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class ErrorDialog
###########################################################################

class ErrorDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"错误", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.Size( 400,100 ), wx.ALIGN_CENTRE )
		self.m_staticText6.Wrap( -1 )
		bSizer8.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button29 = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer8 )
		self.Layout()
		bSizer8.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button29.Bind( wx.EVT_BUTTON, self._Close )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def _Close( self, event ):
		event.Skip()
		self.Destroy()


