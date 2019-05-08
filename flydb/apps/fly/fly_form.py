from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelFormWidget

from flydb.models import Fly
from .hospitalization import HospitalizationAdminApp
from .permissions_list import PermissionsListApp

class FlyFormApp(ModelFormWidget):

    UID = 'fly-edit-app'
    MODEL = Fly

    TITLE = 'Fly stock edit'

    INLINES = [HospitalizationAdminApp, PermissionsListApp]

    READ_ONLY = ['entrydate', 'updated', 'genotype']

    FIELDSETS = [
        'public',
        segment(
            ('ccuid', 'specie', 'entrydate', 'updated'),
            ('legacysource', 'legacy1', 'legacy2', 'legacy3'),
            ('lab', 'category')
        ),
        'h3:Care',
        segment(
            ('location', 'loc1_location', 'loc2_person', 'loc3_data')
        ),
        'h3:Genotype',
        segment(
            'genotype',
            ('chrx', 'chry', 'bal1'),
            ('chr2', 'bal2'),
            ('chr3', 'bal3'),
            'chr4',
            'chru'
        ),
        segment(
            'print',
            ('hospital', 'died'),
            'comments'
        ),
        'h3:More',
        segment('flydbid'),
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

        self.hospital.label_visible = False
        self.died.label_visible = False
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
