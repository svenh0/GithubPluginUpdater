from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigText, ConfigSubDict, ConfigYesNo
from Tools.Notifications import AddPopup
from Screens.MessageBox import MessageBox

from socket import timeout
from twisted.web.client import getPage

from GithubPluginUpdater import githuburls, search_strings, filenames, pluginnames, lastgithubcommits

import GithubPluginUpdater
import AutoUpdateCheck

VERSION = "1.0.0"

gpu_session = None
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
	
	try:
		print "=====[GithubPluginUpdater] aus standby aufgewacht ..."
		#AddPopup("GithubPluginUpdater beim Aufwachen aus Standby gestartet",MessageBox.TYPE_INFO,15,'GPU_PopUp_START')
		
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			reload(AutoUpdateCheck)
			from AutoUpdateCheck import loadPages as checkupdate
			checkupdate()

	except:
		import traceback
		traceback.print_exc()


def standbyCounterChanged(configElement):
	
	print "=====[GithubPluginUpdater] gehe in standby..."
	from Screens.Standby import inStandby
	inStandby.onClose.append(leaveStandby)


def sessionstart(reason, **kwargs):
	global gpu_session
	if kwargs.has_key("session") and reason == 0:
		gpu_session = kwargs["session"]
		print "=====[GithubPluginUpdater] sessionstart...."
		#== add to set function at restart from standby
		config.misc.standbyCounter.addNotifier(standbyCounterChanged, initial_call = False)
		
		#config.plugins.githubpluginupdater.lastcommit = ConfigSubDict()
		#config.plugins.githubpluginupdater.update_check = ConfigSubDict()
		
		#for counter, pl in enumerate(pluginnames):
			#config.plugins.githubpluginupdater.lastcommit[pl] = ConfigText(default=lastgithubcommits[counter])
			#config.plugins.githubpluginupdater.update_check[pl] = ConfigYesNo(default = True)
			#print "==== value: ", config.plugins.githubpluginupdater.lastcommit[pl].value, pl

def autostart(reason, **kwargs):

	print "=====[GithubPluginUpdater] autostart - reason: ", reason
	if reason == 0:
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
		
			#config.plugins.githubpluginupdater.update_check = ConfigSubDict()
			#for counter, pl in enumerate(pluginnames):
			#	config.plugins.githubpluginupdater.update_check[pl] = ConfigYesNo(default = True)
			
			print "=====[GithubPluginUpdater] runUpdateCheck...."
			reload(AutoUpdateCheck)
			from AutoUpdateCheck import loadPages as checkupdate
			checkupdate()

def main(session, **kwargs):

	reload(GithubPluginUpdater)
	try:
		from GithubPluginUpdater import UpdateScreen
		session.open(UpdateScreen)


	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):

	descriptors = []
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("github-Versionen updaten")+ " (" + VERSION + ")", where = PluginDescriptor.WHERE_SESSIONSTART, fnc=sessionstart) )
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("github-Versionen updaten")+ " (" + VERSION + ")", where=[ PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU ], fnc = main, needsRestart = False, icon = "GithubPluginUpdater.png") )
	descriptors.append( PluginDescriptor(where = PluginDescriptor.WHERE_AUTOSTART, needsRestart = True, fnc = autostart) )

	return descriptors