from django.db import models


class StockCenter(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "stock center"
        verbose_name_plural = "stock centers"
        ordering = ["name"]

    def __str__(self):
        return self.name
