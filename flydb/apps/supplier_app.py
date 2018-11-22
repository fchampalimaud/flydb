from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Supplier

class SupplierAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-Supplier-app'.lower()
    MODEL = Supplier
    
    TITLE = 'Suppliers'

    LIST_DISPLAY = ['supplier_name', 'supplier_contact', 'supplier_email', 'supplier_url']

    #list of filters fields
    #LIST_FILTER    = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']
    
    #read only fields
    #READ_ONLY      = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']
    
    #EDITFORM_CLASS = SupplierModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>LegacySourceAdminApp'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dollar'
    ########################################################
    
    
    