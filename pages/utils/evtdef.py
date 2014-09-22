import wx

myEVT_COPY_COUNT = wx.NewEventType()
myEVT_COPY_END = wx.NewEventType()

EVT_COPY_COUNT = wx.PyEventBinder(myEVT_COPY_COUNT, 1)
EVT_COPY_END = wx.PyEventBinder(myEVT_COPY_END, 1)
class EventCopyCount(wx.PyCommandEvent):
	def __init__(self, etype, eid, copied, destFile, fileCount):
		wx.PyCommandEvent.__init__(self, etype, eid)
		self._copied = copied
		self._destFile = destFile
		self._fileCount = fileCount

	def GetCopied(self):
		return self._copied

	def GetDestFile(self):
		return self._destFile

	def GetFileCount(self):
		return self._fileCount

class EventCopyEnd(wx.PyCommandEvent):
	def __init__(self, etype, eid, total):
		wx.PyCommandEvent.__init__(self, etype, eid)
		self._total = total

	def GetTotal(self):
		return self._total
