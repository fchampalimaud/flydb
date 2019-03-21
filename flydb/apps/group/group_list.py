from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from .group_create import GroupCreateApp
from .group_edit   import GroupEditApp
from django.contrib.auth.models import Group

class GroupAdminApp(ModelAdminWidget):
    UID = 'group-app'
    MODEL = Group

    TITLE = 'Groups'

    # list of fields to display in the table
    LIST_DISPLAY = ['name']

    # fields to be used in the search
    SEARCH_FIELDS = ['name__icontains']

    USE_DETAILS_TO_EDIT = False
    USE_DETAILS_TO_ADD = False

    EDITFORM_CLASS = GroupEditApp
    #ADDFORM_CLASS  = GroupCreateApp

    # AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = 'users olive'
    ########################################################


