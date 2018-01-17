from pathlib import Path

from django.contrib import admin
from django.apps import apps

app = apps.get_app_config(Path(__file__).parent.name)

for model in app.get_models():
    admin.site.register(model)
