#!/usr/bin/python
# -*- coding: utf-8 -*-

from Screens.Console import Console
from Tools.Notifications import AddPopup
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox
from Components.config import *

from Screens.Screen import Screen
from Components.Label import Label
from skin import parseColor
from Components.ActionMap import ActionMap
from pprint import pprint

# GUI (System) 
from enigma import eTimer, ePoint, eSize, getDesktop


from socket import timeout
from twisted.web.client import getPage

from Tools.BoundFunction import boundFunction

import Screens.Standby
import os
import subprocess
import time
import GithubPluginUpdater_Setup

PluginVersion = ""
counter = 0
test = False

pluginnames = ['SerienRecorder',
							'SeriesPlugin',
							'InfoBarTunerState',
							'EnhancedMovieCenter']

#default for load config-values
lastgithubcommits = [ '', '', '', '']

#to save the last read commits from github
last_commit   = ["", "", "", ""]

pluginsfolder = ['serienrecorder',
								 'SeriesPlugin',
								 'InfoBarTunerState',
								 'EnhancedMovieCenter']

filenames = [ '/usr/lib/enigma2/python/Plugins/Extensions/serienrecorder/SerienRecorderHelpers.py',
							'/usr/lib/enigma2/python/Plugins/Extensions/SeriesPlugin/plugin.py',
							'/usr/lib/enigma2/python/Plugins/Extensions/InfoBarTunerState/plugin.py',
							'/usr/lib/enigma2/python/Plugins/Extensions/EnhancedMovieCenter/EnhancedMovieCenter.py']

githuburls = [ 'https://github.com/einfall/serienrecorder/raw/master/src/SerienRecorderHelpers.py',
							 'https://github.com/betonme/e2openplugin-SeriesPlugin/raw/master/src/plugin.py',
							 'https://github.com/betonme/e2openplugin-InfoBarTunerState/raw/master/src/plugin.py',
							 'https://github.com/betonme/e2openplugin-EnhancedMovieCenter/raw/master/src/EnhancedMovieCenter.py']

githubcommiturls = [ 'https://github.com/einfall/serienrecorder',
							 'https://github.com/betonme/e2openplugin-SeriesPlugin',
							 'https://github.com/betonme/e2openplugin-InfoBarTunerState',
							 'https://github.com/betonme/e2openplugin-EnhancedMovieCenter']

gitzipurls = [ 'https://github.com/einfall/serienrecorder/archive/master.zip',
							 'https://github.com/betonme/e2openplugin-SeriesPlugin/archive/master.zip',
							 'https://github.com/betonme/e2openplugin-InfoBarTunerState/archive/master.zip',
							 'https://github.com/betonme/e2openplugin-EnhancedMovieCenter/archive/master.zip']

gitzip_folder = [ 'serienrecorder-master',
									'e2openplugin-SeriesPlugin-master',
									'e2openplugin-InfoBarTunerState-master',
									'e2openplugin-EnhancedMovieCenter-master']

search_strings = [ 'SRVERSION = ',
									 'VERSION = ',
									 'VERSION = ',
									 'EMCVersion = ']

sz_w = getDesktop(0).size().width()

