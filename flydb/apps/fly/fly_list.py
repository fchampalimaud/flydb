import os
from os.path import dirname
import shutil
import logging

from confapp import conf
from pyforms_web.basewidget import BaseWidget
from pyforms_web.organizers import no_columns, segment
from pyforms.controls import ControlCheckBox, ControlFileUpload, ControlButton
from pyforms_web.widgets.django import ModelAdminWidget
from tablib.core import Dataset, UnsupportedFormat

from flydb.models import Fly
from flydb.admin import FlyResource

from .fly_form import FlyForm

# FIXME fix this import when users model is not present
from users.apps._utils import limit_choices_to_database

from django.urls import reverse


logger = logging.getLogger(__name__)


class FlyImportWidget(BaseWidget):
    TITLE = "Import Fly"

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW
    CREATE_BTN_LABEL = '<i class="upload icon"></i>Import'
    HAS_CANCEL_BTN_ON_ADD = False

    def __init__(self, *args, **kwargs):
        super().__init__()

        self._csv_file = ControlFileUpload(label="Import CSV")
        self._import_btn = ControlButton(
            '<i class="upload icon"></i>Import',
            default=self.__import_evt,
            label_visible=False,
            css="basic blue",
            helptext="Import Fly from CSV file",
        )

        self.formset = ["_csv_file", "_import_btn"]

    def __import_evt(self):

        fly_resource = FlyResource()

        if self._csv_file.filepath is not None:
            dataset = Dataset()

            try:
                with open(self._csv_file.filepath, "r") as f:
                    imported_file = dataset.load(f.read())
            except UnsupportedFormat as uf:
                raise Exception(
                    "Unsupported format. Please select a CSV file with the Fly template columns"
                )
            finally:
                shutil.rmtree(dirname(self._csv_file.filepath))

            # Test the import first
            result = fly_resource.import_data(
                dataset, dry_run=True, use_transactions=True, collect_failed_rows=True
            )
            if result.has_validation_errors():
                val_errors = ""
                for err in result.invalid_rows:
                    val_errors += f"row {err.number}:<br><ul>"
                    for key in err.field_specific_errors:
                        val_errors += (
                            f"<li>{key} &rarr; {err.field_specific_errors[key][0]}</li>"
                        )
                    for val in err.non_field_specific_errors:
                        val_errors += f"<li>Non field specific &rarr; {val}</li>"
                    val_errors += "</ul>"
                raise Exception(
                    f"Validation error(s) on row(s): {', '.join([str(err.number) for err in result.invalid_rows])} <br>{val_errors}"
                )
            elif result.has_errors():
                msg = f'ERRORS: '.join([
                    ''.join([
                        f'row: {str(err.row["internal_id"])}, ownership: {str(err.row["ownership"])}, error: {str(err.error)}\n'
                        for err in err_lst
                    ])
                    for _, err_lst in result.row_errors()
                ])
                logger.error(msg)
                raise Exception(
                    f"Error detected that prevents importing on row(s): {', '.join([str(num) for num, _ in result.row_errors()])}"
                )
            else:
                fly_resource.import_data(dataset, dry_run=False, use_transactions=True)

            self.success("Fly file imported successfully!")


class FlyApp(ModelAdminWidget):

    UID = "flydb"
    MODEL = Fly

    TITLE = "Flies"

    EDITFORM_CLASS = FlyForm

    LIST_DISPLAY = [
        "get_stock_id",
        "species",
        "genotype",
        "origin",
        "origin_id",
        "ownership",
    ]

    LIST_FILTER = [
        "species",
        "categories",
        "origin",
        # "wolbachia",
        # "virus_treatment",
        # "isogenization",
        # "died",
        "public",
        # "ownership",
    ]

    SEARCH_FIELDS = [
        "internal_id__icontains",
        "legacy1__icontains",
        "legacy2__icontains",
        "legacy3__icontains",
        "genotype__icontains",
        "location__icontains",
        "comments__icontains",
    ]

    USE_DETAILS_TO_EDIT = False  # required to have form in NEW_TAB

    STATIC_FILES = ["flydb/icon.css"]  # required for the menu icon CSS

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left"
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = "large congento-fly"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        if user.memberships.filter(
            group__accesses__animaldb=cls.MODEL._meta.app_label
        ).exists():
            return True

        return False

    def __init__(self, *args, **kwargs):

        self._unknown_filter = ControlCheckBox(
            "List only stocks with unknown genotypes",
            default=False,
            label_visible=False,
            changed_event=self.populate_list,
        )

        self._import_btn = ControlButton(
            '<i class="upload icon"></i>Import',
            default=self.__import_evt,
            label_visible=False,
            css="basic blue",
            helptext="Import Fly from CSV file",
        )

        url = reverse('get_fly_template')

        self._download_btn = ControlButton(
            '<i class="download icon"></i>Template',
            default='window.open("{0}");'.format(url),
            label_visible=False,
            css="basic blue",
            helptext="Download Fly template as a CSV file",
        )

        super().__init__(*args, **kwargs)

    def get_toolbar_buttons(self, has_add_permission=False):
        toolbar = super().get_toolbar_buttons(has_add_permission)
        return tuple([no_columns(toolbar, "_import_btn", "_download_btn")] + [" ", "_unknown_filter"])

    def get_queryset(self, request, qs):
        if self._unknown_filter.value:
            qs = qs.exclude(chru__exact="")

        return qs

    def get_related_field_queryset(self, request, list_queryset, field, queryset):
        animaldb = self.model._meta.app_label
        queryset = limit_choices_to_database(animaldb, field, queryset)
        return queryset

    def __import_evt(self):
        FlyImportWidget(parent_win=self)
