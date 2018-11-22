from django.db import models

class Location(models.Model):
    location_id = models.AutoField('Id', primary_key=True)
    location_name = models.CharField('Name', max_length=30)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = "Care"
        verbose_name_plural = "Cares"