from .stock_permission import StockPermission
from .stock_queryset import StockQuerySet
from .stock_base import StockBase

class Stock(StockBase):

    objects = StockQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.stock_genotype = self.genotype()
        super().save(*args, **kwargs)

        if self.lab is not None:
            StockPermission.objects.get_or_create(stock=self, group=self.lab, viewonly=False)