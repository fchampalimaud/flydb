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


    def save_form_event(self, obj):
        res = super().save_form_event(obj)

        now = timezone.now()
        months_ago = now.date() - dateutil.relativedelta.relativedelta(months=6)
        queryset = Hospitalization.objects.filter(fly=obj.fly, begin__gte=months_ago)
        if queryset.count()>3:
            msg = f'The fly [{obj.fly}], had more than 3 hospitalizations in the last 6 months.',
            title = 'To many hospitalizations in the last 6 months.'
            self.parent.warning( msg, title )

            # for user in User.objects.filter(is_superuser=True):
            #     notify(title, msg, user=user)

        return res


class HospitalizationAdminApp(ModelAdminWidget):


    MODEL = Hospitalization

    TITLE = 'Special Care'

    LIST_DISPLAY = ['begin', 'end']

    # formset of the edit form
    FIELDSETS = [
        ('begin', 'end')
    ]

    LIST_HEADERS = ['Begin', 'End']

    # AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app

    EDITFORM_CLASS = HospiForm

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    #LAYOUT_POSITION = conf.ORQUESTRA_HOME
    #ORQUESTRA_MENU = 'left'
    #ORQUESTRA_MENU_ORDER = 7
    #ORQUESTRA_MENU_ICON = 'tags green'
    ########################################################


