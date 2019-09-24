from django.db import models


class Source(models.Model):
    source_id = models.AutoField("Id", primary_key=True)
    source_name = models.CharField("Name", max_length=30)

    def __str__(self):
        return self.source_name
