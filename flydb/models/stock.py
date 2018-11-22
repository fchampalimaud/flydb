import datetime, re

from django.contrib.auth.models import User
from django.db import models
from research.models import Group


class Stock(models.Model):

    stock_id        = models.AutoField('Id', primary_key=True)
    stock_ccuid     = models.CharField('CCU ID', max_length=40, blank=True, null=True, unique=True)
    stock_entrydate = models.DateTimeField('Entry date')
    stock_updated   = models.DateTimeField('Last update')
    stock_chrx      = models.CharField('chrX', max_length=60, blank=True, null=True)
    stock_chry      = models.CharField('chrY', max_length=60, blank=True, null=True)
    stock_bal1      = models.CharField('bal1', max_length=60, blank=True, null=True)
    stock_chr2      = models.CharField('chr2', max_length=60, blank=True, null=True)
    stock_bal2      = models.CharField('bal2', max_length=60, blank=True, null=True)
    stock_chr3      = models.CharField('chr3', max_length=60, blank=True, null=True)
    stock_bal3      = models.CharField('bal3', max_length=60, blank=True, null=True)
    stock_chr4      = models.CharField('chr4', max_length=60, blank=True, null=True)
    stock_chru      = models.CharField('chrU', max_length=60, blank=True, null=True)
    stock_comments  = models.TextField('comments', blank=True, null=True)
    stock_print     = models.CharField('Comment to print', max_length=30, blank=True, null=True, default='')
    stock_loc3_data = models.CharField('Local', max_length=30, blank=True, null=True)
    stock_legacy1   = models.CharField('Legacy ID 1', max_length=30, blank=True, null=True)
    stock_legacy2   = models.CharField('Legacy ID 2', max_length=30, blank=True, null=True)
    stock_legacy3   = models.CharField('Legacy ID 3', max_length=30, blank=True, null=True)
    stock_flydbid   = models.CharField('Fly DB ID', max_length=50, blank=True, null=True)
    stock_hospital  = models.BooleanField('Hospital')
    stock_died      = models.BooleanField('Died')
    stock_genotype  = models.CharField('Genotype', max_length=255, blank=True, null=True)
    stock_loc1_location = models.CharField('Chamber location', max_length=30, blank=True, null=True,
        help_text='<b>Format:</b> Tray_Row_Col &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ( <b>Tray</b> = 1-N <b>Row</b> = A-J <b>Col</b> = 1-10 )')

    stock_loc2_person = models.ForeignKey(User, related_name='stock_loc2_person', blank=True, null=True, verbose_name='User', on_delete=models.SET_NULL)
    specie            = models.ForeignKey('Specie', null=True, on_delete=models.SET_NULL)
    lab               = models.ForeignKey(Group, verbose_name='Ownership', null=True, on_delete=models.SET_NULL)
    location          = models.ForeignKey('Location', blank=True, null=True, verbose_name='Care', on_delete=models.SET_NULL)
    legacysource      = models.ForeignKey('LegacySource', null=True, verbose_name='Source', on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-stock_id', ]
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return str(self.stock_ccuid)

    def genotype(self):

        if self.stock_chrx.strip() == "" and self.stock_chry.strip() == "" and self.stock_bal1.strip() == "" and \
                self.stock_chr2.strip() == "" and self.stock_bal2.strip() == "" and \
                self.stock_chr3.strip() == "" and self.stock_bal3.strip() == "" and \
                self.stock_chr4.strip() == "":
            if not self.stock_chru.strip() == "":
                result = '(' + self.stock_chru + ')'
            else:
                result = ''
        else:
            result = self.stock_chrx

            if self.stock_chry.strip() != "":
                result += '/Y' + self.stock_chry

            if self.stock_bal1.strip() != "":
                result += '/' + self.stock_bal1

            ##############################
            result += '; '

            if self.stock_chr2.strip() != "":
                result += self.stock_chr2

            if self.stock_bal2.strip() != "":
                result += '/' + self.stock_bal2

            ##############################
            result += '; '

            if self.stock_chr3.strip() != "":
                result += self.stock_chr3

            if self.stock_bal3.strip() != "":
                result += '/' + self.stock_bal3
            ##############################
            result += '; '

            if self.stock_chr4.strip() != "": result += self.stock_chr4

            if self.stock_chru.strip() != "":
                result += ' (' + self.stock_chru + ')'

        return result

    def legacy(self):
        result = []
        if self.stock_legacy1:
            result.append(self.stock_legacy1)

        if self.stock_legacy2:
            result.append(self.stock_legacy2)

        if self.stock_legacy3:
            result.append(self.stock_legacy3)

        return " | ".join(result)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.stock_entrydate = datetime.datetime.now()
        self.stock_updated = datetime.datetime.now()
        self.stock_genotype = self.genotype()

        if (self.location and self.location.location_id == 1):
            if (not self.stock_loc1_location):
                raise Exception('You have to complete the stock_loc1_location field')
            else:
                if (not re.match('([0-9]*)\_([A-J]*)\_([0-9]*)', self.stock_loc1_location)):
                    raise Exception('The field stock_loc1_location do not have the correct format')
                self.stock_loc2_person = None
                self.stock_loc3_data = None

        if (self.location and self.location.location_id == 2):
            if (not self.stock_loc2_person):
                raise Exception('You have to complete the stock_loc2_person field')
            # self.stock_loc1_location = None
            self.stock_loc3_data = None

        if (self.location and self.location.location_id == 3):
            if (not self.stock_loc3_data):
                raise Exception('You have to complete the stock_loc3_data field')
            self.stock_loc2_person = None
            self.stock_loc1_location = None

        super(Stock, self).save(*args, **kwargs)
