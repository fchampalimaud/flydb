from django.db import models

class Supplier(models.Model):
    supplier_id = models.AutoField('Id', primary_key=True)
    supplier_name = models.CharField('Name', max_length=50)
    supplier_contact = models.CharField('Contact', max_length=30, blank=True, null=True)
    supplier_email = models.EmailField('Email', blank=True, null=True)
    supplier_url = models.URLField('Webpage', blank=True, null=True, verify_exists=True)
    supplier_address = models.TextField('Address', blank=True, null=True)
    supplier_notes = models.TextField('Notes', blank=True, null=True)

    def __unicode__(self):
        return self.supplier_name

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
