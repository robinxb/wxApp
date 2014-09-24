# -*- coding: utf-8 -*-

import _extend

import utils
import os
import requests
import wx

ProductsURL = "http://pm.ejoy.com/HD.html"
GetProductsURL = "http://pm.ejoy.com/admin/get_product"
PostURL = "http://pm2.ejoy.com/admin/update_branch"
GetBranchDetailURL = "http://pm.ejoy.com/admin/get_branch"

class branchDetail(object):
	def __init__(self):
		super(branchDetail, self).__init__()
		self.name = None #str
		self.update_time = None #int
		self.version_for_web = None #str
		self.branchid = None #str
		self.type = None #str
		self.app_name = None #str (ios only)
		self.bundle_id = None #str (ios only)
		self.create_time = None #int
		self.desc = None #str

		#非网页显示信息
		self.server_ip = None
		self.server_name = None
		self.version1 = None
		self.version2 = None
		self.version3 = None

	def FeedWithHtml(self, rawhtml):
		pass

class WebReleaseFrame(_extend.WebReleaseFrame):
	def __init__(self, parent):
		super(WebReleaseFrame, self).__init__(parent)
		self._fetchAll()
		self._loadAll()

	def _fetchAll(self):
		self.branches = []
		s = requests.post(GetProductsURL, data = {'product': "HD"})
		d = s.json()[u"data"][u"branchs"]
		for branch in d:
			bid = branch[u'id']
			r = requests.post(GetBranchDetailURL, {'branch_id': bid})
			j = r.json()['data']
			bObject = branchDetail()
			bObject.name = j[u'name']
			bObject.update_time = j[u'update_time']
			bObject.create_time = j[u'create_time']
			bObject.branchid = j[u'id']
			bObject.version_for_web = j[u'version']
			bObject.desc = j[u'desc']
			ptype = j[u'package_type']
			bObject.type = ptype
			if ptype == 'ios':
				bObject.bundle_id = j[u'spec_items'][u'bundle_id']
				bObject.app_name = j[u'spec_items'][u'app_name']
			self.branches.append(bObject)

	def _loadAll(self):
		# self.m_ItemType.InsertChoice("ios", 1)
		for obj in self.branches:
			self.m_BranchList.Append(obj.name)

		artGitPath, afcGitPath = utils.path.GetDesignAfcPath(), utils.path.GetCodeGitPath()
		if not os.path.exists(artGitPath) or not os.path.exists(afcGitPath):
			wx.MessageBox(u"请先在设置中设置路径", u'错误', wx.OK | wx.ICON_INFORMATION)
			return
		self.artGit = utils.Git(artGitPath)
		self.codeGit = utils.Git(afcGitPath)
		if not self.artGit.IsGitPath():
			wx.MessageBox(u"美术资源路径无效", u'错误', wx.OK | wx.ICON_ERROR)
			return
		if not self.codeGit.IsGitPath():
			wx.MessageBox(u"程序资源路径无效", u'错误', wx.OK | wx.ICON_ERROR)
			return

		self.m_ArtBranch.Clear()
		current_branch, branches, stdout = self.artGit.GetBranches()
		for b in branches:
			self.m_ArtBranch.Append(b)

		self.m_CodeBranch.Clear()
		current_branch, branches, stdout = self.codeGit.GetBranches()
		for b in branches:
			self.m_CodeBranch.Append(b)

	def _OnSelectItem( self, event ):
		event.Skip()
		selectId = self.m_BranchList.GetSelection()
		if selectId == wx.NOT_FOUND:
			return
		obj = self.branches[selectId]
		self.m_ItemBranchName.SetValue(obj.name)
		self.m_ItemDesc.SetValue(obj.desc)
		bIsIOS = obj.type == 'ios'
		self.m_ItemIsIos.SetValue(bIsIOS)
		if bIsIOS:
			self.m_ItemAppName.SetValue(obj.app_name)
			self.m_ItemBundleID.SetValue(obj.bundle_id)

		# self.m_ItemType.EditEnumProperty("EditEnum", "EditEnumProperty", ['A', 'B', 'C'], [0, 1, 2], "Text Not in List")
		# self.m_ItemType.SetChoices(obj.type)
		# print self.m_ItemType.GetChoices()
