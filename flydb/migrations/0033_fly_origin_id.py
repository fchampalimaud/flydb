# Generated by Django 2.1.8 on 2019-06-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0032_fly_origin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='origin_id',
            field=models.CharField(blank=True, max_length=20, verbose_name='original ID'),
        ),
    ]
