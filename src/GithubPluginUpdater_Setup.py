#!/usr/bin/python
# -*- coding: utf-8 -*-

# GUI (System)
from enigma import getDesktop

# GUI (Screens)
from Screens.Screen import Screen
from Components.ConfigList import ConfigListScreen
from Screens.MessageBox import MessageBox

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
		self["key_yellow"] = StaticText("Update-Info")
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
		
		self.list.append( getConfigListEntry(_("Updatecheck und Info beim Start der Box"), config.plugins.githubpluginupdater.enable_autocheck, _("Prüft beim Box-Start (auch GUI-Neustart und Start aus dem Idle) auf Updates und gibt eine Meldung aus (nein/nur bei Updates/immer). Bei 'immer' kommt auch eine Info-Meldung, dass kein Update verfügbar ist.")) )
		
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			self.list.append( getConfigListEntry(_("   Intervall für AutoUpdateCheck beim Start der Box"), config.plugins.githubpluginupdater.autoCheck_interval, _("Legt den Prüf-Intervall für den AutoUpdateCheck beim Start der Box fest. Innerhalb des Intervalls erfolgt kein erneuter Update-Check beim Start der Box.")) )
			
			self.list.append( getConfigListEntry(_("   Anzeigedauer für Update-Info-Fenster (in Sek)"), config.plugins.githubpluginupdater.popups_timeout, _("Legt fest, nach wieviel Sekunden das Update-Info-Fenster automatisch geschlossen wird (1-20 Sek., 0 = wartet auf Tastendruck)")) )
			
			self.list.append( getConfigListEntry(_("   erweiterte Update-Info mit Frage zum Öffnen des Plugins"), config.plugins.githubpluginupdater.show_updatequestion, _("Zeigt beim Update-Hinweis zusätzlich eine Frage, ob man den GithubPluginUpdater direkt direkt öffnen möchte.")) )
			
			if config.plugins.githubpluginupdater.show_updatequestion.value == "True":
				self.list.append( getConfigListEntry(_("       Antwort für Frage steht standardmäßig auf:"), config.plugins.githubpluginupdater.updatequestion_defaultanswer, _("Legt fest, welche Antwort für die Frage zum Öffnen des GithubPluginUpdaters standardmäßig vorausgewählt sein soll. Bei 'nein' öffnet sich das Plugin bei Zeitablauf der Frage nicht automatisch.")) )
			
			from GithubPluginUpdater import pluginnames, filenames
			self.list.append( getConfigListEntry(_("   Update-Check für %s bei Box-Start") % pluginnames[4], config.plugins.githubpluginupdater.update_check[pluginnames[4]], _("Legt fest, ob für das Plugin beim Box-Start eine Update-Prüfung durchgeführt werden soll.")) )
			for counter in range(len(pluginnames)-1):
				if os.path.isfile(filenames[counter]):
					self.list.append( getConfigListEntry(_("   Update-Check für %s bei Box-Start") % pluginnames[counter], config.plugins.githubpluginupdater.update_check[pluginnames[counter]], _("Legt fest, ob für das Plugin beim Box-Start eine Update-Prüfung durchgeführt werden soll.")) )
		
		self.list.append( getConfigListEntry(_("Variante zum Prüfen auf github-Updates / Alternative"), config.plugins.githubpluginupdater.check_type, _("Es gibt 3 Varianten zur Update-Prüfung. Am zuverlässigstens ist die Variante 'api-Abruf', welche eine Zugriffsbeschränkung von 60 Abrufen pro Stunde hat. Bei api kann eine Rückfall-Alternative gewählt werden.")) )
		self.list.append( getConfigListEntry(_("Prüfe nur den src-Ordner"), config.plugins.githubpluginupdater.checkonly_src, _("Prüft nur den src-Ordner auf ein Update. Dabei werden unrelevante Updates außerhalb dieses Ordners ignoriert, da eh nur der src-Ordner geupdatet wird.")) )
		self.list.append( getConfigListEntry(_("Warnhinweis vor einem github-Update anzeigen"), config.plugins.githubpluginupdater.show_warninginfo, _("Der Warnhinweis vor einem github-Update zu den möglichen Folgen eines solchen Updates kann hier aktiviert bzw. deaktiviert werden.")) )
		self.list.append( getConfigListEntry(_("erzeuge ein Backup des Plugins vor dem Update"), config.plugins.githubpluginupdater.backup, _("Legt vor dem Update der Github-Version ein Backup des lokalen Plugins an.")) )
		if config.plugins.githubpluginupdater.backup.value:
			self.list.append( getConfigListEntry(_("   Speicherort für das Plugin-Backup"), config.plugins.githubpluginupdater.backup_path, _("Legt den Ort für das Plugin-Backup fest (Auswahl mit OK). Der Pfad wird noch durch die lokale Plugin-Versionsnummer und Datum/Zeit ergänzt.")) )

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

