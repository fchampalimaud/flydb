from confapp import conf
from pyforms_web.organizers import segment, no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.allcontrols import ControlButton

# from flydb.models import Fly
from .hospitalization import HospitalizationAdminApp

from users.apps._utils import FormPermissionsMixin
from users.apps._utils import limit_choices_to_database
# FIXME import this when users model is not present

# FIXME pyforms now supports help_text
# transform this into a link, change icon to external ref
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


class FlyForm(FormPermissionsMixin, ModelFormWidget):

    CLOSE_ON_REMOVE = True

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

        self.died.checkbox_type = ""
        self.died.label_visible = False
        self.died.label = "Stock is dead"

        self.origin_obs.style = "height: 4em"
        # self.special_husbandry_conditions.style = "height: 4em"

        self.wolbachia.checkbox_type = ""

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

        self.__on_origin()

    @property
    def title(self):
        try:
            return str(self.model_object)  # FIXME use internal_id or something
        except AttributeError:
            pass  # apparently it defaults to App TITLE

    def get_fieldsets(self, default):
        default = [
            {
                "1:<i class='file alternate outline icon'></i>General": [
                        ("species", "flybase_id", "internal_id", 'location'),
                        "categories",
                        no_columns("died"),
                        no_columns("public"),
                ],
                "2:<i class='dna icon'></i>Genotype": [
                    "info:Try to fill in all applicable fields. "
                    "If you are not certain of the genetic location, write the full "
                    "genotype in the <b>Unknown</b> field below.",
                    ("chrx", "chry", "chr2", "chr3", "chr4"),
                    ("bal1", " ", "bal2", "bal3", " "),
                    "-",
                    "chru",
                ],
                "3:<i class='home icon'></i>Origin": [
                    # ('legacysource', 'legacy1', 'legacy2', 'legacy3'),
                    ("origin", "origin_center", "origin_internal", "origin_external", "origin_id"),
                    "origin_obs",
                ],
                "4:<i class='plus square icon'></i>Special Care": [
                    ('wolbachia', 'wolbachia_treatment_date', 'virus_treatment_date', 'isogenization_background'),
                    "special_husbandry_conditions",
                    'HospitalizationAdminApp',
                ],
                "5:<i class='print icon'></i>Thermal Printer": [('printable_comment', "_print"),],
            },
            segment(
                "info:You can use the <b>Line description</b> field below to "
                "provide more details. Use the <b>Comments</b> field below for "
                "private notes.",
                ("line_description", "comments"),
            ),
        ]
        if self.object_pk:  # editing existing object
            default += [("maintainer", "ownership", "created", "modified")]

        return default

    def get_related_field_queryset(self, field, queryset):
        animaldb = self.model._meta.app_label
        queryset = limit_choices_to_database(animaldb, field, queryset)
        return queryset

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
