from django.contrib import admin
from . import models

admin.site.register(models.Fly)
admin.site.register(models.Specie)
admin.site.register(models.Category)
admin.site.register(models.Location)
admin.site.register(models.LegacySource)
admin.site.register(models.Source)
admin.site.register(models.Hospitalization)
# admin.site.register(models.Supplier)
