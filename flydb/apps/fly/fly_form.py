from confapp import conf
from pyforms_web.organizers import segment, no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.allcontrols import ControlButton

# from flydb.models import Fly
from .hospitalization import HospitalizationAdminApp


BDSC_CATEGORIES_HELP_TAG = """
<a
    href="https://bdsc.indiana.edu/stocks/index.html"
    target="_blank"
    data-inverted=""
    data-tooltip="Learn more about BDSC categories"
    data-position="top center"
>
    <i class="help link teal icon"></i>
</a>
"""

FLYBASE_LINK_TAG = """
<a
    href="https://flybase.org/reports/%s.html"
    target="_blank"
>
    <i class="external alternate link teal icon"></i>
</a>
"""


class FlyForm(ModelFormWidget):

    READ_ONLY = ['created', 'modified']

    INLINES = [
        HospitalizationAdminApp,
    ]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):

        self._print = ControlButton(
            'Print',
            default=None,
            css='basic blue',
        )

        super().__init__(*args, **kwargs)

        if self.flybase_id.value:
            self.flybase_id.label += FLYBASE_LINK_TAG % self.flybase_id.value

        self.categories.label += BDSC_CATEGORIES_HELP_TAG

        self.public.checkbox_type = ""
        self.public.label_visible = False
        self.public.label = "Share with Congento network"

        self.died.checkbox_type = ""
        self.died.label_visible = False
        self.died.label = "Stock is dead"

        self.origin_obs.style = "height: 4em"
        # self.special_husbandry_conditions.style = "height: 4em"

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
        self.chru.label = "Unknown genotype"

        self.origin.changed_event = self.__on_origin
        self.wolbachia.changed_event = self.__wolbachia_changed_evt
        self.isogenization.changed_event = self.__isogenization_changed_evt
        self.virus_treatment.changed_event = self.__virus_treatment_changed_evt

        self.__on_origin()
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
                ("species", "flybase_id", "internal_id", 'location'),
                "categories",
                no_columns("died"),
                no_columns("public"),
            ),
            'h3:Genotype',
            segment(
                "info:Try to fill in all applicable fields. "
                "If you are not certain of the genetic location, write the full "
                "genotype in the <b>Unknown</b> field below.",
                ("chrx", "chry", "chr2", "chr3", "chr4"),
                ("bal1", " ", "bal2", "bal3", " "),
                "-",
                "chru",
            ),
            "h3:Extra Info",
            segment(
                ('wolbachia', 'wolbachia_test_date', 'wolbachia_treatment', 'wolbachia_strain'),
                ('virus_treatment', 'virus_treatment_date', ' ', ' '),
                ('isogenization', 'background', 'generations', ' '),
                ' ',
                'HospitalizationAdminApp',
                "special_husbandry_conditions",
            ),
            'h3:Previous IDs',
            segment(
                # ('legacysource', 'legacy1', 'legacy2', 'legacy3'),
                ("origin", "origin_center", "origin_internal", "origin_external", "origin_id"),
                "origin_obs",
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

    def __on_origin(self):
        if self.origin.value == self.model.ORIGINS.center:
            self.origin_center.show()
            self.origin_internal.hide()
            self.origin_external.hide()
        elif self.origin.value == self.model.ORIGINS.internal:
            self.origin_center.hide()
            self.origin_internal.show()
            self.origin_external.hide()
        elif self.origin.value == self.model.ORIGINS.external:
            self.origin_center.hide()
            self.origin_internal.hide()
            self.origin_external.show()
        else:
            raise ValueError("Invalid origin value")

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
