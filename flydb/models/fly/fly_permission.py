from django.db import models


class FlyPermission(models.Model):


    viewonly = models.BooleanField('Read only access')
    fly      = models.ForeignKey('Fly', on_delete=models.CASCADE)
    group    = models.ForeignKey('auth.Group', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {}".format(str(self.fly), str(self.group), str(self.viewonly))

    class Meta:
        verbose_name = "Fly permission"
        verbose_name_plural = "Flies permissions"

        unique_together = ( ('fly', 'group'), )