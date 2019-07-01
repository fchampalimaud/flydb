# Generated by Django 2.1.8 on 2019-06-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0034_fly_origin_obs'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'stock center',
                'verbose_name_plural': 'stock centers',
                'ordering': ['name'],
            },
        ),
    ]