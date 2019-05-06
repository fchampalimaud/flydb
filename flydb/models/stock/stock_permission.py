from django.db import models


class StockPermission(models.Model):


    viewonly = models.BooleanField('Read only access')
    stock    = models.ForeignKey('Stock', on_delete=models.CASCADE)
    group    = models.ForeignKey('auth.Group', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(str(self.stock), str(self.group), str(self.readonly))

    class Meta:
        verbose_name = "Stock permission"
        verbose_name_plural = "Stocks permissions"

        unique_together = ( ('stock', 'group'), )