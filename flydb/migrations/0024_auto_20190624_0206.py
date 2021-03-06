# Generated by Django 2.1.8 on 2019-06-24 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0023_auto_20190624_0157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fly',
            old_name='last_treatment',
            new_name='virus_treatment_date',
        ),
        migrations.RenameField(
            model_name='fly',
            old_name='last_test',
            new_name='wolbachia_test_date',
        ),
        migrations.RenameField(
            model_name='fly',
            old_name='treatment',
            new_name='wolbachia_treatment',
        ),
        migrations.RemoveField(
            model_name='fly',
            name='strain',
        ),
        migrations.AddField(
            model_name='fly',
            name='wolbachia_strain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fly',
            name='background',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='fly',
            name='generations',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='# generations'),
        ),
    ]
