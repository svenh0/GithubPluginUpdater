# -*- coding: utf-8 -*-

from Components.config import config, ConfigSubsection, ConfigOnOff, ConfigDirectory, ConfigNumber, ConfigSelection, ConfigYesNo, ConfigText, ConfigSelectionNumber


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