from django.db import models

class LegacySource(models.Model):
    legacysource_id = models.AutoField('Id', primary_key=True)
    legacysource_name = models.CharField('Source', max_length=30)

    def __str__(self):
        return self.legacysource_name

    class Meta:
        verbose_name = "Source legacy"
        verbose_name_plural = "Legacy sources"