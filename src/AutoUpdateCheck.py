# -*- coding: utf-8 -*-

from Components.config import config
from Tools.Notifications import AddPopup
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen

from socket import timeout
from twisted.web.client import getPage
from Tools.BoundFunction import boundFunction

from GithubPluginUpdater import reload_value, githuburls, pluginnames, lastgithubcommits, githubcommiturls, search_strings, filenames

import GithubPluginUpdater
import os

session = None
getPageCounter = 0
getContentCounter = 0
UpdateExist = False
UpdatePluginnames = ""


def loadPages(gpu_session):
			
			global githuburls
			global githubcommiturls
			global getPageCounter
			global session
			global UpdatePluginnames
			global getContentCounter
			
			session = gpu_session
			
			getContentCounter = 0
			getPageCounter = 0
			UpdateExist = False
			UpdatePluginnames = ""
			
			getPageCounter = 0

			for i in range(len(githubcommiturls)-1):
				
				if os.path.isfile(filenames[i]) and config.plugins.githubpluginupdater.update_check[pluginnames[i]].value:
					getPageCounter +=1
					deferred = getPage(githubcommiturls[i], timeout=10)
					deferred.addCallback(getLastCommit, i+1)
					deferred.addErrback(errorHandler, i+1)
			
			#check for GithubPluginUpdater
			if config.plugins.githubpluginupdater.update_check[pluginnames[4]].value:
				getPageCounter +=1
				deferred = getPage(githuburls[4], timeout=10)
				deferred.addCallback(getLastCommit, 5)
				deferred.addErrback(errorHandler, 5)

def errorHandler(result, number):
			
			global getContentCounter
			global getPageCounter
			
			getContentCounter += 1
			if getContentCounter == getPageCounter:
				getUpdateInfoMessage(MessageBox.TYPE_ERROR)


def getGPUVersion(content):

			gpu_version=""
			search_string = "VERSION = "
			pos1 = content.find(search_string)
			if pos1 > 0:
				pos2 = content.find("\n",pos1+len(search_string))
				gpu_version = str(content[pos1:pos2])
				gpu_version = gpu_version.replace(search_string,"")
				gpu_version = gpu_version.replace('"',"")
			return gpu_version

def checkGPUVersion(local_version, github_version):
			
			github_version_split = github_version.split(".")
			github_version_split = map(lambda x: int(x), github_version_split)
			if " beta" in local_version:
				local_version_split = local_version.split(" ")[0].split(".")
				local_version_split = map(lambda x: int(x), local_version_split)
				#set higher github-Version at beta
				local_version_split.append(0)
				github_version_split.append(1)
			else:
				local_version_split = local_version.split(".")
				local_version_split = map(lambda x: int(x), local_version_split)
			
			if (github_version_split > local_version_split):
				return True
			
			return False

def getLastCommit(contents, number):
			
			try:

				global getContentCounter
				global getPageCounter
				global UpdateExist
				global lastgithubcommits
				global session
				global UpdatePluginnames
			
				getContentCounter += 1
				
				#== check Update for GithubPluginUpdater
				if number == 5:
					f = open(filenames[number-1], 'r')
					plugin_txt = f.read()
					f.close()
					local_version = getGPUVersion(plugin_txt)
					github_version = getGPUVersion(contents)
					print "========= GPU local_version, github_version: ", local_version, github_version
					if checkGPUVersion(local_version, github_version):
						UpdateExist = True
						UpdatePluginnames += "\n    - " + "GithubPluginUpdater (" + github_version + ")"
				
				#== die anderen Plugins - jedoch nur wenn Plugin installiert ist ===
				elif os.path.isfile(filenames[number-1]):
					last_commit = ""
					last_local_commit = config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value
					print "========= last_local_Commit:  ", last_local_commit, pluginnames[number-1]

					search_string = "<relative-time datetime="
					pos1 = contents.find(search_string)
					if pos1 > 0:
						last_commit = str(contents[pos1+25:pos1+25+19])

					if last_local_commit < last_commit:
						UpdateExist = True
						UpdatePluginnames += "\n    - " + pluginnames[number-1]

				if getContentCounter == getPageCounter:
					getUpdateInfoMessage(MessageBox.TYPE_INFO)

			except:
				import traceback
				traceback.print_exc()


def getUpdateInfoMessage(MessageBoxType = MessageBox.TYPE_INFO):

					global UpdateExist
					global session
					global UpdatePluginnames
					
					if UpdateExist:
						if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
							if config.plugins.githubpluginupdater.show_updatequestion.value == "False":
								AddPopup("\n = GithubPluginUpdater = \n\n  >>> es liegen für folgende Plugins Updates vor !!! <<<\n  " + UpdatePluginnames + "\n\n\n  zum Update den GithubPluginUpdater öffnen",MessageBoxType , int(config.plugins.githubpluginupdater.popups_timeout.value),'GPU_PopUp_Update')
							else:
								if reload_value:
									reload(GithubPluginUpdater)
								from GithubPluginUpdater import UpdateInfo
								session.open(UpdateInfo, UpdatePluginnames)
					else:
						if config.plugins.githubpluginupdater.enable_autocheck.value == "True":
							AddPopup("\n = GithubPluginUpdater = \n\n  keine Plugin-Updates gefunden",MessageBoxType, int(config.plugins.githubpluginupdater.popups_timeout.value),'GPU_PopUp_Update')
					
