# Generated by Django 2.1.8 on 2019-06-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0036_fly_origin_center'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='origin_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fly_stocks', to='flydb.StockCenter', verbose_name='stock center'),
        ),
    ]
