from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlCheckBox
from pyforms.controls import ControlButton
from confapp import conf
from pyforms_web.organizers import segment


class FlyDashboard(BaseWidget):

    UID = "fly-dashboard-app"
    TITLE = "Dashboard"

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left"
    ORQUESTRA_MENU_ICON = "clipboard outline"
    ORQUESTRA_MENU_ORDER = 0
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._code = ControlText("Code", on_enter_event=self.__find_btn_evt)
        self._print = ControlCheckBox("Send to printer", label_visible=False)
        self._findbtn = ControlButton(
            "Find", label_visible=False, default=self.__find_btn_evt
        )

        self.formset = [(segment("_print", "_code", "_findbtn"), " ")]

    def __find_btn_evt(self):
        pass
