from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Source

class SourceAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-Source-app'.lower()
    MODEL = Source
    
    TITLE = 'Sources'

    LIST_DISPLAY = ['source_name']

    #list of filters fields
    #LIST_FILTER    = ['source_id','source_name']

    #list of fields to display in the table
    LIST_DISPLAY   = ['source_name']
    
    #fields to be used in the search
    SEARCH_FIELDS  = ['source_name__icontains']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    FIELDSETS      = ['source_name']
    
    #read only fields
    #READ_ONLY      = ['source_id','source_name']
    
    #EDITFORM_CLASS = SourceModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>FlyAdminApp'
    ORQUESTRA_MENU_ORDER = 5
    ORQUESTRA_MENU_ICON  = 'map signs orange'
    ########################################################
    
    
    