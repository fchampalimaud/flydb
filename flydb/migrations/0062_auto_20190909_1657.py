# Generated by Django 2.1.12 on 2019-09-09 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flydb', '0061_auto_20190813_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fly',
            name='bal1',
            field=models.CharField(blank=True, max_length=60, verbose_name='Balancer 1'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='bal2',
            field=models.CharField(blank=True, max_length=60, verbose_name='Balancer 2'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='bal3',
            field=models.CharField(blank=True, max_length=60, verbose_name='Balancer 3'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chr2',
            field=models.CharField(blank=True, max_length=60, verbose_name='Chromosome 2'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chr3',
            field=models.CharField(blank=True, max_length=60, verbose_name='Chromosome 3'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chr4',
            field=models.CharField(blank=True, max_length=60, verbose_name='Chromosome 4'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chru',
            field=models.CharField(blank=True, max_length=60, verbose_name='Unknown genotype'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chrx',
            field=models.CharField(blank=True, max_length=60, verbose_name='Chromosome X'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='chry',
            field=models.CharField(blank=True, max_length=60, verbose_name='Chromosome Y'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='died',
            field=models.BooleanField(verbose_name='Stock is dead'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='internal_id',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Internal ID'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='origin_external',
            field=models.CharField(blank=True, max_length=100, verbose_name='Lab name'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='origin_id',
            field=models.CharField(blank=True, max_length=20, verbose_name='Original ID'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='origin_internal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='fly_stocks_shared', to='users.Group', verbose_name='Lab name'),
        ),
        migrations.AlterField(
            model_name='fly',
            name='origin_obs',
            field=models.TextField(blank=True, verbose_name='Observations'),
        ),
    ]
