from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelAdminWidget
from flydb.models import StockPermission



class PermissionsListApp(ModelAdminWidget):

    MODEL = StockPermission
    TITLE = 'Permissions'

    LIST_DISPLAY = ['group', 'viewonly']
    FIELDSETS    = [ ('group', 'viewonly') ]