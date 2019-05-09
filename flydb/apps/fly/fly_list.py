from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from flydb.models import Fly

from .fly_form import FlyFormApp


class FlyAdminApp(ModelAdminWidget):
    UID = 'fly-app'
    MODEL = Fly

    TITLE = 'Flies'

    LIST_DISPLAY = ['ccuid', 'specie', 'genotype', 'legacysource', 'legacy', 'lab']
    READ_ONLY    = ['entrydate', 'updated', 'genotype']
    LIST_FILTER  = ['legacysource__legacysource_name', 'specie', 'hospital', 'died', 'lab', 'location']

    SEARCH_FIELDS = [
        'ccuid', 'legacy1', 'legacy2', 'legacy3',
        'genotype', 'chrx', 'chry', 'bal1', 'chr2', 'bal2',
        'chr3', 'bal3', 'chr4', 'chru', 'loc1_location', 'loc3_data',
        'comments'
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
