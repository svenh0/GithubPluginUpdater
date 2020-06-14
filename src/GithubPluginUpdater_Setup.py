#!/usr/bin/python
# -*- coding: utf-8 -*-

# GUI (System)
from enigma import getDesktop

# GUI (Screens)
from Screens.Screen import Screen
from Components.ConfigList import ConfigListScreen
#from Screens.MessageBox import MessageBox
from GithubPluginUpdaterMessage import MessageBoxGPU as MessageBox

# GUI (Summary)
from Screens.Setup import SetupSummary
from Screens.LocationBox import LocationBox

# GUI (Components)
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.Label import Label

# Configuration
from Components.config import * 

import os
from datetime import datetime, timedelta
from . import _

PluginVersion = ""

sz_w = getDesktop(0).size().width()

class GithubPluginUpdaterSetup(Screen, ConfigListScreen):
	
	if sz_w == 1920:
		skin = """
		<screen name="GithubPluginUpdaterSetup" position="center,center" size="1200,820">
			<ePixmap pixmap="skin_default/buttons/red.png" position="10,5" size="295,70" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/green.png" position="305,5" size="295,70" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/yellow.png" position="600,5" size="295,70" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/blue.png" position="895,5" size="295,70" scale="stretch" alphatest="on" />
			<widget source="key_red" render="Label" position="10,5" zPosition="1" size="295,70" font="Regular;30" halign="center" valign="center" backgroundColor="#9f1313" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_green" render="Label" position="310,5" zPosition="1" size="300,70" font="Regular;30" halign="center" valign="center" backgroundColor="#1f771f" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_yellow" render="Label" position="610,5" zPosition="1" size="300,70" font="Regular;30" halign="center" valign="center" backgroundColor="#9f1313" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_blue" render="Label" position="910,5" zPosition="1" size="300,70" font="Regular;30" halign="center" valign="center" backgroundColor="#1f771f" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget name="config" position="10,90" itemHeight="35" size="1180,540" enableWrapAround="1" scrollbarMode="showOnDemand" />
			<ePixmap pixmap="skin_default/div-h.png" position="10,650" zPosition="2" size="1180,2" />
			<widget name="help" position="10,655" size="1180,145" font="Regular;32" />
		</screen>"""
	else:
		skin = """
		<screen name="GithubPluginUpdaterSetup" position="center,center" size="800,600">
			<ePixmap pixmap="skin_default/buttons/red.png" position="0,0" size="200,40" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/green.png" position="200,0" size="200,40" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/yellow.png" position="400,0" size="200,40" scale="stretch" alphatest="on" />
			<ePixmap pixmap="skin_default/buttons/blue.png" position="600,0" size="200,40" scale="stretch" alphatest="on" />
			<widget source="key_red" render="Label" position="0,0" zPosition="1" size="200,40" font="Regular;22" halign="center" valign="center" backgroundColor="#9f1313" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_green" render="Label" position="200,0" zPosition="1" size="200,40" font="Regular;22" halign="center" valign="center" backgroundColor="#1f771f" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_yellow" render="Label" position="400,0" zPosition="1" size="200,40" font="Regular;22" halign="center" valign="center" backgroundColor="#9f1313" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget source="key_blue" render="Label" position="600,0" zPosition="1" size="200,40" font="Regular;22" halign="center" valign="center" backgroundColor="#1f771f" shadowColor="black" shadowOffset="-2,-2" transparent="1" />
			<widget name="config" position="5,50" itemHeight="30" size="790,450" enableWrapAround="1" scrollbarMode="showOnDemand" />
			<ePixmap pixmap="skin_default/div-h.png" position="0,501" zPosition="2" size="800,2" />
			<widget name="help" position="5,505" size="790,75" font="Regular;22" />
		</screen>"""


	def __init__(self, session):
		Screen.__init__(self, session)

		# Summary
		global PluginVersion
		from plugin import VERSION
		PluginVersion = VERSION
		self.skinName = "GithubPluginUpdaterSetup"
		self.setup_title = _("GithubPluginUpdater Setup ") + str(PluginVersion)
		self.onChangedEntry = []
		
		self.list = []
		self.buildConfig()
		ConfigListScreen.__init__(self, self.list, session = session, on_change = self.changed)

		def selectionChanged():
			if self["config"].current:
				self["config"].current[1].onDeselect(self.session)
			self["config"].current = self["config"].getCurrent()
			if self["config"].current:
				self["config"].current[1].onSelect(self.session)
			for x in self["config"].onSelectionChanged:
				x()
		self["config"].selectionChanged = selectionChanged
		self["config"].onSelectionChanged.append(self.updateHelp)

		# Initialize widgets
		self["key_green"] = StaticText(_("OK"))
		self["key_red"] = StaticText(_("Cancel"))
		self["key_yellow"] = StaticText(_("Update-Info"))
		self["key_blue"] = StaticText("")
		self["help"] = Label("")
		
		# Define Actions
		self["actions"] = ActionMap(["SetupActions", "ColorActions"],
			{
				"cancel": 	self.keyCancel,
				"save": 		self.keySave,
				"ok": 			self.ok,
				"yellow":		self.updateInfo,
			},-2)

		# Trigger change
		self.changed()

		self.onLayoutFinish.append(self.layoutFinished)

	def buildConfig(self):
		
		self.list.append( getConfigListEntry(_("Updatecheck and Info on starting the box"), config.plugins.githubpluginupdater.enable_autocheck, _("check on boxstart (also on GUI-Restart and start from Idle) for updates and show a message (none/only on updates/always). On 'always' show a message also if is not updates avaible.")) )
		
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			self.list.append( getConfigListEntry(_("   interval of AutoUpdateCheck on boxstart"), config.plugins.githubpluginupdater.autoCheck_interval, _("set the check-interval of AutoUpdateCheck on boxstart. Within the interval there is no renewed update check when the box is started.")) )
			
			self.list.append( getConfigListEntry(_("   duration of update-info-window (in seconds)"), config.plugins.githubpluginupdater.popups_timeout, _("set after how many seconds the update-info-window is closed (1-20 seconds, 0 = wait for key-press)")) )
			
			self.list.append( getConfigListEntry(_("   advanced update-info with question to open the plugin"), config.plugins.githubpluginupdater.show_updatequestion, _("show on update-info an additioal question, if you want to open directly the GithubPluginUpdater.")) )
			
			if config.plugins.githubpluginupdater.show_updatequestion.value == "True":
				self.list.append( getConfigListEntry(_("       answer for question is default set to:"), config.plugins.githubpluginupdater.updatequestion_defaultanswer, _("set the default answer to the question to open the GithubPluginUpdaters. on 'no' the plugin is not open automaically on timeout of the question.")) )
			
			from GithubPluginUpdater import pluginnames, filenames
			self.list.append( getConfigListEntry(_("   update-check for %s on boxstart") % pluginnames[4], config.plugins.githubpluginupdater.update_check[pluginnames[4]], _("set if you want to check for updates for this plugin on box-start.")) )
			for counter in range(len(pluginnames)-1):
				if os.path.isfile(filenames[counter]):
					self.list.append( getConfigListEntry(_("   update-check for %s on boxstart") % pluginnames[counter], config.plugins.githubpluginupdater.update_check[pluginnames[counter]], _("set if you want to check for updates for this plugin on box-start.")) )
		
		self.list.append( getConfigListEntry(_("option to check for github-updates / alternative"), config.plugins.githubpluginupdater.check_type, _("There are 3 options for the update check. The most reliable option is the 'api call', which has an access restriction of 60 calls per hour. A relapse alternative can be chosen at api.")) )
		self.list.append( getConfigListEntry(_("check only the src-folder"), config.plugins.githubpluginupdater.checkonly_src, _("Checks only the src folder for an update. Irrelevant updates outside of this folder are ignored, since only the src folder is updated anyway.")) )
		self.list.append( getConfigListEntry(_("show warning before a github update"), config.plugins.githubpluginupdater.show_warninginfo, _("The warning before a github update on the possible consequences of such an update can be activated or deactivated here.")) )
		self.list.append( getConfigListEntry(_("create a backup of the plugin before update"), config.plugins.githubpluginupdater.backup, _("create a backup from the local plugin before update the guthub-version.")) )
		if config.plugins.githubpluginupdater.backup.value:
			self.list.append( getConfigListEntry(_("   storage location for the plugin backup"), config.plugins.githubpluginupdater.backup_path, _("Defines the location for the plugin backup (selection with OK). The path is supplemented by the local plugin version number and date/time.")) )

	def layoutFinished(self):
		self.setTitle(self.setup_title)

	def ok(self):
		if self["config"].getCurrent()[1] == config.plugins.githubpluginupdater.backup_path:
			self.openDirectoryBrowser(config.plugins.githubpluginupdater.backup_path.value)

	def openDirectoryBrowser(self, path):
		try:
			self.session.openWithCallback(
				self.openDirectoryBrowserCB,
				LocationBox,
					windowTitle = _("Choose Directory:"),
					text = _("Choose directory"),
					currDir = str(path),
					bookmarks = None,
					autoAdd = False,
					editDir = True,
					inhibitDirs = ["/bin", "/boot", "/dev", "/etc", "/home", "/lib", "/proc", "/run", "/sbin", "/sys", "/usr", "/var"],
					minFree = 15 )
		except Exception, e:
			print('[GithubPluginUpdaterSetup] openDirectoryBrowser get failed: ', str(e))

	def openDirectoryBrowserCB(self, path):
		if path is not None:
			config.plugins.githubpluginupdater.backup_path.setValue(path)

	def setCustomTitle(self):
		self.setTitle(self.setup_title)

	def updateHelp(self):
		cur = self["config"].getCurrent()
		if cur:
			self["help"].text = cur[2]

	def changeConfig(self):
		self.list = []
		self.buildConfig()
		self["config"].setList(self.list)

	def changed(self):
		for x in self.onChangedEntry:
			x()
		current = self["config"].getCurrent()[1]
		if (current == config.plugins.githubpluginupdater.backup) or (current == config.plugins.githubpluginupdater.enable_autocheck) or (current == config.plugins.githubpluginupdater.show_updatequestion):
			self.changeConfig()
			return

	def getCurrentEntry(self):
		return self["config"].getCurrent()[0]

	def getCurrentValue(self):
		return str(self["config"].getCurrent()[1].getText())

	def createSummary(self):
		return SetupSummary
	
	def updateInfo(self):
		try:
			check_interval = [x for x in config.plugins.githubpluginupdater.autoCheck_interval.choices.choices if config.plugins.githubpluginupdater.autoCheck_interval.value == x[0]][0][1]
			lastcheck = datetime.fromtimestamp(int(config.plugins.githubpluginupdater.lastAutoCheck.value))
			text = 'GithubPluginUpdater Update-Info\n\nLetzter Update-Check: \t%s' % lastcheck
			text = text.expandtabs(14)
			if config.plugins.githubpluginupdater.enable_autocheck.value:
				#calculate the time for next updateCheck
				lastcheck = int(config.plugins.githubpluginupdater.lastAutoCheck.value)
				if config.plugins.githubpluginupdater.autoCheck_interval.value == "1":
					nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(hours=1)
				elif config.plugins.githubpluginupdater.autoCheck_interval.value == "2":
					nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(hours=6)
				elif config.plugins.githubpluginupdater.autoCheck_interval.value == "3":
					nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(hours=12)
				elif config.plugins.githubpluginupdater.autoCheck_interval.value == "4":
					nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(days=1)
				elif config.plugins.githubpluginupdater.autoCheck_interval.value == "5":
					nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(weeks=1)
				elif config.plugins.githubpluginupdater.autoCheck_interval.value == "6":
					#nextcheck = datetime.fromtimestamp(lastcheck) + timedelta(days=30)
					# goto next month
					next_month = datetime.fromtimestamp(lastcheck).replace(day=28) + timedelta(days=4)
					# reset day in the next month date
					nextcheck = next_month.replace(day=datetime.fromtimestamp(lastcheck).day) 
				if config.plugins.githubpluginupdater.autoCheck_interval.value != "0":
					text += '\nnächster Update-Check: \t%s' % nextcheck
					text = text.expandtabs(3)
				text += '\nCheck-Interval: \t%s' % check_interval
				text = text.expandtabs(34)
			self.session.open(MessageBox, text, MessageBox.TYPE_INFO)
		except:
			import traceback
			traceback.print_exc()

