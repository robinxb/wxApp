# -*- coding: utf-8 -*-

import _extend

import utils
import os
import requests
import wx
import pysftp
import paramiko
import json

ProductsURL = "http://pm.ejoy.com/HD.html"
GetProductsURL = "http://pm.ejoy.com/admin/get_product"
PostURL = "http://pm2.ejoy.com/admin/update_branch"
GetBranchDetailURL = "http://pm.ejoy.com/admin/get_branch"

def GetBranchInfo(sshobj, uuid):
	sshin, sshout, ssherr = sshobj.exec_command('cd ~/project/branch && python cfg.py -l %s'%uuid)
	success = False
	js_str = ""
	while True:
		line = sshout.readline()
		if line != "":
			out = line.rstrip('\n')
			js_str = js_str + out
			if "404" in out:
				break
		else:
			success = True
			break
	if success:
		return success, json.loads(js_str)
	else:
		return success, js_str

def CreateBranch(sshobj, data):
	print '===== Create cfg on builder ====='
	sshin, sshout, ssherr = sshobj.exec_command('cd ~/project/branch && python cfg.py -c %s --art %s --code %s'%(data["name"], data["artBranch"], data["codeBranch"]))
	output = sshout.read().strip() + ssherr.read().strip()
	if "Fatal" in output:
		print output
		return False

	info = json.loads(output)

	print '===== Ask builder to create branch on pm.ejoy.com ====='
	cmd = "cd ~/project/branch && python upload.py create %s %s %s %s %s %s %s"%(data["name"], data["version"], data["desc"], data["package_type"], data["app_name"], data["bundle_id"], info["uuid"])
	sshin, sshout, ssherr = sshobj.exec_command(cmd)
	output = sshout.read().strip() + ssherr.read().strip()
	print(output)
	if not "CREATE_SUCCESS" in output:
		return False

	return True

def BuildIPA(sshobj, codeBranch, artBranch):
	print '===== Build IPA ====='
	(sshin1, sshout1, ssherr) = sshobj.exec_command('cd ~/project && ./build.sh %s %s %s %s'%(codeBranch, artBranch))
	success = False
	while True:
		line = sshout1.readline()
		if line != '':
			out = line.rstrip('\n')
			print(out)
			if "BUILDER_IPA_SUCCESS" in out:
				success = True
		else:
			break
	if not success:
		print '===== Build Fail, Please Check The Error ====='
		return False
	return True

def UploadIPA(sshobj, uuid, pathOnRemote):
	print '===== Update IPA to pm.ejoy.com ====='

	(sshin1, sshout1, ssherr) = sshobj.exec_command('cd ~/project/branch && python upload.py update %s %s '%(uuid, pathOnRemote))
	success = False
	while True:
		line = sshout1.readline()
		if line != '':
			out = line.rstrip('\n')
			print(out)
			if "UPLOAD_SUCCESS" in out:
				success = True
		else:
			break
	if not success:
		print '===== Upload IPA Fail, Please Check The Error ====='
	return success


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

class WebReleaseFrame(_extend.WebReleaseFrame):
	def __init__(self, parent):
		super(WebReleaseFrame, self).__init__(parent)
		ip = utils.path.GetBuilderIP()
		self.ssh = paramiko.SSHClient()
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		conn = self.ssh.connect(ip, username = 'farmbuilder', password = "farm")
		print '===== SSH connected to %s ====='%(ip)
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
			bObject.uuid= j[u'version'] #暂时用来存uuid
			bObject.desc= j[u'desc']
			ptype = j[u'package_type']
			bObject.type = ptype
			if ptype == 'ios':
				bObject.bundle_id = j[u'spec_items'][u'bundle_id']
				bObject.app_name = j[u'spec_items'][u'app_name']

			if bObject.uuid:
				success, info = GetBranchInfo(self.ssh, bObject.uuid)
				print(success, info)
				if success:
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

	def _OnClickExecute( self, event):
		event.Skip()


		print '===== Make ipd for CodeBranch: %s and ArtBranch: %s'%(codeBranch, artBranch)

		selectId = self.m_BranchList.GetSelection()
		if selectId == wx.NOT_FOUND:
			return
		obj = self.branches[selectId]
		branch_name = obj.name
		success, info = GetBranchInfo(self.ssh, branch_name)

		if not success:
			print '===== Branch %s NOT FOUND on remote, try to create one ====='%(branch_name)

	def _OnClickAddButton( self, event):
		# "branch_name": data.name,
		# "version": data.version,
		# "desc": data.desc,
		# "package_type": data.package_type,
		# "app_name": data.app_name,
		# "bundle_id": data.bundle_id
		# data.artBranch
		# data.codeBranch
		event.Skip()
		bIsIOS = self.m_ItemIsIos.GetValue() == True
		artBranch, codeBranch = self.m_ArtBranch.GetStringSelection(), self.m_CodeBranch.GetStringSelection()
		artBranch = artBranch.split("/")[-1]
		codeBranch = codeBranch.split("/")[-1]
		data = {
		"name": self.m_ItemBranchName.GetValue(),
		"version": ".".join([
			str(self.m_ItemVersion1.GetValue()),
			str(self.m_ItemVersion2.GetValue()),
			str(self.m_ItemVersion3.GetValue())
		]),
		"desc": self.m_ItemDesc.GetValue(),
		"package_type":  bIsIOS and "ios" or "android",
		"artBranch": artBranch,
		"codeBranch": codeBranch,
		}
		if bIsIOS:
			data["bundle_id"] = self.m_ItemBundleID.GetValue()
			data["app_name"] = self.m_ItemAppName.GetValue()

		if not CreateBranch(self.ssh, data):
			return
