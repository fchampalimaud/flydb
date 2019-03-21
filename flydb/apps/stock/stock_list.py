from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Stock

from .stock_form import StockFormApp


class StockAdminApp(ModelAdminWidget):
    UID = 'stock-app'
    MODEL = Stock

    TITLE = 'Flies'

    LIST_DISPLAY = ['stock_ccuid', 'specie', 'stock_genotype', 'legacysource', 'legacy', 'lab']
    READ_ONLY = ['stock_entrydate', 'stock_updated', 'stock_genotype']
    LIST_FILTER = ['legacysource__legacysource_name', 'specie', 'stock_hospital', 'stock_died', 'lab', 'location']

    SEARCH_FIELDS = ['stock_ccuid', 'stock_legacy1', 'stock_legacy2', 'stock_legacy3',
                     'stock_genotype', 'stock_chrx', 'stock_chry', 'stock_bal1', 'stock_chr2', 'stock_bal2',
                     'stock_chr3', 'stock_bal3', 'stock_chr4', 'stock_chru', 'stock_loc1_location', 'stock_loc3_data',
                     'stock_comments']

    EDITFORM_CLASS = StockFormApp

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'bug'

    ########################################################
