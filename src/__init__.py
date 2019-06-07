# -*- coding: utf-8 -*-

from Components.config import config, ConfigSubsection, ConfigOnOff, ConfigDirectory, ConfigInteger, ConfigNumber, ConfigSelection, ConfigYesNo, ConfigText, ConfigSelectionNumber


#######################################################
# Initialize Configuration
config.plugins.githubpluginupdater = ConfigSubsection()

config.plugins.githubpluginupdater.enable_autocheck 		= ConfigSelection(choices=[("False",_("no")), ("update",_("Info nur bei Updates")), ("True",_("immer"))], default = "False")
config.plugins.githubpluginupdater.popups_timeout 			= ConfigSelectionNumber(0, 20, 1, default = 15)
config.plugins.githubpluginupdater.backup 							= ConfigYesNo(default = False)
config.plugins.githubpluginupdater.backup_path 					= ConfigDirectory(default = "/media/hdd/backup/")
config.plugins.githubpluginupdater.show_warninginfo 		= ConfigYesNo(default = True)
config.plugins.githubpluginupdater.show_updatequestion	= ConfigSelection(choices=[("False",_("no")), ("True",_("yes"))], default = "False")
config.plugins.githubpluginupdater.updatequestion_defaultanswer	= ConfigSelection(choices=[("False",_("no")), ("True",_("yes"))], default = "False")
config.plugins.githubpluginupdater.checkonly_src 		= ConfigYesNo(default = False)
config.plugins.githubpluginupdater.check_type = ConfigSelection(choices=[("normal",_("normale Webseite")), ("commits",_("commits-Liste")), ("api-normal",_("api-Abruf / normale Website")), ("api-commits",_("api-Abruf / commits-Liste"))], default = "normal")
config.plugins.githubpluginupdater.lastAutoCheck = ConfigInteger(default = 0, limits=(0,2000000000))
interval_options=[]
interval_options.append(( "0",_("always")))
interval_options.append(( "1","stündlich"))
interval_options.append(( "2","alle 6 Stunden"))
interval_options.append(( "3","alle 12 Stunden"))
interval_options.append(( "4",_("daily")))
interval_options.append(( "5",_("weekly")))
interval_options.append(( "6",_("monthly")))
config.plugins.githubpluginupdater.autoCheck_interval = ConfigSelection(default = "2", choices=interval_options)

