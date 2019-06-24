# Generated by Django 2.1.8 on 2019-06-24 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0015_remove_fly_internal_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='flydbid',
        ),
        migrations.AddField(
            model_name='fly',
            name='custom_id',
            field=models.CharField(blank=True, max_length=20, unique=True, verbose_name='ID'),
        ),
    ]