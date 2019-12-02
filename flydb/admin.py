from django.contrib import admin
from import_export import resources, widgets
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from . import models
from .models import Fly, Species, Category, Location, LegacySource, Source, StockCenter, Hospitalization


class FlyResource(resources.ModelResource):
    origin_center = Field(attribute='origin_center', column_name='origin_center', widget=ForeignKeyWidget(StockCenter, 'name'))
    species = Field(attribute='species', column_name='species', widget=ForeignKeyWidget(Species, 'name'))   
    legacysource = Field(attribute='legacysource', column_name='legacysource', widget=ForeignKeyWidget(LegacySource, 'name'))   
    #origin_internal = Field(attribute='origin_internal', column_name='origin_internal', widget=ForeignKeyWidget(users.Group??, 'name'))
    categories = Field(attribute='categories', column_name='categories', widget=ManyToManyWidget(Category, field='name'))

    #TODO maintainer and ownership FKs missing
    class Meta:
        model = Fly
        skip_unchanged = True
        clean_model_instances = True


@admin.register(models.Fly)
class FlyAdmin(ImportMixin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FlyResource
    readonly_fields = ["created", "modified"]

admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
admin.site.register(models.LegacySource)
admin.site.register(models.Source)
admin.site.register(models.StockCenter)
admin.site.register(models.Hospitalization)
# admin.site.register(models.Supplier)
