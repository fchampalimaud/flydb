from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Category


class CategoryAdminApp(ModelAdminWidget):
    UID = 'category-app'
    MODEL = Category

    TITLE = 'Categories'

    LIST_DISPLAY = ['name']

    # fields to be used in the search
    SEARCH_FIELDS = ['name__icontains']

    # formset of the edit form
    FIELDSETS = ['name']

    # AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left>StockAdminApp'
    ORQUESTRA_MENU_ORDER = 7
    ORQUESTRA_MENU_ICON = 'tags green'
    ########################################################


