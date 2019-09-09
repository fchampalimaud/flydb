from confapp import conf
from django.contrib.auth.models import User
from pyforms_web.web.middleware import PyFormsMiddleware

# from notifications.tools import notify
from pyforms_web.widgets.django import ModelAdminWidget
from pyforms_web.widgets.django import ModelFormWidget
from flydb.models import Hospitalization
from django.utils import timezone
import dateutil.relativedelta


class HospiForm(ModelFormWidget):

    LAYOUT_POSITION = conf.ORQUESTRA_NEW_WINDOW

    def save_form_event(self, obj):
        res = super().save_form_event(obj)

        now = timezone.now()
        months_ago = now.date() - dateutil.relativedelta.relativedelta(months=6)
        queryset = Hospitalization.objects.filter(
            fly=obj.fly, start_date__gte=months_ago
        )
        if queryset.count() > 3:
            msg = (
                f"The fly [{obj.fly}], had more than 3 hospitalizations in the last 6 months.",
            )
            title = "To many hospitalizations in the last 6 months."
            self.parent.warning(msg, title)

            # FIXME enable notification
            # for user in User.objects.filter(is_superuser=True):
            #     notify(title, msg, user=user)

        return res


class HospitalizationAdminApp(ModelAdminWidget):

    MODEL = Hospitalization

    LIST_DISPLAY = ["start_date", "end_date"]

    LIST_HEADERS = ["Start date", "End date"]

    FIELDSETS = [("start_date", "end_date")]

    EDITFORM_CLASS = HospiForm

    USE_DETAILS_TO_ADD = False
    USE_DETAILS_TO_EDIT = False
