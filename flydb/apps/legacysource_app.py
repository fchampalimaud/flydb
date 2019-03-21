from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import LegacySource

class LegacySourceAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-LegacySource-app'.lower()
    MODEL = LegacySource
    
    TITLE = 'Legacy Sources'

    LIST_DISPLAY = ['legacysource_name']

    #list of filters fields
    #LIST_FILTER    = ['legacysource_name']

    #list of fields to display in the table
    LIST_DISPLAY   = ['legacysource_name']
    
    #fields to be used in the search
    SEARCH_FIELDS  = ['legacysource_name__icontains']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    FIELDSETS      = ['legacysource_name']
    
    #read only fields
    #READ_ONLY      = ['stock','legacysource_id','legacysource_name']
    
    #EDITFORM_CLASS = LegacySourceModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>StockAdminApp'
    ORQUESTRA_MENU_ORDER = 6
    ORQUESTRA_MENU_ICON  = 'map signs yellow'
    ########################################################
    
    
    