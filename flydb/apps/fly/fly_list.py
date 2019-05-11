from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from flydb.models import Fly

from .fly_form import FlyFormApp


class FlyAdminApp(ModelAdminWidget):
    UID = 'fly-app'
    MODEL = Fly

    TITLE = 'Flies'

    LIST_DISPLAY = ['internal_id', 'specie', 'genotype', 'legacysource', 'legacy', 'lab', 'location']
    READ_ONLY    = ['entrydate', 'updated', 'genotype']
    LIST_FILTER  = ['legacysource__legacysource_name', 'specie', 'died', 'lab']

    SEARCH_FIELDS = [
        'internal_id__icontains', 'legacy1__icontains', 'legacy2__icontains', 'legacy3__icontains',
        'genotype__icontains', 'location__icontains',
        'comments__icontains'
    ]

    EDITFORM_CLASS = FlyFormApp

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'bug red'
    ########################################################