########################################################################### 
class UpdateScreen(Screen):
	
	if sz_w == 1920:
		skin = """
		<screen name="GithubPluginUpdater" position="center,center" size="1200,680">
			<widget name="myLabel" position="15,10" size="1100,50" font="Regular;32"/>
			<eLabel text="Menü" position="1080,20" size="90,30" backgroundColor="#777777" halign="center" font="Regular;24"/>

			<eLabel text="(lokale Version)" position="440,80" size="300,50" font="Regular;32" foregroundColor="#FFFF00"/>
			<eLabel text="(github Version)" position="720,80" size="300,50" font="Regular;32" foregroundColor="#FFFF00"/>

			<widget name="myplugin1_name" position="15,165" size="420,50" font="Regular;32"/>
			<widget name="myplugin1_lokal_version" position="440,150" size="200,40" font="Regular;32"/>
			<widget name="myplugin1_git_version" position="720,150" size="200,40" font="Regular;32"/>
			<widget name="myplugin1_update" position="1020,165" size="130,40" backgroundColor="red" font="Regular;32"/>
			<widget name="myplugin1_lokal_date" position="440,190" size="270,40" font="Regular;24"/>
			<widget name="myplugin1_git_date" position="720,190" size="270,40" font="Regular;24"/>

			<widget name="myplugin2_name" position="15,265" size="420,50" font="Regular;32"/>
			<widget name="myplugin2_lokal_version" position="440,250" size="200,40" font="Regular;32"/>
			<widget name="myplugin2_git_version" position="720,250" size="200,40" font="Regular;32"/>
			<widget name="myplugin2_update" position="1020,265" size="130,40" backgroundColor="green" font="Regular;32"/>
			<widget name="myplugin2_lokal_date" position="440,290" size="270,40" font="Regular;24"/>
			<widget name="myplugin2_git_date" position="720,290" size="270,40" font="Regular;24"/>

			<widget name="myplugin3_name" position="15,365" size="420,50" font="Regular;32"/>
			<widget name="myplugin3_lokal_version" position="440,350" size="200,40" font="Regular;32"/>
			<widget name="myplugin3_git_version" position="720,350" size="200,40" font="Regular;32"/>
			<widget name="myplugin3_update" position="1020,365" size="130,40" backgroundColor="yellow" font="Regular;32"/>
			<widget name="myplugin3_lokal_date" position="440,390" size="270,40" font="Regular;24"/>
			<widget name="myplugin3_git_date" position="720,390" size="270,40" font="Regular;24"/>

			<widget name="myplugin4_name" position="15,465" size="420,50" font="Regular;32"/>
			<widget name="myplugin4_lokal_version" position="440,450" size="200,40" font="Regular;32"/>
			<widget name="myplugin4_git_version" position="720,450" size="200,40" font="Regular;32"/>
			<widget name="myplugin4_update" position="1020,465" size="130,40" backgroundColor="blue" font="Regular;32"/>
			<widget name="myplugin4_lokal_date" position="440,490" size="270,40" font="Regular;24"/>
			<widget name="myplugin4_git_date" position="720,490" size="270,40" font="Regular;24"/>

			<eLabel text="Status:" position="15,575" size="115,50" font="Regular;32" foregroundColor="#FFFF00"/>
			<widget name="status_txt" position="130,575" size="960,50" font="Regular;32"/>
		</screen>"""
	else:
		skin = """
		<screen name="GithubPluginUpdater" position="center,center" size="930,520">
			<widget name="myLabel" position="15,20" size="700,30" font="Regular;24"/>
			<eLabel text="Menü" position="850,20" size="70,20" backgroundColor="#777777" halign="center" font="Regular;18"/>

			<eLabel text="(lokale Version)" position="320,80" size="200,30" font="Regular;24" foregroundColor="#FFFF00"/>
			<eLabel text="(github Version)" position="550,80" size="200,30" font="Regular;24" foregroundColor="#FFFF00"/>

			<widget name="myplugin1_name" position="15,135" size="300,30" font="Regular;24"/>
			<widget name="myplugin1_lokal_version" position="320,120" size="200,30" font="Regular;24"/>
			<widget name="myplugin1_git_version" position="550,120" size="200,30" font="Regular;24"/>
			<widget name="myplugin1_update" position="800,135" size="100,30" backgroundColor="red" font="Regular;24"/>
			<widget name="myplugin1_lokal_date" position="320,150" size="200,40" font="Regular;18"/>
			<widget name="myplugin1_git_date" position="550,150" size="200,40" font="Regular;18"/>

			<widget name="myplugin2_name" position="15,215" size="300,30" font="Regular;24"/>
			<widget name="myplugin2_lokal_version" position="320,200" size="200,30" font="Regular;24"/>
			<widget name="myplugin2_git_version" position="550,200" size="200,30" font="Regular;24"/>
			<widget name="myplugin2_update" position="800,215" size="100,30" backgroundColor="green" font="Regular;24"/>
			<widget name="myplugin2_lokal_date" position="320,230" size="200,40" font="Regular;18"/>
			<widget name="myplugin2_git_date" position="550,230" size="200,40" font="Regular;18"/>

			<widget name="myplugin3_name" position="15,295" size="300,30" font="Regular;24"/>
			<widget name="myplugin3_lokal_version" position="320,280" size="200,30" font="Regular;24"/>
			<widget name="myplugin3_git_version" position="550,280" size="200,30" font="Regular;24"/>
			<widget name="myplugin3_update" position="800,295" size="100,30" backgroundColor="yellow" font="Regular;24"/>
			<widget name="myplugin3_lokal_date" position="320,310" size="200,40" font="Regular;18"/>
			<widget name="myplugin3_git_date" position="550,310" size="200,40" font="Regular;18"/>

			<widget name="myplugin4_name" position="15,375" size="300,30" font="Regular;24"/>
			<widget name="myplugin4_lokal_version" position="320,360" size="200,30" font="Regular;24"/>
			<widget name="myplugin4_git_version" position="550,360" size="200,30" font="Regular;24"/>
			<widget name="myplugin4_update" position="800,375" size="100,30" backgroundColor="blue" font="Regular;24"/>
			<widget name="myplugin4_lokal_date" position="320,390" size="200,40" font="Regular;18"/>
			<widget name="myplugin4_git_date" position="550,390" size="200,40" font="Regular;18"/>

			<eLabel text="Status:" position="15,450" size="90,30" font="Regular;24" foregroundColor="#FFFF00"/>
			<widget name="status_txt" position="110,450" size="790,30" font="Regular;24"/>
		</screen>"""


	
	def __init__(self, session, args = 0):
		self.session = session
		Screen.__init__(self, session)
		
		try:
			self["myLabel"] = Label("")
			global PluginVersion
			from plugin import VERSION
			PluginVersion = VERSION
			self.skinName = "GithubPluginUpdater"
			
			global pluginnames

			for i in range(len(pluginnames)):
				#print(i,pluginnames[i])
				self["myplugin" + str(i+1) + "_name"] = Label(pluginnames[i])
				self["myplugin" + str(i+1) + "_lokal_version"] = Label("...")
				self["myplugin" + str(i+1) + "_lokal_date"] = Label("(...)")
				self["myplugin" + str(i+1) + "_git_version"] = Label("")
				self["myplugin" + str(i+1) + "_git_date"] = Label("")
				self["myplugin" + str(i+1) + "_update"] = Label(" Update")
				self["myplugin" + str(i+1) + "_update"].hide()

			self["status_txt"] = Label("lokale Versionen wurden geladen")
			
			self["myActionMap"] = ActionMap(["EPGSelectActions", "SetupActions", "ColorActions", "MenuActions"],
				{
						"ok"    : self.keyOK,
						"cancel": self.cancel,
						"red"   : boundFunction(self.runUpdateScript, 1),
						"green" : boundFunction(self.runUpdateScript, 2),
						"yellow": boundFunction(self.runUpdateScript, 3),
						"blue"  : boundFunction(self.runUpdateScript, 4),
						"info"  : self.keyOK,
						"menu"  : self.menu
				},-1)
			
			self.reloadGitVersion = True
			self.reloadLocalVersion = True
			self.runUpdate = False
			self.updateExist = False
			self.getPageCounter = 0
			self.getContentCounter = 0
			self.getCommitCounter = 0
			self.getContentWithError = False
			self.onShown.append(self.loadPages)
			self.onLayoutFinish.append( self.LayoutFinish )

		except:
			import traceback
			traceback.print_exc()


	def LayoutFinish(self):
			
			self.setTitle("GithubPluginUpdater - " + PluginVersion)
			self["myLabel"].setText(_("zum Neuladen der github-Versionen 'OK' drücken "))

	def setup(self):
			
			reload(GithubPluginUpdater_Setup)
			try:
				from GithubPluginUpdater_Setup import GithubPluginUpdaterSetup
				self.session.open(GithubPluginUpdaterSetup)
				
			except:
				import traceback
				traceback.print_exc()


	def keyOK(self):
			
			self.reloadGitVersion = True
			self.reloadLocalVersion = True
			self.updateExist = False
			self.loadPages()

	def runUpdateScript(self, number, force_install = False):
		
		self.UpdateNumber  = number
		self.force_install = force_install
		
		local_version = self["myplugin" + str(number) + "_lokal_version"].getText()
		git_version = self["myplugin" + str(number) + "_git_version"].getText()
		
		if not local_version:
			return
		
		if test:
			last_github_commit = lastgithubcommits[number-1]
		else:
			last_github_commit = last_commit[number-1]
		
		if not force_install and (config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value >= last_github_commit):
			print "=== [GithubPluginUpdater] runScript Number with no update: ", number, last_github_commit, config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value
			#print "=== return ===="
			return
		
		if config.plugins.githubpluginupdater.show_warninginfo.value:
			self.session.openWithCallback(self.runUpdateScriptCallback, MessageBox, "Warnhinweis:\n\nPlugin-Versionen im github sind oft noch Test-Versionen und können gewisse Probleme nach der Installation verursachen!\n\nDaher sollten nur erfahrene User ein solches Update auf eine github-Version durchführen.\n\nSoll das github-Update jetzt gestartet werden?", MessageBox.TYPE_YESNO, default = False)
		else:
			self.runUpdateScriptCallback(True)


	def runUpdateScriptCallback(self, ret):

		if ret:
			global last_commit
			global pluginnames
			global lastgithubcommits

			number = self.UpdateNumber
			force_install = self.force_install

			check_curl = subprocess.check_output("opkg list-installed curl", shell=True)
			print "=== cmd-output curl ===: ", check_curl

			if not check_curl:
				check_wget = subprocess.check_output("opkg list-installed wget", shell=True)
				print "=== cmd-output wget ===: ", check_wget

			if not check_curl and not check_wget:
				self.session.open(MessageBox, "Das Update konnte nicht gestartet werden!\n\nEs muss erst das curl-Paket installiert werden.\n\nDas curl-Paket kann im Plugin per Menü-Taste über den Eintrag 'curl-Paket auf der Box installieren' installiert werden!.\n\n\nper Telnet geht es z.B. mit folgendem Befehl:\n\n opkg install curl", MessageBox.TYPE_INFO)
				return

			try:
				global PluginVersion
			
				#print "[GithubPluginUpdater] Start Plugin - Version: ", PluginVersion
			
				#set backup_path ======================
				self.backuplocation = self.getBackupLocation()
			
				self.reloadGitVersion = True
				self.reloadLocalVersion = True
				self.updateExist = False
				self.runUpdate = True

				cmd = self.getConsoleCmd(number)
				self.session.open(Console,_("GithubPluginUpdater") + " (" + PluginVersion + ")",[cmd])
			
				config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value = last_commit[number-1]
				config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].save()
				config.plugins.githubpluginupdater.save()
		
			except:
				import traceback
				traceback.print_exc()


	def getBackupLocation(self):
			
			if config.plugins.githubpluginupdater.backup_path.value:
				backuplocation = config.plugins.githubpluginupdater.backup_path.value
			elif config.plugins.configurationbackup.backuplocation.value:
				backuplocation = config.plugins.configurationbackup.backuplocation.value
				backuplocation = os.path.join(self.backuplocation, 'backup/')
			else:
				backuplocation = '/media/hdd/'
				backuplocation = os.path.join(self.backuplocation, 'backup/')
			return backuplocation


	def loadPages(self):
			
			if 			self.reloadGitVersion == False:
				return
			
			global githuburls
			global pluginnames

			self.getContentCounter = 0
			self.getPageCounter = 0
			self.getContentWithError = False

			for i in range(len(githuburls)):
				if self.reloadLocalVersion == True:
					self.getLocalVersion(pluginnames[i],i+1)
				if self["myplugin" + str(i+1) + "_lokal_version"].getText():
					self.getPage(githuburls[i], i+1)
			
			self.reloadGitVersion = False
			self.reloadLocalVersion = False


	def getPage(self, url, number):

			self["status_txt"].setText("lade github-Versionen ...")

			self.getPageCounter += 2
			
			self["myplugin" + str(number) + "_git_version"].instance.setForegroundColor(parseColor("foreground"))
			self["myplugin" + str(number) + "_lokal_version"].instance.setForegroundColor(parseColor("foreground"))
			self["myplugin" + str(number) + "_name"].instance.setForegroundColor(parseColor("foreground"))
			self["myplugin" + str(number) + "_git_version"].setText("...")
			self["myplugin" + str(number) + "_git_date"].setText("(...)")
			self["myplugin" + str(number) + "_update"].hide()
			deferred = getPage(url, timeout=5)
			deferred.addCallback(self.getWebContent, number)
			deferred.addErrback(self.errorHandler, number)

			url = githubcommiturls[number-1]
			self.deferred = getPage(url, timeout=5)
			self.deferred.addCallback(self.getLastCommit, number)
			self.deferred.addErrback(self.errorHandler, number)


	def errorHandler(self, result, number):
			
			self.getContentCounter += 1
			self.getContentWithError = True
			print "== GithubPluginUpdater getContentError: ", number, result

			self.checkIfLastPage()


	def getWebContent(self, contents, number):
			
			self.getContentCounter += 1

			pos1 = contents.find(search_strings[number-1])
			if pos1 > 0:
				pos2 = contents.find("\n",pos1+len(search_strings[number-1]))
				git_version = str(contents[pos1:pos2])
				git_version = git_version.replace(search_strings[number-1],"")
				git_version = git_version.replace("'","")
				git_version = git_version.replace('"',"")
				#set github version in the screen
				self["myplugin" + str(number) + "_git_version"].setText(git_version)

			self.checkIfLastPage()


	def getLastCommit(self, contents, number):
			
			try:

				global pluginnames
				global lastgithubcommits
				global last_commit
				
				self.getContentCounter += 1
				search_string = "<relative-time datetime="
				
				pos1 = contents.find(search_string)
				if pos1 > 0:
					last_commit[number-1] = str(contents[pos1+25:pos1+25+19])
				
				if test:
					last_local_commit = lastgithubcommits[number-1]
				else:
					last_local_commit = config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value
				
				#print "===== local_Commit, last_commit: ", last_local_commit, last_commit[number-1], pluginnames[number-1]
				
				local_version = self["myplugin" + str(number) + "_lokal_version"].getText()

				if len(local_version) and (last_local_commit < last_commit[number-1]):
					self["myplugin" + str(number) + "_git_version"].instance.setForegroundColor(parseColor("red"))
					self["myplugin" + str(number) + "_name"].instance.setForegroundColor(parseColor("red"))
					self["myplugin" + str(number) + "_update"].show()
					self.updateExist = True
					print "===== new commit === local_Commit, last_commit: ", last_local_commit, last_commit[number-1], pluginnames[number-1]
				else:
					self["myplugin" + str(number) + "_git_version"].instance.setForegroundColor(parseColor("foreground"))
					self["myplugin" + str(number) + "_lokal_version"].instance.setForegroundColor(parseColor("green"))
					self["myplugin" + str(number) + "_name"].instance.setForegroundColor(parseColor("foreground"))
					self["myplugin" + str(number) + "_update"].hide()

				self["myplugin" + str(number) + "_git_date"].setText(last_commit[number-1])

				self.checkIfLastPage()

			except:
				import traceback
				traceback.print_exc()

	def checkIfLastPage(self):
			
			if self.getContentCounter == self.getPageCounter:
				if self.getContentWithError:
					self["status_txt"].setText("github-Versionen wurden geladen (mit Fehler)")
				else:
					if self.updateExist:
						self["status_txt"].setText("github-Versionen wurden geladen - Updates vorhanden")
					else:
						self["status_txt"].setText("github-Versionen wurden geladen - keine Updates vorhanden")
				self.getContentCounter = 0
				self.getPageCounter = 0
				self.getContentWithError = False
				
				for i in range(len(pluginnames)):
					if self["myplugin" + str(i+1) + "_lokal_version"].getText() and not config.plugins.githubpluginupdater.lastcommit[pluginnames[i]].value:
						self.session.open(MessageBox, 'Es existieren nicht für alle Plugins lokale github-Datumswerte, die zum Versionsvergleich genutzt werden.\nDaher werden diese Plugins automatisch als Update angeboten. Es gibt folgende Möglichkeiten erstmals ein lokales github-Datum zu speichern:\n\n1. wenn alle Plugins auf der Box tatsächlich aktuell sind, dann kann per Menü-Taste die Option "setze für alle Plugins das aktuelle github-Datum" gewählt werden\n\noder\n\n2. die jeweiligen Plugins können per Farb-Taste aktualisiert werden.\n\nDanach sollten alle Plugins als aktuell angezeigt werden.', MessageBox.TYPE_INFO)
						break


	def getLocalVersion(self, PluginName, number):
		
		try:

			local_label_name = "myplugin" + str(number) + "_lokal_version"
			
			local_version = self.readLocalVersion(number)
			self[local_label_name].setText(local_version)
			self[local_label_name].show()
			
			local_label_name = "myplugin" + str(number) + "_lokal_date"
			if not len(local_version):
				self[local_label_name].setText("")
			else:
				if test:
					last_local_commit = lastgithubcommits[number-1]
				else:
					last_local_commit = config.plugins.githubpluginupdater.lastcommit[pluginnames[number-1]].value
				self[local_label_name].setText(last_local_commit)

		except:
			import traceback
			traceback.print_exc()
	
	def readLocalVersion(self, number):
		
		try:
			
			global filenames
			global search_strings
			
			local_version = "..."
			
			if not os.path.isfile(filenames[number-1]):
				return ""

			with open(filenames[number-1], 'r') as input_file:
				for line_number, line in enumerate(input_file):
					if search_strings[number-1] in line:
						local_version=line
						local_version = local_version.replace(search_strings[number-1],"")
						local_version = local_version.replace("'","")
						local_version = local_version.replace('"',"")
						local_version = local_version.replace("\n","")
						break
			
			return local_version
		
		except:
			import traceback
			traceback.print_exc()


	def menu(self):
		
		list = []
		
		list.append((_("Setup"), "setup"))
		
		list.append(("--", ""))
		
		for i in range(len(pluginnames)):
			if os.path.isfile(filenames[i]):
				list.append((_("Erzwinge Update für " + pluginnames[i]), "force_update_" + str(i)))
		
		list.append(("--", ""))
		
		list.append((_("setze für alle Plugins das aktuelle github-Datum"), "setallgitdate"))
		list.append((_("lösche für alle Plugins das aktuelle github-Datum"), "resetallgitdate"))
		
		list.append(("--", ""))
		check_curl = subprocess.check_output("opkg list-installed curl", shell=True)
		if not check_curl:
			list.append((_("curl-Paket auf der Box installieren"), "install_curl"))
		else:
			list.append((_("curl-Paket auf der Box deinstallieren"), "remove_curl"))
		
		list.append(('--', ''))
		list.append((_('Plugin-Backup wiederherstellen'), 'restore_backup'))
		
		self.session.openWithCallback(
			self.menuCallback,
			ChoiceBox, 
			title = _('Menü GithubPluginUpdater'),
			list = list,
		)

	def menuCallback(self, ret):
		ret = ret and ret[1]
		print "=== ret ===", ret
		if ret:
			if ret == "setup":
				self.setup()
			elif ret == "force_update_0":
				self.runUpdateScript(1, True)
			elif ret == "force_update_1":
				self.runUpdateScript(2, True)
			elif ret == "force_update_2":
				self.runUpdateScript(3, True)
			elif ret == "force_update_3":
				self.runUpdateScript(4, True)
			elif ret == "resetallgitdate":
				for i in range(len(pluginnames)):
					config.plugins.githubpluginupdater.lastcommit[pluginnames[i]].value = ""
					config.plugins.githubpluginupdater.lastcommit[pluginnames[i]].save()
				config.plugins.githubpluginupdater.save()
				self.keyOK()
			elif ret == "setallgitdate":
				for i in range(len(pluginnames)):
					config.plugins.githubpluginupdater.lastcommit[pluginnames[i]].value = last_commit[i]
					config.plugins.githubpluginupdater.lastcommit[pluginnames[i]].save()
				config.plugins.githubpluginupdater.save()
				self.keyOK()
			elif ret == "install_curl":
				cmd = "opkg install curl"
				self.session.open(Console,_("GithubPluginUpdater") + " (" + PluginVersion + ")",[cmd])
			elif ret == "remove_curl":
				cmd = "opkg remove curl"
				self.session.open(Console,_("GithubPluginUpdater") + " (" + PluginVersion + ")",[cmd])
			elif ret == 'restore_backup':
				list = []
				for i in range(len(pluginnames)):
					if os.path.isfile(filenames[i]):
						list.append((_('Backup für ' + pluginnames[i]) + ' wiederherstellen', 'restore_backup_' + str(i)))

				if len(list):
					self.session.openWithCallback(self.backupmenuCallback, ChoiceBox, title=_('Menü Plugin-Backup wiederherstellen'), list=list)
				else:
					self.session.open(MessageBox, 'keines der möglichen Plugins ist auf der Box installiert.\nEine Backup-Wiederherstellung ist dadurch nicht möglich.', MessageBox.TYPE_INFO)

	def backupmenuCallback(self, ret):
		ret = ret and ret[1]
		print '=== ret backupmenu ===', ret
		if ret:
			if ret == 'restore_backup_0':
				self.backuplocation = os.path.join(self.getBackupLocation(), pluginnames[0])
				self.backup_pluginName = pluginnames[0]
			elif ret == 'restore_backup_1':
				self.backuplocation = os.path.join(self.getBackupLocation(), pluginnames[1])
				self.backup_pluginName = pluginnames[1]
			elif ret == 'restore_backup_2':
				self.backuplocation = os.path.join(self.getBackupLocation(), pluginnames[2])
				self.backup_pluginName = pluginnames[2]
			elif ret == 'restore_backup_3':
				self.backuplocation = os.path.join(self.getBackupLocation(), pluginnames[3])
				self.backup_pluginName = pluginnames[3]
			
			list = []
			if os.path.isdir(self.backuplocation):
				dirs = os.listdir(self.backuplocation)
				for file in dirs:
					file_path = os.path.join(self.backuplocation, file)
					if os.path.isdir(file_path):
						list.append((str(file), str(file_path)))

			if len(list):
				list.sort(reverse=True)
				self.session.openWithCallback(self.backupfolderCallback, ChoiceBox, title=_("Backup für das Plugin '%s' auswählen") % self.backup_pluginName, list=list)
			else:
				self.session.open(MessageBox, _("keine Backups für das Plugins '" + self.backup_pluginName + "' gefunden."), MessageBox.TYPE_INFO)


	def backupfolderCallback(self, ret):
		ret = ret and ret[1]
		print '=== ret backupfolder ===', ret
		if ret:
			self.backup_pluginPath = ret
			self.session.openWithCallback(self.runRestoreBackupCallback, MessageBox, _("Soll das nachfolgende Backup für das Plugin '" + self.backup_pluginName + "' wirklich wiederhergestellt werden?\n\nBackup:\n") + str(ret), MessageBox.TYPE_YESNO)

	def runRestoreBackupCallback(self, ret):
		
		global pluginsfolder
		if ret:
			number = pluginnames.index(self.backup_pluginName) + 1
			
			if not os.path.isfile(filenames[number - 1]):
				self.session.open(MessageBox, _("Die Backup-Wiederherstellung für das Plugin '" + self.backup_pluginName + "' ist fehlgeschlagen.\n\nMöglicherweise befinden sich nicht alle Plugin-Dateien im nachfolgenden Backup-Ordner:\n\n") + self.backup_pluginPath, MessageBox.TYPE_INFO)
				return
			
			self.reloadGitVersion = True
			self.reloadLocalVersion = True
			self.updateExist = False
			self.runUpdate = True
			
			newLine = '\n'
			cmd = newLine
			cmd += 'echo -e "========================================================"' + newLine
			cmd += 'echo -e "\n  Backup-Wiederherstellung für das Plugin -' + self.backup_pluginName + '-"' + newLine
			cmd += "local_version=$(grep '" + search_strings[number - 1] + "' " + filenames[number - 1] + ')' + newLine
			cmd += 'local_version=$(echo $local_version | sed "s/' + search_strings[number - 1] + '//")' + newLine
			cmd += 'echo -e "\n  installierte Version vor der Backup-Wiederherstellung: $local_version"' + newLine
			cmd += 'echo -e "\n  kopiere Backup-Dateien ......"' + newLine
			cmd += 'cp -pr ' + self.backup_pluginPath + '/* /usr/lib/enigma2/python/Plugins/Extensions/' + pluginsfolder[number - 1] + '/' + newLine
			cmd += "local_version=$(grep '" + search_strings[number - 1] + "' " + filenames[number - 1] + ')' + newLine
			cmd += 'local_version=$(echo $local_version | sed "s/' + search_strings[number - 1] + '//")' + newLine
			cmd += 'echo -e "\n  installierte Version nach der Backup-Wiederherstellung: $local_version"' + newLine
			cmd += 'echo -e "\n========================================================\n\n"' + newLine
			
			self.session.open(Console, _('GithubPluginUpdater') + ' (' + PluginVersion + ')', [cmd])
			
			backup_datum = self.backup_pluginPath[self.backup_pluginPath.rfind('/') + 1:]
			backup_datum = backup_datum[len(backup_datum) - 19:]
			if len(backup_datum) != 19:
				backup_datum = ''
			else:
				backup_datum_list = list(backup_datum)
				backup_datum_list[10] = 'T'
				backup_datum_list[13] = ':'
				backup_datum_list[16] = ':'
				backup_datum = ''.join(backup_datum_list)
			
			config.plugins.githubpluginupdater.lastcommit[pluginnames[number - 1]].value = backup_datum
			config.plugins.githubpluginupdater.lastcommit[pluginnames[number - 1]].save()
			config.plugins.githubpluginupdater.save()


	def cancel(self):
			
			self.reloadGitVersion = False
			self.reloadLocalVersion = False
			if hasattr(self, "deferred"):
				self.deferred.cancel()
				del self.deferred
			if self.runUpdate == True:
				self.session.openWithCallback(self.restartGUI, MessageBox, "Es wurden Plugins aktualisiert!\nSoll jetzt ein GUI-Neustart durchgeführt werden?", MessageBox.TYPE_YESNO)
			else:
				#self.close(False,self.session)
				self.close()
				

	def restartGUI(self, doRestart):
			
			if doRestart:
				self.session.open(Screens.Standby.TryQuitMainloop, 3)
				self.close()
			else:
				self.close()


	def getConsoleCmd(self, number):
	
			global pluginsfolder
			global gitzip_folder
			global search_strings
			
			newLine = "\n"
			cmd  = 'cd /tmp' + newLine
			cmd += 'unset LD_PRELOAD' + newLine
			cmd += 'echo -e "========================================================"' + newLine
			cmd += 'echo -e "\n  == Update ' + pluginnames[number-1] + ' =="' + newLine
			cmd += "local_version=$(grep '" + search_strings[number-1] + "' " + filenames[number-1] + ")" + newLine
			cmd += 'local_version=$(echo $local_version | sed "s/' + search_strings[number-1] + '//")' + newLine
			cmd += 'echo -e "\n  installierte Version vor dem Update: $local_version"' + newLine
			
			if config.plugins.githubpluginupdater.backup.value:
				cmd += "folder_version=" + self["myplugin" + str(number) + "_lokal_version"].getText() + newLine
				backupPath = os.path.join(self.backuplocation + pluginnames[number-1], self["myplugin" + str(number) + "_lokal_version"].getText().replace('\n', '').replace('\r', '') + time.strftime('_%Y-%m-%d_%H-%M-%S') + '/')

				#print "=== BackupPath: ", backupPath
				cmd += 'mkdir -p ' + backupPath + newLine
				cmd += '#echo -e "Pfad: ' + backupPath + '"' + newLine
				cmd += "echo -e " + '"' + "\n  sichere lokale Version in '" + backupPath + "'......" + '"' + newLine
				cmd += 'cp -pr /usr/lib/enigma2/python/Plugins/Extensions/' + pluginsfolder[number-1] + '/* ' + backupPath + newLine
			
			cmd += 'echo -e "\n  lade aktuelle Version von Github......"' + newLine

			#== fuer die DMM-Variante mit curl:  curl gibt es als Paket im jeweiligen Feed unter www.dreamboxupdate.com =======
			
			UpdateZipFile = "Update_" + pluginnames[number-1] + ".zip"
			cmd += 'wget -o /tmp/' + UpdateZipFile + ' ' + gitzipurls[number-1] + ' 2>/dev/null || curl -A "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3" -o /tmp/' + UpdateZipFile + ' -sL ' + gitzipurls[number-1] + newLine

			cmd += 'echo -e "\n  installiere aktuelle Github-Version......"' + newLine
			cmd += 'unzip -oq ' + UpdateZipFile + newLine
			cmd += 'cp -pr /tmp/' + gitzip_folder[number-1] + '/src/* /usr/lib/enigma2/python/Plugins/Extensions/' + pluginsfolder[number-1] + '/' + newLine
			cmd += 'rm -rf /tmp/' + gitzip_folder[number-1] +' /tmp/' + UpdateZipFile + newLine
			
			cmd += "local_version=$(grep '" + search_strings[number-1] + "' " + filenames[number-1] + ")" + newLine
			cmd += 'local_version=$(echo $local_version | sed "s/' + search_strings[number-1] + '//")' + newLine
  
			cmd += 'echo -e "\n  installierte Version nach dem Update: $local_version"' + newLine
			cmd += 'echo -e "\n========================================================\n\n"'
			
			return cmd


