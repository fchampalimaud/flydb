from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget
from flydb.models import Fly

from .fly_form import FlyForm


class FlyApp(ModelAdminWidget):

    UID = "flydb"
    MODEL = Fly

    TITLE = "Flies"

    EDITFORM_CLASS = FlyForm

    LIST_DISPLAY = [
        "internal_id",
        "specie",
        "genotype",
        "legacysource",
        "legacy",
        "location",
    ]

    LIST_FILTER = ["legacysource__legacysource_name", "specie", "died"]

    SEARCH_FIELDS = [
        "internal_id__icontains",
        "legacy1__icontains",
        "legacy2__icontains",
        "legacy3__icontains",
        "genotype__icontains",
        "location__icontains",
        "comments__icontains",
    ]

    READ_ONLY = ["entrydate", "updated", "genotype"]

    USE_DETAILS_TO_EDIT = False

    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = "left"
    ORQUESTRA_MENU_ORDER = 1
    ORQUESTRA_MENU_ICON = "bug red"

    @classmethod
    def has_permissions(cls, user):
        if user.is_superuser:
            return True

        if user.memberships.filter(
                group__accesses__animaldb=cls.MODEL._meta.app_label
        ).exists():
            return True

        return False
