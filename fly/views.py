from django.http import HttpResponse
from django.utils import simplejson
from fly.models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import datetime
import socket
import sys


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
def print_stock_barcode(request, stock_url, returnRequest = True):
    
    stock = Stock.objects.get( pk = stock_url )
    now = datetime.datetime.now()

    if stock.stock_loc1_location!=None:
        location = stock.stock_loc1_location
    else:
        location = ""
        
    message = "%d|%s|%s|%s|%s|%s|%s|%s" % ( stock.stock_id, stock.stock_ccuid, stock.lab.lab_name, stock.genotype(), now.strftime("%Y-%m-%d"), stock.stock_print , location, stock.stock_legacy1)
    
    HOST = get_client_ip(request)
    PORT = settings.PRINTER_SERVER_PORT
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #print  (HOST, PORT)
    s.connect( (HOST, PORT) )    
    s.send(message)
    s.close()
    resp = {'result': 'ok'}    
    if returnRequest:  return HttpResponse(simplejson.dumps(resp), mimetype='application/json')

@login_required
def findstock(request, barcode):

    try:
        stock = Stock.objects.get( stock_ccuid = barcode )
        if( request.POST.get('autoprint', 'off')=='on' ):
            print_stock_barcode(request, stock.stock_id, False)
        resp = {'result': 'found',
                'stock_id': stock.stock_id,
                'stock_ccu': stock.stock_ccuid,
                'genotype': str(stock.genotype()).encode('ascii', 'xmlcharrefreplace'),
            }
    except ObjectDoesNotExist:
        resp = {'result': 'notfound'}
    except:
        resp = {'result': ("Unexpected error: "+ str(sys.exc_info()) ) }
        
    return HttpResponse(simplejson.dumps(resp), mimetype='application/json')

@login_required
def flipnow(request, id):

    try:
        copy = Copy.objects.get( pk=id )
        copy.copy_lastflipdate = datetime.datetime.now()
        copy.save()

        resp = {'result': 'ok', 'copy_lastflipdate': str(copy.copy_lastflipdate) }
    except ObjectDoesNotExist:
        resp = {'result': 'notfound'}

    return HttpResponse(simplejson.dumps(resp), mimetype='application/json')

@login_required
def duplicate(request, id):

    try:
        copy = Copy.objects.get( pk=id )
        copy.copy_entrydate = datetime.datetime.now()
        copy.copy_updated = datetime.datetime.now()
        copy.pk = None
        copy.save()

        father = Copy.objects.get( pk=id )
        copy.source = Source.objects.get(pk=1)
        copy.copy_src1_copy = father
        copy.save()

        resp = {'result': 'ok', 'id': copy.pk}
    except Exception as ex:
        resp = {'result': 'error', 'msg': ex.args}

    return HttpResponse(simplejson.dumps(resp), mimetype='application/json')

#Flip by location
@login_required
def flipbylocation(request, loc):

    try:
        stock = Stock.objects.get( stock_loc1_location=loc )
        #flip code
        stock.save()
        resp = {'result': 'ok', 'location': loc }
    except ObjectDoesNotExist:
        resp = {'result': 'notfound'}

    return HttpResponse(simplejson.dumps(resp), mimetype='application/json')