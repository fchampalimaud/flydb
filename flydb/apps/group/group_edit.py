from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelFormWidget
from django.contrib.auth.models import Group, User
from pyforms.controls import ControlAutoComplete

class GroupEditApp(ModelFormWidget):
    MODEL = Group

    TITLE = 'Group edit'

    FIELDSETS = ['name', '_users']

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_NEW_TAB
    ########################################################

    def __init__(self, *args, **kwargs):
        self._users = ControlAutoComplete(
            'Users',
            queryset=User.objects.all(),
            multiple=True
        )

        super().__init__(*args, **kwargs)

        if self.object_pk is not None:
            self._users.value = [o.pk for o in User.objects.filter(groups=self.model_object)]


    def save_object(self, obj: Group, **kwargs):
        res = super().save_object(obj, **kwargs)

        for pk in self._users.value:
            user = User.objects.get(pk=pk)
            obj.user_set.add(user)
        return res