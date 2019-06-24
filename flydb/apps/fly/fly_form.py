from confapp import conf
from pyforms_web.organizers import segment, no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.allcontrols import ControlButton, ControlText

# from flydb.models import Fly
from .hospitalization import HospitalizationAdminApp
# from .permissions_list import PermissionsListApp


class FlyForm(ModelFormWidget):

    FIELDSETS = [
        'public',
        ('internal_id', 'category', 'location'),
        segment(
            ('wolbachia','last_test', 'treatment', 'strain'),
            ('virus_treatment', 'last_treatment', ' ', ' '),
            ('isogenization', 'background', 'generations', ' '),
            'died',
            ' ',
            'HospitalizationAdminApp',
        ),
        'h3:Previous IDs',
        segment(
            ('legacysource', 'legacy1', 'legacy2', 'legacy3')
        ),
        'h3:Genotype',
        segment(
            'species',
            # no_columns('_new_genotype', '_set_genotype'),
            ('chrx', 'chry', 'bal1'),
            ('chr2', 'bal2'),
            ('chr3', 'bal3'),
            'chr4',
            'chru'
        ),
        'print',
        'comments',
        # ('responsible', 'lab'),
        # 'PermissionsListApp'
    ]

    READ_ONLY = ['entrydate', 'updated', 'genotype']

    INLINES = [
        HospitalizationAdminApp,
        # PermissionsListApp,
    ]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):

        self._set_genotype = ControlButton(
            'Update genotype',
            default=self.__update_genotype_evt,
            css='basic blue'
        )
        self._new_genotype = ControlText('New genotype', visible=False)

        super().__init__(*args, **kwargs)

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

    def set_genotype(self, genotype_txt):
        """
        Update the genotype fields from the full genotype label
        :param genotype_txt:
        :return:
        """
        raise Exception('Wrong genotype')

    def __update_genotype_evt(self):
        if self._new_genotype.visible:
            if self._new_genotype.value:
                try:
                    self.set_genotype(self._new_genotype.value)
                    self._new_genotype.hide()
                except Exception as e:
                    self.alert(str(e), 'Error parsing genotype text')
                    self._new_genotype.value = ''
        else:
            self._new_genotype.show()

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

    @property
    def title(self):
        try:
            return str(self.model_object)  # FIXME use internal_id or something
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def get_fieldsets(self, default):
        # user = PyFormsMiddleware.user()
        # if user.is_superuser:
        #     default += [("responsible", "lab"),]
        return default
