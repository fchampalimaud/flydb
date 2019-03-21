from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelFormWidget
from django.contrib.auth.models import Group, User
from pyforms.controls import ControlAutoComplete

class GroupCreateApp(ModelFormWidget):
    MODEL = Group

    TITLE = 'Group create'

    FIELDSETS = ['name']

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
