from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget

from flydb.models import Species


class FlySpeciesForm(ModelFormWidget):

    FIELDSETS = [("specie_name", "specie_ncbitax")]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW


class FlySpeciesApp(ModelAdminWidget):

    UID = 'fly-species'
    MODEL = Species

    TITLE = 'Species'

    EDITFORM_CLASS = FlySpeciesForm

    # LIST_DISPLAY = ["specie_name", "specie_ncbitax"]

    USE_DETAILS_TO_ADD = False  # required to have form in NEW_TAB
    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left>FlyApp'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'cog'

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser or user.is_admin(cls.MODEL._meta.app_label):
            return True
        return False
