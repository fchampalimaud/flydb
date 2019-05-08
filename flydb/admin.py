from django.contrib import admin
from .models import Fly, Hospitalization, Specie, Location, LegacySource, Category, Source, Supplier

admin.site.register(Fly)
admin.site.register(Hospitalization)
admin.site.register(Specie)
admin.site.register(Location)
admin.site.register(LegacySource)
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Supplier)