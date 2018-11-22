from django.core.management import setup_environ
import settings
setup_environ(settings)
from fly.models import *

#Update stocks
stocks = Stock.objects.all()
for stock in stocks:
    try:
        stock.save()
    except:
	print stock.stock_id
        raise


#Update copies
copies = Copy.objects.all()
for copy in copies:
    copy.save()
