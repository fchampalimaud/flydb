# Generated by Django 2.1.8 on 2019-07-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0047_auto_20190704_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='public',
            field=models.BooleanField(default=False, verbose_name='public through Congento'),
        ),
    ]