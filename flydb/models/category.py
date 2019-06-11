from django.db import models


class Category(models.Model):
    name = models.CharField('Name', max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
        return self.name
