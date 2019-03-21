from django.db import models

class Hospitalization(models.Model):

    stock = models.ForeignKey('Stock', on_delete=models.CASCADE)
    begin = models.DateField('Begin')
    end = models.DateField('End', null=True, blank=True)
