from confapp import conf
from pyforms_web.organizers import segment, no_columns
from pyforms_web.web.middleware import PyFormsMiddleware
from pyforms_web.widgets.django import ModelFormWidget
from pyforms_web.allcontrols import ControlButton
from django.urls import reverse

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
    <i class="help circle icon"></i>
</a>
"""

FLYBASE_LINK_TAG = """
<a
    href="https://flybase.org/reports/%s.html"
    target="_blank"
>
    <i class="external alternate link
     icon"></i>
</a>
"""


class FlyForm(FormPermissionsMixin, ModelFormWidget):

    CLOSE_ON_REMOVE = True

    INLINES = [HospitalizationAdminApp]

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB

    def __init__(self, *args, **kwargs):

        if kwargs.get('pk'):
            url = reverse('print_barcode', args=[kwargs.get('pk')])
            self._print = ControlButton(
                '<i class="ui icon print"></i>Print',
                default='window.open("{0}", "_blank");'.format(url),
                css="basic blue",
            )

        super().__init__(*args, **kwargs)

        if self.flybase_id.value:
            self.flybase_id.label += FLYBASE_LINK_TAG % self.flybase_id.value

        self.categories.label += BDSC_CATEGORIES_HELP_TAG

        self.public.checkbox_type = ""
        self.public.label_visible = False

        self.died.checkbox_type = ""
        self.died.label_visible = False

        self.origin_obs.style = "height: 4em"
        self.special_husbandry_conditions.style = "height: 4em"

        self.wolbachia.checkbox_type = ""

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
            segment(
                ("species", "flybase_id", "internal_id", "location"),
                "categories",
                no_columns("died"),
                no_columns("public"),
            ),
            segment(
                "h3:Origin",
                # ('legacysource', 'legacy1', 'legacy2', 'legacy3'),
                (
                    "origin",
                    "origin_center",
                    "origin_internal",
                    "origin_external",
                    "origin_id",
                ),
                "origin_obs",
            ),
            segment(
                "h3:Genotype",
                "info:Try to fill in all applicable fields. "
                "If you are not certain of the genetic location, write the full "
                "genotype in the <b>Unknown</b> field below.",
                ("chrx", "chry", "chr2", "chr3", "chr4"),
                ("bal1", " ", "bal2", "bal3", " "),
                "-",
                "chru",
            ),
            segment(
                "h3:Special Care",
                (
                    "wolbachia",
                    "wolbachia_treatment_date",
                    "virus_treatment_date",
                    "isogenization_background",
                ),
                "special_husbandry_conditions",
                "HospitalizationAdminApp",
            ),
            segment(
                "info:You can use the <b>Line description</b> field below to "
                "provide more details. Use the <b>Comments</b> field below for "
                "private notes.",
                ("line_description", "comments"),
            ),
        ]
        if self.object_pk:  # editing existing object
            default.insert(4, segment("h3:Thermal Printer", ("printable_comment", "_print")))
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
