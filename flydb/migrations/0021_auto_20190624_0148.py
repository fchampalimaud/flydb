# Generated by Django 2.1.8 on 2019-06-24 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0020_auto_20190624_0145'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Specie',
            new_name='Species',
        ),
    ]