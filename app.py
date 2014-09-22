# -*- coding: utf-8 -*-

import pages
import wx

app = wx.App(False)

frame = pages.MainFrame(None)
frame.Show(True)
app.MainLoop()