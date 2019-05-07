from .fly_permission import FlyPermission
from .fly_queryset import FlyQuerySet
from .fly_base import FlyBase

class Fly(FlyBase):

    objects = FlyQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.genotype = self.genotype()
        super().save(*args, **kwargs)

        if self.lab is not None:
            FlyPermission.objects.get_or_create(stock=self, group=self.lab, viewonly=False)