from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Specie

class SpecieAdminApp(ModelAdminWidget):


    UID   = 'flydb-Specie-app'.lower()
    MODEL = Specie

    TITLE = 'Species'

    LIST_DISPLAY = ['specie_name', 'specie_ncbitax',]
    #list of filters fields
    #LIST_FILTER    = ['fly','specie_id','specie_name','specie_ncbitax']

    #list of fields to display in the table
    LIST_DISPLAY   = ['specie_name','specie_ncbitax']

    #fields to be used in the search
    SEARCH_FIELDS  = ['specie_name__icontains','specie_ncbitax__icontains']

    #sub models to show in the interface
    #INLINES        = []

    #formset of the edit form
    FIELDSETS      = [('specie_name','specie_ncbitax')]

    #read only fields
    #READ_ONLY      = ['fly','specie_id','specie_name','specie_ncbitax']

    #EDITFORM_CLASS = SpecieModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values

    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>FlyAdminApp'
    ORQUESTRA_MENU_ORDER = 2
    ORQUESTRA_MENU_ICON  = 'dna olive'
    ########################################################


