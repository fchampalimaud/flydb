from confapp import conf
from pyforms_web.organizers import segment
from pyforms_web.widgets.django import ModelFormWidget

from flydb.models import Stock


class StockFormApp(ModelFormWidget):
    UID = 'stock-edit-app'
    MODEL = Stock

    TITLE = 'Stocks edit'

    READ_ONLY = ['stock_entrydate', 'stock_updated', 'stock_genotype']

    FIELDSETS = [
        segment(
            ('stock_ccuid', 'specie', 'stock_entrydate', 'stock_updated'),
            ('legacysource', 'stock_legacy1', 'stock_legacy2', 'stock_legacy3'),
            'lab'
        ),
        'h3:Care',
        segment(
            ('location', 'stock_loc1_location', 'stock_loc2_person', 'stock_loc3_data')
        ),
        'h3:Genotype',
        segment(
            'stock_genotype',
            ('stock_chrx', 'stock_chry', 'stock_bal1'),
            ('stock_chr2', 'stock_bal2'),
            ('stock_chr3', 'stock_bal3'),
            'stock_chr4',
            'stock_chru'
        ),
        segment(
            'stock_print',
            ('stock_hospital', 'stock_died'),
            'stock_comments'
        ),
        'h3:More',
        segment('stock_flydbid')
    ]

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.stock_hospital.label_visible = False
        self.stock_died.label_visible = False

