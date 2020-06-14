from Plugins.Plugin import PluginDescriptor
from Components.config import config, ConfigText, ConfigSubDict, ConfigYesNo
from enigma import eTimer
from datetime import datetime, timedelta
import Screens.Standby
from . import _

from socket import timeout
from twisted.web.client import getPage

from GithubPluginUpdater import reload_value, githuburls, search_strings, filenames, pluginnames, lastgithubcommits

import GithubPluginUpdater
import AutoUpdateCheck

VERSION = "1.7.0"

session = None
updateTimer = None
updateTimer_conn = None
getPageCounter = 0
getContentCounter = 0
local_version = []
UpdateExist = False

config.plugins.githubpluginupdater.lastcommit = ConfigSubDict()
config.plugins.githubpluginupdater.update_check = ConfigSubDict()
for counter, pl in enumerate(pluginnames):
	config.plugins.githubpluginupdater.lastcommit[pl] = ConfigText(default=lastgithubcommits[counter])
	config.plugins.githubpluginupdater.update_check[pl] = ConfigYesNo(default = True)

try:
	from enigma import eMediaDatabase
	isDreamOS = True
except:
	isDreamOS = False

def leaveStandby():
	global session
	try:
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			print "[GithubPluginUpdater] wakeup from standby - runUpdateCheck"
			startUpdateCheck()
		else:
			print "[GithubPluginUpdater] wakeup from standby - AutoUpdateCheck not activated"
		
	except:
		import traceback
		traceback.print_exc()


def standbyCounterChanged(configElement):
	
	print "[GithubPluginUpdater] go to standby..."
	from Screens.Standby import inStandby
	inStandby.onClose.append(leaveStandby)


def sessionstart(reason, **kwargs):
	global session
	global updateTimer
	global updateTimer_conn
	
	if kwargs.has_key("session") and reason == 0:
		session = kwargs["session"]
		#print "=====[GithubPluginUpdater] sessionstart....", session
		#== add to set function at restart from standby
		config.misc.standbyCounter.addNotifier(standbyCounterChanged, initial_call = False)
		
		print "[GithubPluginUpdater] runUpdateCheck in sessionstart - after 5 seconds...."
		if config.plugins.githubpluginupdater.enable_autocheck.value != "False":
			updateTimer = eTimer()
			
			if isDreamOS:
				updateTimer_conn = updateTimer.timeout.connect(startUpdateCheck)
			else:
				updateTimer.callback.append(startUpdateCheck)
			#start 5 seconds after boxstart if could check later for start to idle if use elektro-plugin
			updateTimer.start(5*1000)
	else:
		print "[GithubPluginUpdater] sessionstart ohne session...."
		pass

def startUpdateCheck():
	global session
	global updateTimer
	global updateTimer_conn
	
	if isinstance(updateTimer, eTimer):
		#print "=====[GithubPluginUpdater] startUpdateCheck with eTimer"
		if isDreamOS:
			updateTimer_conn = None
		else:
			updateTimer.callback.remove(startUpdateCheck)
	else:
		#print "=====[GithubPluginUpdater] startUpdateCheck without eTimer"
		pass
	updateTimer = None
	
	if Screens.Standby.inStandby:
		print "[GithubPluginUpdater] inStandby - don't check for updates"
		return
	
	#check for next interval
	if config.plugins.githubpluginupdater.autoCheck_interval.value != "0":
		lastcheck = int(config.plugins.githubpluginupdater.lastAutoCheck.value)
		
		#calculate the time for next updateCheck
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
		else:
			next_month = datetime.fromtimestamp(lastcheck).replace(day=28) + timedelta(days=4)  # goto next month
			nextcheck = next_month.replace(day=datetime.fromtimestamp(lastcheck).day) # reset day in the next month date
		
		if datetime.now() < nextcheck: #no AutoUpdateCheck - wait for next interval
			print "[GithubPluginUpdater] don't startUpdateCheck, wait for next interval:", nextcheck
			return
	
	print "[GithubPluginUpdater] startUpdateCheck ...."
	if reload_value:
		reload(AutoUpdateCheck)
	from AutoUpdateCheck import startAutoUpdate as checkupdate
	checkupdate(session)

def main(session, **kwargs):

	if reload_value:
		reload(GithubPluginUpdater)
	try:
		from GithubPluginUpdater import UpdateScreen
		session.open(UpdateScreen)

	except:
		import traceback
		traceback.print_exc()

def Plugins(**kwargs):

	descriptors = []
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("update github-versions")+ " (" + VERSION + ")", where = PluginDescriptor.WHERE_SESSIONSTART, fnc=sessionstart) )
	descriptors.append( PluginDescriptor(name =_("GithubPluginUpdater"), description=_("update github-versions")+ " (" + VERSION + ")", where=[ PluginDescriptor.WHERE_EXTENSIONSMENU, PluginDescriptor.WHERE_PLUGINMENU ], fnc = main, needsRestart = False, icon = "GithubPluginUpdater.png") )

	return descriptors

