# Generated by Django 2.1.11 on 2019-08-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0055_auto_20190813_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fly',
            name='virus_treatment',
        ),
        migrations.AlterField(
            model_name='fly',
            name='virus_treatment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Virus treatment date'),
        ),
    ]