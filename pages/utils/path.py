# -*- coding: utf-8 -*-

import os
import tempfile
import contextlib
import shutil

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

