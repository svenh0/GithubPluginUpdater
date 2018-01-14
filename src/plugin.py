from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigText, ConfigSubDict, ConfigYesNo
from Tools.Notifications import AddPopup
from Screens.MessageBox import MessageBox

from socket import timeout
from twisted.web.client import getPage

from GithubPluginUpdater import githuburls, search_strings, filenames, pluginnames, lastgithubcommits

import GithubPluginUpdater
import AutoUpdateCheck

VERSION = "1.1.0"

session = None
getPageCounter = 0
getContentCounter = 0
local_version = []
UpdateExist = False

config.plugins.githubpluginupdater.lastcommit = ConfigSubDict()
config.plugins.githubpluginupdater.update_check = ConfigSubDict()
for counter, pl in enumerate(pluginnames):
	config.plugins.githubpluginupdater.lastcommit[pl] = ConfigText(default=lastgithubcommits[counter])
	config.plugins.githubpluginupdater.update_check[pl] = ConfigYesNo(default = True)

def leaveStandby():
	global session
	try:
		print "=====[GithubPluginUpdater] aus standby aufgewacht ..."
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			reload(AutoUpdateCheck)
			from AutoUpdateCheck import loadPages as checkupdate
			checkupdate(session)

	except:
		import traceback
		traceback.print_exc()


def standbyCounterChanged(configElement):
	
	print "=====[GithubPluginUpdater] gehe in standby..."
	from Screens.Standby import inStandby
	inStandby.onClose.append(leaveStandby)


def sessionstart(reason, **kwargs):
	global session
	if kwargs.has_key("session") and reason == 0:
		session = kwargs["session"]
		print "=====[GithubPluginUpdater] sessionstart....", session
		#== add to set function at restart from standby
		config.misc.standbyCounter.addNotifier(standbyCounterChanged, initial_call = False)
		
		print "=====[GithubPluginUpdater] runUpdateCheck in sessionstart ...."
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			reload(AutoUpdateCheck)
			from AutoUpdateCheck import loadPages as checkupdate
			checkupdate(session)
	else:
		print "=====[GithubPluginUpdater] sessionstart ohne session...."
		pass

def autostart(reason, **kwargs):
	global session
	
	print "=====[GithubPluginUpdater] autostart - reason: ", reason
	if kwargs.has_key("session") and reason == 0:
		session = kwargs["session"]
		print "=====[GithubPluginUpdater] autostart mit session..."
	else:
		print "=====[GithubPluginUpdater] autostart ohne session..."
		pass

def main(session, **kwargs):

	reload(GithubPluginUpdater)
	try:
		from GithubPluginUpdater import UpdateScreen
		session.open(UpdateScreen)

#	reload(AutoUpdateCheck)
#	try:
#		from AutoUpdateCheck import loadPages as checkupdate
#		checkupdate(session)

	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):

	descriptors = []
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("github-Versionen updaten")+ " (" + VERSION + ")", where = PluginDescriptor.WHERE_SESSIONSTART, fnc=sessionstart) )
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("github-Versionen updaten")+ " (" + VERSION + ")", where=[ PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU ], fnc = main, needsRestart = False, icon = "GithubPluginUpdater.png") )
	#descriptors.append( PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, needsRestart = True, fnc = autostart) )

	return descriptors