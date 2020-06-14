# -*- coding: utf-8 -*-

from Components.config import config
#from Tools.Notifications import AddPopup
#from Screens.MessageBox import MessageBox
from GithubPluginUpdaterMessage import MessageBoxGPU as MessageBox
from GithubPluginUpdaterMessage import AddPopupGPU as AddPopup
from Screens.Screen import Screen

from socket import timeout
from twisted.web.client import getPage
from Tools.BoundFunction import boundFunction

from GithubPluginUpdater import reload_value, githuburls, pluginnames, lastgithubcommits, githubcommiturls, githubcommitlisturls,search_strings, filenames, getBranch

import GithubPluginUpdater
import os
import time
from . import _

try:
	import simplejson as json
except ImportError:
	import json

session = None
getPageCounter = 0
getContentCounter = 0
UpdateExist = False
UpdatePluginnames = ""

limit_remaining = 60
limit_resetTime = 0
checkType = ""

def startAutoUpdate(gpu_session):
			#print "=====[GithubPluginUpdater] startAutoUpdate"
			global session
			session = gpu_session
			
			import Screens.Standby
			if Screens.Standby.inStandby:
				print "[GithubPluginUpdater] inStandby - don't check for updates"
				return
			
			if config.plugins.githubpluginupdater.check_type.value.startswith("api"):
				#load rate limit at first if check with api
				headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',}
				url = "https://api.github.com/rate_limit"
				deferred = getPage(url, timeout=10, headers=headers)
				deferred.addCallback(loadLimitRemaining_getWebContent)
				deferred.addErrback(errorHandler, 0)
			else:
				loadPages()

def loadLimitRemaining_getWebContent(contents):
			#print "=====[GithubPluginUpdater] AutoUpdate loadLimitRemainig_getWebContent"
			contents = json.loads(contents)
			
			global limit_remaining, limit_resetTime
			limit_remaining = contents['rate']['remaining']
			limit_resetTime = contents['rate']['reset']
			#print "=====[GithubPluginUpdater] AutoUpdate LimitRemainig", limit_remaining
			loadPages()

