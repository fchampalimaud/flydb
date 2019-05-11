from django.db import models
from django.db.models import Q

class FlyQuerySet(models.QuerySet):
    """
    ORDER QUERYSET MANAGER DEFINITION
    """

    def list_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to list.
        """
        if user.is_superuser:
            return self
        else:
            return self.filter(
                Q(flypermission__group__in=user.groups.all()) |
                Q(responsible=user)
            )

    def has_add_permissions(self, user):
        """
        The function returns a Boolean indicating if the user can add or not a new object.
        """
        return True


    def has_view_permissions(self, user):
        """
        The function returns a boolean indicating if the user has view permissions to the current queryset.
        """
        if user.is_superuser:
            return self
        else:
            return self.filter(
                Q(flypermission__group__in=user.groups.all()) |
                Q(responsible=user)
            )

    def has_update_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to update.
        """
        if user.is_superuser:
            return self
        else:
            return self.filter(
                Q(flypermission__group__in=user.groups.all(), flypermission__viewonly=False) |
                Q(responsible=user)
            )

    def has_remove_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to remove.
        """
        if user.is_superuser:
            return self
        else:
            return self.filter(
                Q(flypermission__group__in = user.groups.all(), flypermission__viewonly = False) |
                Q(responsible=user)
            )