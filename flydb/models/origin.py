from django.db import models
from model_utils import Choices


class Origin(models.Model):

    ORIGIN_TYPES = Choices(
        ("center", "Stock Center"),
        ("internal", "Internal Lab"),
        ("external", "External Lab"),
    )

    source = models.CharField(max_length=100, verbose_name="source name")
    previous_id = models.CharField(max_length=30)
    category = models.CharField(
        max_length=8, choices=ORIGIN_TYPES, default=ORIGIN_TYPES.center
    )

    stock = models.ForeignKey(
        to="flydb.Fly", on_delete=models.CASCADE, related_name="origins"
    )

    class Meta:
        verbose_name = "origin"
        verbose_name_plural = "origins"
        ordering = ["source"]

    def __str__(self):
        return self.source
