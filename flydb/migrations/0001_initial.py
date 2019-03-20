# Generated by Django 2.1.7 on 2019-03-20 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegacySource',
            fields=[
                ('legacysource_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('legacysource_name', models.CharField(max_length=30, verbose_name='Source')),
            ],
            options={
                'verbose_name': 'Source legacy',
                'verbose_name_plural': 'Legacy sources',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('location_name', models.CharField(max_length=30, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Care',
                'verbose_name_plural': 'Cares',
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('source_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('source_name', models.CharField(max_length=30, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('specie_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('specie_name', models.CharField(max_length=100, verbose_name='Name')),
                ('specie_ncbitax', models.IntegerField(blank=True, null=True, verbose_name='NCBITAX')),
            ],
            options={
                'verbose_name': 'Specie',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('stock_ccuid', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='CCU ID')),
                ('stock_entrydate', models.DateTimeField(verbose_name='Entry date')),
                ('stock_updated', models.DateTimeField(verbose_name='Last update')),
                ('stock_chrx', models.CharField(blank=True, max_length=60, null=True, verbose_name='chrX')),
                ('stock_chry', models.CharField(blank=True, max_length=60, null=True, verbose_name='chrY')),
                ('stock_bal1', models.CharField(blank=True, max_length=60, null=True, verbose_name='bal1')),
                ('stock_chr2', models.CharField(blank=True, max_length=60, null=True, verbose_name='chr2')),
                ('stock_bal2', models.CharField(blank=True, max_length=60, null=True, verbose_name='bal2')),
                ('stock_chr3', models.CharField(blank=True, max_length=60, null=True, verbose_name='chr3')),
                ('stock_bal3', models.CharField(blank=True, max_length=60, null=True, verbose_name='bal3')),
                ('stock_chr4', models.CharField(blank=True, max_length=60, null=True, verbose_name='chr4')),
                ('stock_chru', models.CharField(blank=True, max_length=60, null=True, verbose_name='chrU')),
                ('stock_comments', models.TextField(blank=True, null=True, verbose_name='comments')),
                ('stock_print', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Comment to print')),
                ('stock_loc3_data', models.CharField(blank=True, max_length=30, null=True, verbose_name='Local')),
                ('stock_legacy1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Legacy ID 1')),
                ('stock_legacy2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Legacy ID 2')),
                ('stock_legacy3', models.CharField(blank=True, max_length=30, null=True, verbose_name='Legacy ID 3')),
                ('stock_flydbid', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fly DB ID')),
                ('stock_hospital', models.BooleanField(verbose_name='Hospital')),
                ('stock_died', models.BooleanField(verbose_name='Died')),
                ('stock_genotype', models.CharField(blank=True, max_length=255, null=True, verbose_name='Genotype')),
                ('stock_loc1_location', models.CharField(blank=True, help_text='<b>Format:</b> Tray_Row_Col &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ( <b>Tray</b> = 1-N <b>Row</b> = A-J <b>Col</b> = 1-10 )', max_length=30, null=True, verbose_name='Chamber location')),
                ('lab', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Ownership')),
                ('legacysource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flydb.LegacySource', verbose_name='Source')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='flydb.Location', verbose_name='Care')),
                ('specie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='flydb.Specie')),
                ('stock_loc2_person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_loc2_person', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ['-stock_id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('supplier_name', models.CharField(max_length=50, verbose_name='Name')),
                ('supplier_contact', models.CharField(blank=True, max_length=30, null=True, verbose_name='Contact')),
                ('supplier_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('supplier_url', models.URLField(blank=True, null=True, verbose_name='Webpage')),
                ('supplier_address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('supplier_notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
    ]
