# Generated by Django 2.1.8 on 2019-06-24 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0014_auto_20190624_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='internal_id',
        ),
    ]