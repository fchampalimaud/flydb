from .fly_permission import FlyPermission
from .fly_queryset import FlyQuerySet
from .fly_base import FlyBase
from django.db import models

class Fly(FlyBase):
    public = models.BooleanField('Public', default=False)

    ccuid = models.CharField('CCU ID', max_length=40, blank=True, null=True, unique=True)
    comments = models.TextField('comments', blank=True, null=True)
    print = models.CharField('Comment to print', max_length=30, blank=True, null=True, default='')
    shelf = models.CharField('Shelf', max_length=30, blank=True, null=True, help_text = 'Format: Tray_Row_Col ( Tray=1-N; Row=A-J; Col=1-10 )')
    responsible = models.ForeignKey('auth.User', blank=True, null=True, verbose_name='User', on_delete=models.SET_NULL)
    external_location = models.CharField('Local', max_length=30, blank=True, null=True)

    location = models.ForeignKey('Location', blank=True, null=True, verbose_name='Care', on_delete=models.SET_NULL)
    legacysource = models.ForeignKey('LegacySource', null=True, verbose_name='Source', on_delete=models.SET_NULL)

    wolbachia = models.BooleanField('Wolbachia')
    last_test = models.DateField('Last test', null=True, blank=True)
    treatment = models.BooleanField('Treatment')
    strain = models.CharField('Strain', null=True, blank=True, max_length=255)

    virus_treatment = models.BooleanField('Virus Treatment')
    last_treatment = models.DateField('Last treatment', null=True, blank=True)

    isogenization = models.BooleanField('Isogenization')
    background = models.CharField('Background', null=True, blank=True, max_length=255)
    generations = models.CharField('#Generations', null=True, blank=True, max_length=255)


    lab = models.ForeignKey('auth.Group', verbose_name='Ownership', on_delete=models.CASCADE)

    objects = FlyQuerySet.as_manager()


    def legacy(self):
        result = []
        if self.legacy1:
            result.append(self.legacy1)

        if self.legacy2:
            result.append(self.legacy2)

        if self.legacy3:
            result.append(self.legacy3)

        return " | ".join(result)




    def save(self, *args, **kwargs):
        self.genotype = self.genotype()
        super().save(*args, **kwargs)

        if self.lab is not None:
            FlyPermission.objects.get_or_create(fly=self, group=self.lab, viewonly=False)