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
	sshin, sshout, ssherr = sshobj.exec_command('cd ~/project/branch && python cfg.py -c %s --art %s --code %s -t %s'%(data["name"], data["artBranch"], data["codeBranch"], data["package_type"]))
	output = sshout.read().strip() + ssherr.read().strip()
	if "Fatal" in output:
		print output
		return False
	print output
	print ssherr.read()

	info = json.loads(output)

	print '===== Ask builder to create branch on pm.ejoy.com ====='
	if data["package_type"] == "ios":
		cmd = "cd ~/project/branch && python upload.py create %s %s %s %s %s %s %s"%(data["name"], data["version"], data["desc"], data["package_type"], info["uuid"], data["app_name"], data["bundle_id"])
	else:
		cmd = "cd ~/project/branch && python upload.py create %s %s %s %s %s"%(data["name"], data["version"], data["desc"], data["package_type"], info["uuid"])

	sshin, sshout, ssherr = sshobj.exec_command(cmd)
	output = sshout.read().strip() + ssherr.read().strip()
	print(output)
	if not "CREATE_SUCCESS" in output:
		return False

	return True

def Build(sshobj, uuid, no_output = False):
	print '===== Build IPA ====='
	(sshin1, sshout1, ssherr) = sshobj.exec_command('cd ~/project/branch && python build.py %s'%(uuid))
	build_success = False
	hash_success = False
	if not no_output:
		while True:
			line = sshout1.readline()
			if line != '':
				out = line.rstrip('\n')
				print(out)
				if "BUILDER_IPA_SUCCESS" in out:
					build_success = True
				if "MD5_GENERATE_SUCCESS" in out:
					hash_success = True
			else:
				break
		if not build_success or not hash_success:
			print '===== Build Fail, Please Check The Error ====='
			print ssherr.read()
			return False
	else:
		sshout1.read()
	return True

def Upload(sshobj, uuid, pathOnRemote):
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
		self.code_branch = None
		self.art_branch = None

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

	def __del__(self):
		self.ssh.close()
		print '===== SSH close ====='

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
					bObject.code_branch = info['codeBranch']
					bObject.art_branch = info['artBranch']
					bObject.version1, bObject.version2, bObject.version3 = info['version'].split('.')
					self.branches.append(bObject)
					self.m_BranchList.Append(bObject.name)

	def _loadAll(self):
		self.m_ArtBranch.Clear()
		self.m_CodeBranch.Clear()

		current_branch, branches, stdout = utils.helper.GetArtGitBranchs(self.ssh)
		for b in branches:
			self.m_ArtBranch.Append(b)

		current_branch, branches, stdout = utils.helper.GetCodeGitBranchs(self.ssh)
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
		self.m_ItemVersion1.SetValue(int(obj.version1))
		self.m_ItemVersion2.SetValue(int(obj.version2))
		self.m_ItemVersion3.SetValue(int(obj.version3))
		bIsIOS = obj.type == 'ios'
		self.m_ItemIsIos.SetValue(bIsIOS)
		if bIsIOS:
			self.m_ItemAppName.SetValue(obj.app_name)
			self.m_ItemBundleID.SetValue(obj.bundle_id)
		idx = self.m_ArtBranch.FindString(obj.art_branch)
		if not idx == wx.NOT_FOUND:
			self.m_ArtBranch.SetSelection(idx)
		idx = self.m_CodeBranch.FindString(obj.code_branch)
		if not idx == wx.NOT_FOUND:
			self.m_CodeBranch.SetSelection(idx)


	def _OnClickRefresh( self, event ):
		event.Skip()
		self._fetchAll()

	def _OnClickExecute( self, event):
		event.Skip()

		artBranch, codeBranch = self.m_ArtBranch.GetStringSelection(), self.m_CodeBranch.GetStringSelection()
		print '===== Make ipa for CodeBranch: %s and ArtBranch: %s'%(codeBranch, artBranch)

		selectId = self.m_BranchList.GetSelection()
		if selectId == wx.NOT_FOUND:
			return
		obj = self.branches[selectId]
		success, info = GetBranchInfo(self.ssh, obj.uuid)

		if not success:
			print '===== Branch %s NOT FOUND on remote ====='%(obj.name)
			return
		if Build(self.ssh, obj.uuid, obj.type == 'android'):
			if obj.type == 'ios':
				Upload(self.ssh, obj.uuid , "~/project/aegean/client/archive/momo_release_id.ipa")
			else:
				Upload(self.ssh, obj.uuid , "~/project/aegean/client/archive/farm_momo.apk")

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
