from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Hospitalization


class HospitalizationAdminApp(ModelAdminWidget):


    MODEL = Hospitalization

    TITLE = 'Hospitalization'

    LIST_DISPLAY = ['begin', 'end']

    # formset of the edit form
    FIELDSETS = [
        ('begin', 'end')
    ]

    # AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    #LAYOUT_POSITION = conf.ORQUESTRA_HOME
    #ORQUESTRA_MENU = 'left'
    #ORQUESTRA_MENU_ORDER = 7
    #ORQUESTRA_MENU_ICON = 'tags green'
    ########################################################


