# Generated by Django 2.1.8 on 2019-06-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0033_fly_origin_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='origin_obs',
            field=models.TextField(blank=True, verbose_name='observations'),
        ),
    ]
