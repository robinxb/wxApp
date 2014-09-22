# -*- coding: utf-8 -*-

import os
import tempfile
import contextlib
import shutil

from appdirs import AppDirs
import shelve

def GetFullPath(filename, dirname = "." + os.sep):
	return os.path.normpath(os.path.join(dirname + os.sep, filename))

@contextlib.contextmanager
def GetNewTempDir():
	temp_dir = tempfile.mkdtemp()
	yield temp_dir
	shutil.rmtree(temp_dir)

def GetUserDataLocatin(filename = None):
	if filename and filename != "" :
		return AppDirs("AegeanTool", "Ejoy").user_data_dir + os.sep + filename
	else:
		return AppDirs("AegeanTool", "Ejoy").user_data_dir

def _GetLocalCfg(key):
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	var = None
	if shelf.has_key(key):
		var = shelf[key]
	shelf.close()
	return var

def _SetLocalCfg(key, val):
	assert(type(key) == unicode or type(key) == str)
	assert(type(val) == unicode or type(val) == str)
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	shelf[key] = val
	shelf.close()

def GetDesignAfcPath():
	return _GetLocalCfg("afcDesignPath")

def SetDesignAfcPath(path):
	return _SetLocalCfg("afcDesignPath", path)

def GetCodeGitPath():
	return _GetLocalCfg("afcGitPath")

def SetCodeGitPath(path):
	return _SetLocalCfg("afcGitPath", path)

def GetSVNPath():
	return _GetLocalCfg("SVNPath")

def SetSVNPath(path):
	return _SetLocalCfg("SVNPath", path)

def GetBuilderIP():
	return _GetLocalCfg("BuilderIP")

def SetBuilderIP(ip):
	return _SetLocalCfg("BuilderIP", ip)
