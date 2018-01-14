# -*- coding: utf-8 -*-

from Components.config import config
from Tools.Notifications import AddPopup
from Screens.MessageBox import MessageBox
from Screens.Screen import Screen

from socket import timeout
from twisted.web.client import getPage
from Tools.BoundFunction import boundFunction

from GithubPluginUpdater import test, githuburls, pluginnames, lastgithubcommits, githubcommiturls, search_strings, filenames

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
			
			session = gpu_session
			
			getContentCounter = 0
			getPageCounter = 0
			UpdateExist = False
			
			getPageCounter = 0

			for i in range(len(githubcommiturls)):
				
				if os.path.isfile(filenames[i]) and config.plugins.githubpluginupdater.update_check[pluginnames[i]].value:
					getPageCounter +=1
					deferred = getPage(githubcommiturls[i], timeout=10)
					deferred.addCallback(getLastCommit, i+1)
					deferred.addErrback(errorHandler, i+1)

def errorHandler(result, number):
			
			global getContentCounter
			global getPageCounter
			
			getContentCounter += 1
			if getContentCounter == getPageCounter:
				getUpdateInfoMessage(MessageBox.TYPE_ERROR)


def getLastCommit(contents, number):
			
			try:

				global getContentCounter
				global getPageCounter
				global UpdateExist
				global lastgithubcommits
				global session
				global UpdatePluginnames
			
				getContentCounter += 1
				
				#== nur wenn Plugin installiert ist ===
				if os.path.isfile(filenames[number-1]):
					last_commit = ""
					if test:
						last_local_commit = lastgithubcommits[number-1]
					else:
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
								reload(GithubPluginUpdater)
								from GithubPluginUpdater import UpdateInfo
								print "========= update exist - open Updatescreen ==============="
								session.open(UpdateInfo, UpdatePluginnames)
					else:
						if config.plugins.githubpluginupdater.enable_autocheck.value == "True":
							AddPopup("\n = GithubPluginUpdater = \n\n  keine Plugin-Updates gefunden",MessageBoxType, int(config.plugins.githubpluginupdater.popups_timeout.value),'GPU_PopUp_Update')
					
