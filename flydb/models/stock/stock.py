import datetime, re
from .stock_permission import StockPermission
from django.contrib.auth.models import User, Group
from django.db import models

from .stock_queryset import StockQuerySet

class Stock(models.Model):

    stock_id        = models.AutoField('Id', primary_key=True)
    stock_ccuid     = models.CharField('CCU ID', max_length=40, blank=True, null=True, unique=True)
    stock_entrydate = models.DateTimeField('Entry date', auto_now_add=True)
    stock_updated   = models.DateTimeField('Last update', auto_now=True)
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
    stock_loc1_location = models.CharField(
        'Chamber location', max_length=30, blank=True, null=True,
        help_text='<b>Format:</b> Tray_Row_Col '
                  '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; '
                  '( <b>Tray</b> = 1-N <b>Row</b> = A-J <b>Col</b> = 1-10 )'
    )

    wolbachia = models.BooleanField('Wolbachia')
    last_test = models.DateField('Last test', null=True, blank=True)
    treatment = models.BooleanField('Treatment')
    strain    = models.CharField('Strain', null=True, blank=True, max_length=255)

    virus_treatment = models.BooleanField('Virus Treatment')
    last_treatment  = models.DateField('Last treatment', null=True, blank=True)

    isogenization = models.BooleanField('Isogenization')
    background    = models.CharField('Background', null=True, blank=True, max_length=255)
    generations   = models.CharField('#Generations', null=True, blank=True, max_length=255)

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    stock_loc2_person = models.ForeignKey(User, related_name='stock_loc2_person', blank=True, null=True, verbose_name='User', on_delete=models.SET_NULL)
    specie            = models.ForeignKey('Specie', null=True, on_delete=models.SET_NULL)
    lab               = models.ForeignKey(Group, verbose_name='Ownership', on_delete=models.CASCADE)
    location          = models.ForeignKey('Location', blank=True, null=True, verbose_name='Care', on_delete=models.SET_NULL)
    legacysource      = models.ForeignKey('LegacySource', null=True, verbose_name='Source', on_delete=models.SET_NULL)

    objects = StockQuerySet.as_manager()

    class Meta:
        ordering = ['-stock_id', ]
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return str(self.stock_ccuid)

    def genotype(self):

        columns = [
            self.stock_chrx, self.stock_chry,
            self.stock_chr2, self.stock_chr3, self.stock_chr4,
            self.stock_bal1, self.stock_bal2, self.stock_bal3
        ]

        if len([x is None or x.strip()=='' for x in columns])==8:
            result = '' if (self.stock_chru is None or self.stock_chru.strip()=='') else f"{self.stock_chru}"
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

    """
    def clean_fields(self, exclude=None):

        if self.location and self.location.location_id == 1:
            if not self.stock_loc1_location:
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
    """


    def save(self, *args, **kwargs):
        self.stock_genotype = self.genotype()
        super().save(*args, **kwargs)

        StockPermission.objects.get_or_create(
            stock=self, group=self.lab, viewonly=False
        )