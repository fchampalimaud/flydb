from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .models import Fly
import simplejson, datetime, socket, sys

from flydb.admin import FlyResource
import csv
from django.http import HttpResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

@login_required
def get_fly_template(request):
    fly_resource = FlyResource()
    dataset = fly_resource.export()
    
    # prepare response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fly_template.csv"'

    if dataset.csv:
        header = dataset.csv.splitlines()
        if len(header) > 0:
            csv_list = header[0].split(',')
            writer = csv.writer(response)
            writer.writerow(csv_list)

    return response

@login_required
def print_barcode(request, fly_url):
    stock = Fly.objects.get(pk=fly_url)
    now = datetime.datetime.now()

    if stock.location != None:
        location = stock.location
    else:
        location = ""

    message = "%d|%s|%s|%s|%s|%s|%s|%s" % (
        stock.id,
        stock.internal_id,
        stock.ownership,
        stock.get_genotype(),
        now.strftime("%Y-%m-%d"),
        stock.printable_comment,
        location,
        stock.origin_id,
    )

    HOST = get_client_ip(request)
    PORT = settings.PRINTER_SERVER_PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    s.send(message)
    s.close()

    return HttpResponse('<script type="text/javascript">window.close()</script>') 


@login_required
def findstock(request, barcode):

    try:
        stock = Fly.objects.get(ccuid=barcode)
        if request.POST.get("autoprint", "off") == "on":
            print_barcode(request, stock.id, False)
        resp = {
            "result": "found",
            "id": stock.id,
            "ccu": stock.ccuid,
            "genotype": str(stock.genotype()).encode("ascii", "xmlcharrefreplace"),
        }
    except ObjectDoesNotExist:
        resp = {"result": "notfound"}
    except:
        resp = {"result": ("Unexpected error: " + str(sys.exc_info()))}

    return HttpResponse(simplejson.dumps(resp), mimetype="application/json")


# Flip by location
@login_required
def flipbylocation(request, loc):

    try:
        stock = Fly.objects.get(loc1_location=loc)
        stock.save()
        resp = {"result": "ok", "location": loc}
    except ObjectDoesNotExist:
        resp = {"result": "notfound"}

    return HttpResponse(simplejson.dumps(resp), mimetype="application/json")
