# -*- coding: utf-8 -*-

import os
import tempfile
import contextlib
import shutil

from appdirs import AppDirs
import shelve

def GetFullPath(filename, dirname = "." + os.sep):
	return os.path.normpath(os.path.join(dirname + os.sep, filename))

# ============
# HTTP Release
# ============
def GetHttpDir():
	return "E:\\project\\http_test"

# ============
#    Git
# ============

def GetGitPath():
	return 'E:\\project\\afc'

def GetHotFixBasePath():
	return "E:\\project\\design\\resource\\release_tool\\hotfix"

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

def GetDesignAfcPath():
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	path = None
	if shelf.has_key("afcDesignPath"):
		path = shelf["afcDesignPath"]
	shelf.close()
	return path

def SetDesignAfcPath(path):
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	shelf["afcDesignPath"] = path
	shelf.close()

def GetCodeGitPath():
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	path = None
	if shelf.has_key("afcGitPath"):
		path = shelf["afcGitPath"]
	shelf.close()
	return path

def SetCodeGitPath(path):
	globalConfig = GetUserDataLocatin("global")
	basedir = os.path.dirname(globalConfig)
	if not os.path.exists(basedir):
		os.makedirs(basedir)
	shelf = shelve.open(globalConfig)
	shelf["afcGitPath"] = path
	shelf.close()
