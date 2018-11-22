from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from fly.models import Stock

class StockAdminApp(ModelAdminWidget):
    

    UID   = 'flydb-Stock-app'.lower()
    MODEL = Stock
    
    TITLE = 'Stocks'

    #list of filters fields
    #LIST_FILTER    = ['stock_id','stock_ccuid','stock_entrydate','stock_updated','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2','stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_comments','stock_print','stock_loc3_data','stock_legacy1','stock_legacy2','stock_legacy3','stock_flydbid','stock_hospital','stock_died','stock_genotype','stock_loc1_location','stock_loc2_person','specie','lab','location','legacysource']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['stock_id','stock_ccuid','stock_entrydate','stock_updated','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2','stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_comments','stock_print','stock_loc3_data','stock_legacy1','stock_legacy2','stock_legacy3','stock_flydbid','stock_hospital','stock_died','stock_genotype','stock_loc1_location','stock_loc2_person','specie','lab','location','legacysource']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['stock_id','stock_ccuid','stock_entrydate','stock_updated','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2','stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_comments','stock_print','stock_loc3_data','stock_legacy1','stock_legacy2','stock_legacy3','stock_flydbid','stock_hospital','stock_died','stock_genotype','stock_loc1_location','stock_loc2_person','specie','lab','location','legacysource']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['stock_id','stock_ccuid','stock_entrydate','stock_updated','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2','stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_comments','stock_print','stock_loc3_data','stock_legacy1','stock_legacy2','stock_legacy3','stock_flydbid','stock_hospital','stock_died','stock_genotype','stock_loc1_location','stock_loc2_person','specie','lab','location','legacysource']
    
    #read only fields
    #READ_ONLY      = ['stock_id','stock_ccuid','stock_entrydate','stock_updated','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2','stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_comments','stock_print','stock_loc3_data','stock_legacy1','stock_legacy2','stock_legacy3','stock_flydbid','stock_hospital','stock_died','stock_genotype','stock_loc1_location','stock_loc2_person','specie','lab','location','legacysource']
    
    #EDITFORM_CLASS = StockModelFormWidget    #edit form class
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
    
    
    