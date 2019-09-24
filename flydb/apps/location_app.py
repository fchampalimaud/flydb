from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Location


class LocationAdminApp(ModelAdminWidget):

    UID = "flydb-Location-app".lower()
    MODEL = Location

    TITLE = "Cares"

    LIST_DISPLAY = ["location_name"]

    # list of filters fields
    # LIST_FILTER    = ['fly','location_id','location_name']

    # list of fields to display in the table
    LIST_DISPLAY = ["location_name"]

    # fields to be used in the search
    SEARCH_FIELDS = ["location_name__icontains"]

    # sub models to show in the interface
    # INLINES        = []

    # formset of the edit form
    FIELDSETS = ["location_name"]

    # read only fields
    # READ_ONLY      = ['fly','location_id','location_name']

    # EDITFORM_CLASS = LocationModelFormWidget    #edit form class
    # CONTROL_LIST   = ControlQueryList #Control to be used in to list the values

    # AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left>FlyAdminApp"
    ORQUESTRA_MENU_ORDER = 4
    ORQUESTRA_MENU_ICON = "h square blue"
    ########################################################
