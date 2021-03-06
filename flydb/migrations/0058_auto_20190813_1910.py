# Generated by Django 2.1.11 on 2019-08-13 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0057_auto_20190813_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='origin_center',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fly_stocks', to='flydb.StockCenter', verbose_name='Stock center'),
        ),
    ]
