from fly.models import *
import fly.models as Fly
from django.contrib import admin
from django.contrib import messages
from cnpframework.models import *
from cnpframework.admin import *
from aclframework.admin import ACLModelAdmin, ACLTableAdminModel
from aclframework.models import ACLTemplate
import datetime
from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from django.db.models import Q
from fly.views import print_stock_barcode


class SpecieAdmin(admin.ModelAdmin):
	list_display = ('specie_name', 'specie_ncbitax',)

admin.site.register(Specie, SpecieAdmin)


################################################################################

class SupplierAdmin(admin.ModelAdmin):
	list_display = ('supplier_name', 'supplier_contact', 'supplier_email','supplier_url',)

admin.site.register(Supplier, SupplierAdmin)

################################################################################

class SourceAdmin(admin.ModelAdmin):
    list_display = ('source_name', )

admin.site.register(Source, SourceAdmin)

################################################################################

class LegacySourceAdmin(admin.ModelAdmin):
    list_display = ('legacysource_name', )
    
admin.site.register(LegacySource, LegacySourceAdmin)

################################################################################

class LocationAdmin(admin.ModelAdmin):
	list_display = ('location_name', )

admin.site.register( Location,  LocationAdmin)



################################################################################
############ STOCK ADMIN PAGE ##################################################
################################################################################


class StockAdmin(ACLModelAdmin):
    actions = [ 'duplicate_action', 'print_action']
    list_display = ('stock_ccuid','specie','stock_genotype','legacysource','legacy', 'lab')
    readonly_fields = ('stock_entrydate','stock_updated','stock_genotype')
    list_filter = ('legacysource__legacysource_name','specie','stock_hospital', 'stock_died','lab', 'location')
    #list_filter = ('legacysource__legacysource_name','specie','specie__specie_name', 'stock_hospital', 'stock_died','lab')
    #inlines = [CopyInline, ]
    search_fields = ['stock_ccuid', 'stock_legacy1','stock_legacy2','stock_legacy3',
        'stock_genotype','stock_chrx','stock_chry','stock_bal1','stock_chr2','stock_bal2',
        'stock_chr3','stock_bal3','stock_chr4','stock_chru','stock_loc1_location','stock_loc3_data', 'stock_comments']

    fieldsets = [
        (None, {
            'fields': [('stock_ccuid','specie','stock_entrydate','stock_updated'),
            ('legacysource','stock_legacy1','stock_legacy2','stock_legacy3'), 'lab']
        }),
        ('Care', {
            'fields': [('location','stock_loc1_location','stock_loc2_person','stock_loc3_data')]
        }),
        ('Genotype', {
            'fields': [('stock_genotype'),('stock_chrx','stock_chry','stock_bal1'),('stock_chr2','stock_bal2'),('stock_chr3','stock_bal3'),('stock_chr4'),('stock_chru')]
        }),
        (None, {
            'fields': [ 'stock_print', ('stock_comments','stock_hospital','stock_died') ]
        }),
        ('More', {
            'fields': [ 'stock_flydbid'] ,'classes':('collapse',)
        }),
        
    ]
    
    def changelist_view(self, request, extra_context=None):

        try:
        	test = request.META['HTTP_REFERER'].split(request.META['PATH_INFO'])
        except:
                test = '/fly/stock/'

        if test[-1] and not test[-1].startswith('?'):
            if not request.GET.has_key('stock_died__exact'):
                q = request.GET.copy()
                q['stock_died__exact'] = '0'
                request.GET = q
                request.META['QUERY_STRING'] = request.GET.urlencode()

        return super(StockAdmin,self).changelist_view(request, extra_context=extra_context)


    def save_model(self, request, obj, form, change):
        try:
            return super(StockAdmin, self).save_model( request, obj, form, change)
        except Exception as e:
            messages.error(request, e )

    def duplicate_action(self, request, queryset):
        n = queryset.count()
        if n>1: messages.error(request, "Sorry, you only can duplicate a stock at a time.")
        else:
            user = request.useruser = request.user
            groups = user.groups.all()

            for row in queryset:
                row.stock_id = None
                row.stock_ccuid += " (copy)"
                row.save()
                obj = row

                rows = ACLTemplate.objects.filter( Q(acltemplate_table__model='stockacl') & Q(applyto__in=groups) ).distinct()
                for row in rows:
                    aclrow = obj.acl.through()
                    aclrow.acltable_permissions = row.acltemplate_permissions
                    aclrow.acltable_read = row.acltemplate_read
                    aclrow.acltable_update = row.acltemplate_update
                    aclrow.acltable_delete = row.acltemplate_delete
                    aclrow.acltable_nread = row.acltemplate_nread
                    aclrow.acltable_nupdate = row.acltemplate_nupdate
                    aclrow.acltable_ndelete = row.acltemplate_ndelete
                    aclrow.group = row.group
                    aclrow.foreign = obj
                    try:  aclrow.save()
                    except IntegrityError:  pass
       
    duplicate_action.short_description = "Duplicate stock"


    def print_action(self, request, queryset):
        for row in queryset:
            print_stock_barcode( request, row.stock_id, False)
    print_action.short_description = "Print all selected stocks"


#class StockACLAdmin(ACLTableAdminModel): pass
#admin.site.register(StockACL, StockACLAdmin)
      

admin.site.register(Stock, StockAdmin)

################################################################################