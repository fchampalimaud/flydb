# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FlyLegacysource(models.Model):
    legacysource_id = models.AutoField(primary_key=True)
    legacysource_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'fly_legacysource'


class FlyLocation(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'fly_location'


class FlySource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'fly_source'


class FlySpecie(models.Model):
    specie_id = models.AutoField(primary_key=True)
    specie_name = models.CharField(max_length=100)
    specie_ncbitax = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'fly_specie'


class FlyStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    stock_ccuid = models.CharField(max_length=40, blank=True, null=True)
    specie_id = models.IntegerField()
    stock_entrydate = models.DateTimeField()
    stock_updated = models.DateTimeField()
    stock_chrx = models.CharField(max_length=60, blank=True, null=True)
    stock_chry = models.CharField(max_length=60, blank=True, null=True)
    stock_bal1 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr2 = models.CharField(max_length=60, blank=True, null=True)
    stock_bal2 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr3 = models.CharField(max_length=60, blank=True, null=True)
    stock_bal3 = models.CharField(max_length=60, blank=True, null=True)
    stock_chr4 = models.CharField(max_length=60, blank=True, null=True)
    stock_chru = models.CharField(max_length=230, blank=True, null=True)
    stock_comments = models.TextField(blank=True, null=True)
    stock_hospital = models.IntegerField()
    stock_died = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    stock_loc1_location = models.CharField(max_length=30, blank=True, null=True)
    stock_loc2_person_id = models.IntegerField(blank=True, null=True)
    stock_loc3_data = models.CharField(max_length=30, blank=True, null=True)
    lab_id = models.IntegerField()
    legacysource_id = models.IntegerField()
    stock_legacy1 = models.CharField(max_length=30, blank=True, null=True)
    stock_legacy2 = models.CharField(max_length=30, blank=True, null=True)
    stock_legacy3 = models.CharField(max_length=30, blank=True, null=True)
    stock_flydbid = models.CharField(max_length=50, blank=True, null=True)
    stock_genotype = models.CharField(max_length=255, blank=True, null=True)
    stock_print = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'fly_stock'


class FlyStockacl(models.Model):
    acltable_id = models.AutoField(primary_key=True)
    acltable_permissions = models.IntegerField()
    acltable_read = models.IntegerField()
    acltable_update = models.IntegerField()
    acltable_delete = models.IntegerField()
    acltable_nread = models.IntegerField()
    acltable_nupdate = models.IntegerField()
    acltable_ndelete = models.IntegerField()
    group_id = models.IntegerField()
    foreign_id = models.IntegerField()

    class Meta:
        db_table = 'fly_stockacl'
        unique_together = (('group_id', 'foreign_id'),)


class FlySupplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)
    supplier_contact = models.CharField(max_length=30, blank=True, null=True)
    supplier_email = models.CharField(max_length=75, blank=True, null=True)
    supplier_url = models.CharField(max_length=200, blank=True, null=True)
    supplier_address = models.TextField(blank=True, null=True)
    supplier_notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'fly_supplier'
