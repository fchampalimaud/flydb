from django.db import models



class StockQuerySet(models.QuerySet):
    """
    ORDER QUERYSET MANAGER DEFINITION
    """

    def list_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to list.
        """
        return self.filter(
            stock_permission_set__group__in=user.groups.all()
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
        return self.filter(
            stock_permission_set__group__in=user.groups.all()
        )

    def has_update_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to update.
        """
        return self.filter(
            stock_permission_set__group__in=user.groups.all(),
            stock_permission_set__viewonly=False
        )

    def has_remove_permissions(self, user):
        """
        The function filters the queryset to return only the objects the user has permissions to remove.
        """
        return self.filter(
            stock_permission_set__group__in = user.groups.all(),
            stock_permission_set__viewonly = False
        )