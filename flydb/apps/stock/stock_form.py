from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelFormWidget

from flydb.models import Stock
from .hospitalization import HospitalizationAdminApp
from .permissions_list import PermissionsListApp

class StockFormApp(ModelFormWidget):

    UID = 'stock-edit-app'
    MODEL = Stock

    TITLE = 'Stocks edit'

    INLINES = [HospitalizationAdminApp, PermissionsListApp]

    READ_ONLY = ['stock_entrydate', 'stock_updated', 'stock_genotype']

    FIELDSETS = [
        segment(
            ('stock_ccuid', 'specie', 'stock_entrydate', 'stock_updated'),
            ('legacysource', 'stock_legacy1', 'stock_legacy2', 'stock_legacy3'),
            ('lab', 'category')
        ),
        'h3:Care',
        segment(
            ('location', 'stock_loc1_location', 'stock_loc2_person', 'stock_loc3_data')
        ),
        'h3:Genotype',
        segment(
            'stock_genotype',
            ('stock_chrx', 'stock_chry', 'stock_bal1'),
            ('stock_chr2', 'stock_bal2'),
            ('stock_chr3', 'stock_bal3'),
            'stock_chr4',
            'stock_chru'
        ),
        segment(
            'stock_print',
            ('stock_hospital', 'stock_died'),
            'stock_comments'
        ),
        'h3:More',
        segment('stock_flydbid'),
        segment(
            'wolbachia',
            ('last_test', 'treatment', 'strain'),
            'virus_treatment',
            ('last_treatment', ' ', ' '),
            'isogenization',
            ('background', 'generations', ' '),
        ),
        'h2:Hospital',
        'HospitalizationAdminApp',
        'PermissionsListApp'
    ]

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stock_hospital.label_visible = False
        self.stock_died.label_visible = False
        self.wolbachia.label_visible = False
        self.virus_treatment.label_visible = False
        self.isogenization.label_visible = False

        self.wolbachia.changed_event = self.__wolbachia_changed_evt
        self.isogenization.changed_event = self.__isogenization_changed_evt
        self.virus_treatment.changed_event = self.__virus_treatment_changed_evt

        self.__isogenization_changed_evt()
        self.__wolbachia_changed_evt()
        self.__virus_treatment_changed_evt()

    def __wolbachia_changed_evt(self):
        if self.wolbachia.value:
            self.last_test.show()
            self.treatment.show()
            self.strain.show()
        else:
            self.last_test.hide()
            self.treatment.hide()
            self.strain.hide()

    def __virus_treatment_changed_evt(self):
        if self.virus_treatment.value:
            self.last_treatment.show()
        else:
            self.last_treatment.hide()

    def __isogenization_changed_evt(self):
        if self.isogenization.value:
            self.background.show()
            self.generations.show()
        else:
            self.background.hide()
            self.generations.hide()
