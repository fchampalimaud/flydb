# Generated by Django 2.2.1 on 2019-05-11 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0005_auto_20190511_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='hospital',
        ),
        migrations.RemoveField(
            model_name='fly',
            name='location',
        ),
    ]