from django.db import models


class Hospitalization(models.Model):

    fly = models.ForeignKey("Fly", on_delete=models.CASCADE)
    start_date = models.DateField("Start date")
    end_date = models.DateField("End date", null=True, blank=True)
