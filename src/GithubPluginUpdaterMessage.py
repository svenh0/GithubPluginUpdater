from Tools.Notifications import __AddNotification as AddNotification, RemovePopup
from Screens.MessageBox import MessageBox
from Screens.ChoiceBox import ChoiceBox

class MessageBoxGPU(MessageBox):
	def __init__(self, session, text, type = MessageBox.TYPE_YESNO, timeout = -1, close_on_any_key = False, default = True, enable_input = True, msgBoxID = None, windowTitle = None, additionalActionMap=None, title = _("Message")):
		MessageBox.__init__(self, session, text, type, timeout, close_on_any_key, default, enable_input, msgBoxID)
		self.skinName = ["MessageBoxGPU","MessageBox",]
		#print "=== MessageBoxGPU"


class ChoiceBoxGPU(ChoiceBox):
	def __init__(self, session, title = "", list = [], keys = None, selection = 0, skin_name = [], windowTitle = None, allow_cancel = True, titlebartext = _("Input")):
		ChoiceBox.__init__(self, session, title, list, keys, selection, skin_name)
		if isinstance(skin_name, str):
			skin_name = [skin_name]
		self.skinName = skin_name + ["ChoiceBoxGPU", "ChoiceBox"]
		#print "=== ChoiceBoxGPU"


def AddPopupGPU(text, type, timeout, id = None, domain = None, screen=MessageBoxGPU, additionalActionMap=None):
	#print "=== AddPopupGPU"
	if id is not None:
		RemovePopup(id)
	print "AddPopup, id =", id, "domain =", domain
	AddNotification(None, screen, id, text = text, type = type, timeout = timeout, close_on_any_key = True)