class UpdateInfo(Screen):
	
	skin = """ <screen position="90,90" size="0,0" title="Update Info"></screen>"""

	def __init__(self, session, UpdatePluginnames=""):
		Screen.__init__(self, session)
		
		self.session = session
		self.UpdatePluginnames = UpdatePluginnames
		self.firsttime = True
		self.onShown.append(self.showmsg)
		self.onLayoutFinish.append( self.LayoutFinish )

	def LayoutFinish(self):
		
		self.setTitle("GithubPluginUpdater - Updateinfo")

	def showmsg(self):
		
		if self.firsttime:
			self.firsttime = False
			default_answer = False
			if config.plugins.githubpluginupdater.updatequestion_defaultanswer.value == "True":
				default_answer = True
			self.session.openWithCallback(self.openGPU, MessageBox, "\n = GithubPluginUpdater = \n\n  >>> es liegen für folgende Plugins Updates vor !!! <<<\n  " + self.UpdatePluginnames + "\n\n\nSoll der GithubPluginUpdater geöffnet werden?", MessageBox.TYPE_YESNO, timeout = int(config.plugins.githubpluginupdater.popups_timeout.value), default = default_answer)
	
	def openGPU(self, confirm):
		
		if confirm:
			self.session.open(UpdateScreen)
		self.close()
