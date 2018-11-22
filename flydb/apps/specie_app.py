from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Specie

class SpecieAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-Specie-app'.lower()
    MODEL = Specie
    
    TITLE = 'Species'

    LIST_DISPLAY = ['specie_name', 'specie_ncbitax',]
    #list of filters fields
    #LIST_FILTER    = ['stock','specie_id','specie_name','specie_ncbitax']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['stock','specie_id','specie_name','specie_ncbitax']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['stock','specie_id','specie_name','specie_ncbitax']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['stock','specie_id','specie_name','specie_ncbitax']
    
    #read only fields
    #READ_ONLY      = ['stock','specie_id','specie_name','specie_ncbitax']
    
    #EDITFORM_CLASS = SpecieModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>FlyDashboard'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dollar'
    ########################################################
    
    
    