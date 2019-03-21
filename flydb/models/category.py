from django.db import models

class Category(models.Model):
    name = models.CharField('Name', max_length=30)

    def __str__(self):
        return self.name
