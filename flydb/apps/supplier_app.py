from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget

from flydb.models import Supplier

class SupplierAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-Supplier-app'.lower()
    MODEL = Supplier
    
    TITLE = 'Suppliers'

    LIST_DISPLAY = ['supplier_name', 'supplier_contact', 'supplier_email']

    #fields to be used in the search
    SEARCH_FIELDS  = ['supplier_name__icontains','supplier_contact__icontains','supplier_email__icontains']
    
    #formset of the edit form
    FIELDSETS      = [
        'supplier_name',
        segment('supplier_notes'),
        'h2:Details',
        segment(
            ('supplier_contact','supplier_email'),
            'supplier_url',
            'supplier_address',
        )
    ]
    
    #read only fields
    #READ_ONLY      = ['supplier_id','supplier_name','supplier_contact','supplier_email','supplier_url','supplier_address','supplier_notes']
    
    #EDITFORM_CLASS = SupplierModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'left>StockAdminApp'
    ORQUESTRA_MENU_ORDER = 3
    ORQUESTRA_MENU_ICON  = 'truck Brown'
    ########################################################
    
    
    