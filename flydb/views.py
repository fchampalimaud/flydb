from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from .models import Fly
import simplejson, datetime, socket, sys

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
    fields = [item.name for item in Fly()._meta.get_fields()]

    ignore_export = ['_state', 'id', 'printable_comment', 'genotype', 'created', 'modified', 'hospitalization', 'external_location']
    header_list = ['species', 'flybase_id', 'internal_id', 'location', 'categories', 'died', 'public', 
             'origin', 'origin_center', 'origin_internal', 'origin_external', 'origin_id', 'origin_obs',
             'chrx', 'chry', 'chr2', 'chr3', 'chr4', 'bal1', 'bal2', 'bal3', 'chru',
             'wolbachia', 'wolbachia_treatment_date', 'virus_treatment_date', 'isogenization_background', 'special_husbandry_conditions',
             'line_description', 'comments']

    # add those fields that are not in either list to the end of the header_list
    for item in fields:
        if item not in ignore_export and item not in header_list:
            header_list.append(item)

    # prepare response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fly_template.csv"'

    writer = csv.writer(response)
    writer.writerow(header_list)

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
