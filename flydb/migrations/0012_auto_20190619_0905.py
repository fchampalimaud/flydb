# Generated by Django 2.1.8 on 2019-06-19 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0011_auto_20190611_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='lab',
        ),
        migrations.RemoveField(
            model_name='fly',
            name='responsible',
        ),
    ]
