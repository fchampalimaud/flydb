from django.contrib import admin
from django.utils import timezone
from django.core.exceptions import FieldDoesNotExist
from django.db.models.fields import CharField
from import_export import resources, widgets
from import_export.admin import ExportActionMixin, ImportMixin
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from . import models
from .models import Fly, Species, Category, StockCenter
from users.models import Group
from django.contrib.auth import get_user_model
from datetime import datetime


class FlyResource(resources.ModelResource):
    origin_center = Field(attribute='origin_center', column_name='origin_center', widget=ForeignKeyWidget(StockCenter, 'name'))
    species = Field(attribute='species', column_name='species', widget=ForeignKeyWidget(Species, 'specie_name'))
    origin_internal = Field(attribute='origin_internal', column_name='origin_internal', widget=ForeignKeyWidget(Group, 'name'))
    categories = Field(attribute='categories', column_name='categories', widget=ManyToManyWidget(Category, field='name'))
    maintainer = Field(attribute='maintainer', column_name='maintainer', widget=ForeignKeyWidget(get_user_model(), 'email'))
    ownership = Field(attribute='ownership', column_name='ownership', widget=ForeignKeyWidget(Group, 'name'))

    _original_values = {}
    _date_fields = ['created', 'modified']
    _generated_dates = False
    
    class Meta:
        model = Fly
        skip_unchanged = True
        clean_model_instances = True

    def before_import_row(self, row, **kwargs):
        for field, value in row.items():
            if field in self._date_fields:
                # check if the value is a float and convert to datetime here
                if isinstance(value, float):
                    import xlrd
                    row[field] = datetime(*xlrd.xldate_as_tuple(value, 0), tzinfo=timezone.get_current_timezone())
                else:
                    # we need to add the timezone to the datetime
                    row[field] = value.replace(tzinfo=timezone.get_current_timezone()).astimezone(tz=timezone.get_current_timezone())
            if value is None:
                # check default value for this field within the model and set it in the row value before proceeding
                try:
                    f = self._meta.model._meta.get_field(field)
                except FieldDoesNotExist:
                    continue
                if f.blank is True and f.null is False:
                    row[field] = ''
                pass 
        return super().before_import_row(row, **kwargs)

    def before_save_instance(self, instance, using_transactions, dry_run):
        # temporarily disable the auto_now and auto_now_add for importing the dates used in the import file
        lst = self.Meta.model._meta.local_fields
        # when these fields are defined it means a bulk import, if not, we want the current date
        if instance.created and instance.modified:
            for field in lst:
                if field.column in self._date_fields:
                    self._original_values[field.column] = {
                        'auto_now': field.auto_now,
                        'auto_now_add': field.auto_now_add,
                    }
                    field.auto_now = False
                    field.auto_now_add = False
        else:
            instance.created = instance.modified = timezone.now()
            self._generated_dates = True
            
        return super().before_save_instance(instance, using_transactions, dry_run)

    def after_save_instance(self, instance, using_transactions, dry_run):
        # re-enable the auto_now and auto_now_add with the original_values
        if not self._generated_dates:
            lst = self.Meta.model._meta.local_fields
            for field in lst:
                if field.column in self._date_fields:
                    field.auto_now = self._original_values[field.column]['auto_now']
                    field.auto_now_add = self._original_values[field.column]['auto_now_add']
        return super().after_save_instance(instance, using_transactions, dry_run)


@admin.register(models.Fly)
class FlyAdmin(ImportMixin, ExportActionMixin, admin.ModelAdmin):
    resource_class = FlyResource
    readonly_fields = ["created", "modified"]

admin.site.register(models.Species)
admin.site.register(models.Category)
admin.site.register(models.Location)
admin.site.register(models.Source)
admin.site.register(models.StockCenter)
admin.site.register(models.Hospitalization)
# admin.site.register(models.Supplier)
