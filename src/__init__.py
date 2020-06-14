# -*- coding: utf-8 -*-

from Components.config import config, ConfigSubsection, ConfigOnOff, ConfigDirectory, ConfigInteger, ConfigNumber, ConfigSelection, ConfigYesNo, ConfigText, ConfigSelectionNumber
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns "language_country" like "de_DE"
	os_environ["LANGUAGE"] = lang
	gettext.bindtextdomain("GithubPluginUpdater", resolveFilename(SCOPE_PLUGINS, "Extensions/GithubPluginUpdater/locale"))

def _(txt):
	if txt:
		t = gettext.dgettext("GithubPluginUpdater", txt)
		if t == txt:
			t = gettext.gettext(txt)
		return t 
	else:
		return ""

localeInit()
language.addCallback(localeInit)

# Initialize Configuration
config.plugins.githubpluginupdater = ConfigSubsection()

config.plugins.githubpluginupdater.enable_autocheck 		= ConfigSelection(choices=[("False",_("no")), ("update",_("Info only on updates")), ("True",_(_("always")))], default = "False")
config.plugins.githubpluginupdater.popups_timeout 			= ConfigSelectionNumber(0, 20, 1, default = 15)
config.plugins.githubpluginupdater.backup 					= ConfigYesNo(default = False)
config.plugins.githubpluginupdater.backup_path 				= ConfigDirectory(default = "/media/hdd/backup/")
config.plugins.githubpluginupdater.show_warninginfo 		= ConfigYesNo(default = True)
config.plugins.githubpluginupdater.show_updatequestion		= ConfigSelection(choices=[("False",_("no")), ("True",_("yes"))], default = "False")
config.plugins.githubpluginupdater.updatequestion_defaultanswer	= ConfigSelection(choices=[("False",_("no")), ("True",_("yes"))], default = "False")
config.plugins.githubpluginupdater.checkonly_src 			= ConfigYesNo(default = False)
config.plugins.githubpluginupdater.check_type = ConfigSelection(choices=[("normal",_("normal website")), ("commits",_("commits-list")), ("api-normal",_("api-call / normal website")), ("api-commits",_("api-call / commits-list"))], default = "normal")
config.plugins.githubpluginupdater.lastAutoCheck = ConfigInteger(default = 0, limits=(0,2000000000))
interval_options=[]
interval_options.append(( "0",_("always")))
interval_options.append(( "1",_("hourly")))
interval_options.append(( "2",_("every 6 hours")))
interval_options.append(( "3",_("every 12 hours")))
interval_options.append(( "4",_("daily")))
interval_options.append(( "5",_("weekly")))
interval_options.append(( "6",_("monthly")))
config.plugins.githubpluginupdater.autoCheck_interval = ConfigSelection(default = "2", choices=interval_options)

