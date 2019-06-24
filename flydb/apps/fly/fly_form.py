from confapp import conf
from pyforms_web.organizers import segment, no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.allcontrols import ControlButton, ControlText

# from flydb.models import Fly
from .hospitalization import HospitalizationAdminApp


class FlyForm(ModelFormWidget):

    READ_ONLY = ['created', 'modified']

    INLINES = [
        HospitalizationAdminApp,
    ]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):

        self._set_genotype = ControlButton(
            'Update genotype',
            default=self.__update_genotype_evt,
            css='basic blue'
        )
        self._new_genotype = ControlText('New genotype', visible=False)

        self._print = ControlButton(
            'Print',
            default=None,
            css='basic blue',
        )

        super().__init__(*args, **kwargs)

        self.public.checkbox_type = ""
        self.public.label_visible = False
        self.public.label = "Share with Congento network"

        self.died.checkbox_type = ""
        self.died.label_visible = False
        self.died.label = "Stock is dead"

        # self.wolbachia.label_visible = False
        # self.virus_treatment.label_visible = False
        # self.isogenization.label_visible = False

        self.wolbachia_treatment.checkbox_type = ""

        # FIXME change these in the model verbose name
        self.chrx.label = "Chromosome X"
        self.chry.label = "Chromosome Y"
        self.bal1.label = "Balancer 1"
        self.chr2.label = "Chromosome 2"
        self.bal2.label = "Balancer 2"
        self.chr3.label = "Chromosome 3"
        self.bal3.label = "Balancer 3"
        self.chr4.label = "Chromosome 4"
        self.chru.label = "Unknown"


        self.wolbachia.changed_event = self.__wolbachia_changed_evt
        self.isogenization.changed_event = self.__isogenization_changed_evt
        self.virus_treatment.changed_event = self.__virus_treatment_changed_evt

        self.__isogenization_changed_evt()
        self.__wolbachia_changed_evt()
        self.__virus_treatment_changed_evt()

    @property
    def title(self):
        try:
            return str(self.model_object)  # FIXME use internal_id or something
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def get_fieldsets(self, default):
        user = PyFormsMiddleware.user()

        default = [
            segment(
                ("species", "category", "internal_id", 'location'),
                no_columns("died"),
                no_columns("public"),
            ),
            'h3:Genotype',
            segment(
                # no_columns('_new_genotype', '_set_genotype'),
                ('chrx', 'chry', 'bal1'),
                ('chr2', 'bal2'),
                ('chr3', 'bal3'),
                'chr4',
                'chru',
            ),
            "h3:Extra Info",
            segment(
                ('wolbachia', 'wolbachia_test_date', 'wolbachia_treatment', 'wolbachia_strain'),
                ('virus_treatment', 'virus_treatment_date', ' ', ' '),
                ('isogenization', 'background', 'generations', ' '),
                ' ',
                'HospitalizationAdminApp',
            ),
            'h3:Previous IDs',
            segment(
                ('legacysource', 'legacy1', 'legacy2', 'legacy3')
            ),
            'h3:Thermal Printer',
            segment(
                ('printable_comment', "_print"),
            ),
            segment(
                "info:You can use the <b>Line description</b> field below to "
                "provide more details. Use the <b>Comments</b> field below for "
                "private notes.",
                ("line_description", "comments"),
            ),
        ]

        if user.is_superuser:
            default += [
                segment(
                    ("maintainer", "ownership"),
                    ("created", "modified"),
                )
            ]

        return default

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
            self.wolbachia_test_date.show()
            self.wolbachia_treatment.show()
            self.wolbachia_strain.show()
        else:
            self.wolbachia_test_date.hide()
            self.wolbachia_treatment.hide()
            self.wolbachia_strain.hide()

    def __virus_treatment_changed_evt(self):
        if self.virus_treatment.value:
            self.virus_treatment_date.show()
        else:
            self.virus_treatment_date.hide()

    def __isogenization_changed_evt(self):
        if self.isogenization.value:
            self.background.show()
            self.generations.show()
        else:
            self.background.hide()
            self.generations.hide()
