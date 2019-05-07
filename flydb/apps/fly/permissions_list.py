from pyforms_web.widgets.django import ModelAdminWidget
from flydb.models import FlyPermission



class PermissionsListApp(ModelAdminWidget):

    MODEL = FlyPermission
    TITLE = 'Permissions'

    LIST_DISPLAY = ['group', 'viewonly']
    FIELDSETS    = [ ('group', 'viewonly') ]