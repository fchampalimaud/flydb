# Generated by Django 2.1.8 on 2019-06-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0031_fly_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='fly',
            name='origin_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]