def loadPages():
			
			#print "=====[GithubPluginUpdater] start loadPages"
			global githuburls
			global githubcommiturls
			global getPageCounter
			global session
			global UpdatePluginnames
			global getContentCounter
			global limit_remaining, limit_resetTime
			global checkType
			
			getContentCounter = 0
			getPageCounter = 0
			UpdateExist = False
			UpdatePluginnames = ""
			getPageCounter = 0
			
			headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',}

			for i in range(len(githubcommiturls)):
				#check for last github-commit-Date
				if os.path.isfile(filenames[i]) and config.plugins.githubpluginupdater.update_check[pluginnames[i]].value:
					getPageCounter +=1
					
					#set url to get lastcommit-Date
					if int(limit_remaining) > 0 and config.plugins.githubpluginupdater.check_type.value.startswith("api"):
						if config.plugins.githubpluginupdater.checkonly_src.value:
							url = "https://api.github.com/repos/" + githubcommitlisturls[i] + "/commits?callback=commits&tree=%s&path=src&page=1&per_page=1" % getBranch(i+1)
						else:
							url = "https://api.github.com/repos/" + githubcommitlisturls[i] + "/commits?callback=commits&tree=%s&page=1&per_page=1" % getBranch(i+1)
						checkType = "api"
					
					elif (int(limit_remaining) == 0 and config.plugins.githubpluginupdater.check_type.value == "api-normal") or config.plugins.githubpluginupdater.check_type.value == "normal":
						url = githubcommiturls[i]
						if config.plugins.githubpluginupdater.checkonly_src.value:
							url += "/tree/%s/src" % getBranch(i+1) # check only src-folder
						checkType = "normal"
					
					elif config.plugins.githubpluginupdater.check_type.value in ("commits","api-commits"):
						url = githubcommiturls[i] + "/commits/%s" % getBranch(i+1)
						if config.plugins.githubpluginupdater.checkonly_src.value:
							url += "/src" # check only src-folder
						checkType = "commits"

					deferred = getPage(url, timeout=10, headers=headers)
					deferred.addCallback(getLastCommit, i+1)
					deferred.addErrback(errorHandler, i+1)
					#print "=====[GithubPluginUpdater] start loadPages - check", pluginnames[i], url

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
				global limit_remaining, limit_resetTime
				
				#print "=====[GithubPluginUpdater] getLastCommit for:", pluginnames[number-1]
				
				getContentCounter += 1
				
				checkonly = "main"
				if config.plugins.githubpluginupdater.checkonly_src.value: checkonly = "src"
				
				#== die anderen Plugins - jedoch nur wenn das Plugin installiert ist ===
				if os.path.isfile(filenames[number-1]):
					last_commit = ""
					last_local_commit = config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value
					#print "========= last_local_Commit:  ", last_local_commit, pluginnames[number-1]

					if int(limit_remaining) > 0 and config.plugins.githubpluginupdater.check_type.value.startswith("api"):
						jsonp = contents
						contents = jsonp[ jsonp.index("(") + 1 : jsonp.rindex(")") ]
						commits = json.loads(contents)
						#print "=== contents: ", commits['meta']
						#limit_remaining = commits['meta']['X-RateLimit-Remaining']
						#limit_resetTime = commits['meta']['X-RateLimit-Reset']
						#limit = commits['meta']['X-RateLimit-Limit']
						
						if limit_remaining != "0":
							commits = commits['data']
							for commit in commits:
								if commit:
									#print "=== commit: ", commit
									last_commit = str(commit['commit']['author']['date'][:-1])
									last_commit_info = str(commit['commit']['message'])
									#print "=== Commit-Info:", pluginnames[number-1], last_commit[number-1], last_commit_info[number-1]
									
									print "[GithubPluginUpdater] commit-date:", "api", checkonly, limit_remaining, pluginnames[number-1], last_commit
					
					#fallback for limit_remaining or not use api
					if int(limit_remaining) == 0 or config.plugins.githubpluginupdater.check_type.value.startswith("api") == False:
						search_string = "<relative-time datetime="
						pos1 = contents.find(search_string)
						if pos1 > 0:
							print "[GithubPluginUpdater] found relative time:", checkType, checkonly, pluginnames[number-1], str(contents[pos1+25:pos1+25+19])
							last_commit = str(contents[pos1+25:pos1+25+19])
						else:
							#print "===== not found relative-time ==", pluginnames[number-1]
							if not config.plugins.githubpluginupdater.checkonly_src.value:
								search_string = 'class="js-navigation-open" title="src" id='
								pos1 = contents.find(search_string)
							else:
								pos1=1
							if pos1 > 0:
								#print "=== found src on pos:", pos1
								search_string = "<time-ago datetime="
								pos2 = contents.find(search_string, pos1)
								if pos2 > 0:
									print "[GithubPluginUpdater] found time ago:", checkType, checkonly, pluginnames[number-1], str(contents[pos2+20:pos2+20+19])
									last_commit = str(contents[pos2+20:pos2+20+19])
								else:
									print "===== not found time ago for:", pluginnames[number-1]
							else:
								print "===== not found time-values for:", pluginnames[number-1]
					
					if last_local_commit < last_commit:
						UpdateExist = True
						UpdatePluginnames += "\n    - " + pluginnames[number-1]
						print "[GithubPluginUpdater] new commit:", last_local_commit, last_commit, pluginnames[number-1]

				if getContentCounter == getPageCounter:
					print "[GithubPluginUpdater] UsedCheckType: %s %s, remaining: %s, ConfigCheckType: %s" % (checkType, checkonly, limit_remaining, config.plugins.githubpluginupdater.check_type.value)
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
						AddPopup(_("\n = GithubPluginUpdater = \n\n  >>> there are updates for the following plugins !!! <<<\n  %s\n\n\n  open the GithubPluginUpdater for the update") % UpdatePluginnames,MessageBoxType , int(config.plugins.githubpluginupdater.popups_timeout.value),'GPU_PopUp_Update')
					else:
						if reload_value:
							reload(GithubPluginUpdater)
						from GithubPluginUpdater import UpdateInfo
						session.open(UpdateInfo, UpdatePluginnames)
			else:
				if config.plugins.githubpluginupdater.enable_autocheck.value == "True":
					AddPopup(_("\n = GithubPluginUpdater = \n\n  no plugin updates found"),MessageBoxType, int(config.plugins.githubpluginupdater.popups_timeout.value),'GPU_PopUp_Update')
			
			#set lastAutoCheckTime
			config.plugins.githubpluginupdater.lastAutoCheck.value = int(time.time())
			config.plugins.githubpluginupdater.lastAutoCheck.save()

