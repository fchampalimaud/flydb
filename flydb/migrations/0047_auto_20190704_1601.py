# Generated by Django 2.1.8 on 2019-07-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0046_fly_flybase_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='internal_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='internal ID'),
        ),
    ]
