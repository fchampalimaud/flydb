from django.db import models

class Specie(models.Model):
    specie_id = models.AutoField('Id', primary_key=True)
    specie_name = models.CharField('Name', max_length=100)
    specie_ncbitax = models.IntegerField('NCBITAX', blank=True, null=True)
   
    def __str__(self):
        return self.specie_name

    class Meta:
        verbose_name = "Specie"
        verbose_name_plural = "Species"