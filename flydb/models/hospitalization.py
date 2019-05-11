from django.db import models

class Hospitalization(models.Model):

    fly = models.ForeignKey('Fly', on_delete=models.CASCADE)
    begin = models.DateField('Begin')
    end = models.DateField('End', null=True, blank=True)