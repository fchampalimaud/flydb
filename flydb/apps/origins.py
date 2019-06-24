from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from flydb.models import Origin


class FlyOriginForm(ModelFormWidget):

    FIELDSETS = [("category", "source", "previous_id")]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW


class FlyOriginApp(ModelAdminWidget):

    UID = 'fly-origins'
    MODEL = Origin

    TITLE = 'Origins'

    EDITFORM_CLASS = FlyOriginForm

    LIST_DISPLAY = ["category", "source", "previous_id"]

    USE_DETAILS_TO_ADD = False  # required to have form in NEW_TAB
    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left>FlyApp'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'cog'

    # FIXME the following restriction is not needed if this is to be
    # used as an inline only

    # @classmethod
    # def has_permissions(cls, user):
    #     if user.is_superuser:
    #         return True
    #     return False
