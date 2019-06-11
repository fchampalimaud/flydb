from django.apps import AppConfig


class FlyDBConfig(AppConfig):
    name = "flydb"
    verbose_name = "Fly DB"

    def ready(self):
        # from .dashboard import FlyDashboard
        from .fly.fly_list import FlyApp
        from .categories import FlyCategoryApp
        from .legacysources import FlyLegacySourceApp
        from .sources import FlySourceApp
        # from .location_app import LocationAdminApp
        from .specie_app import SpecieAdminApp
        # from .supplier_app import SupplierAdminApp  # FIXME no data -> delete
        # from .group import GroupAdminApp

        global FlyApp
        global FlyCategoryApp
        global FlyLegacySourceApp
        global FlySourceApp
        # global LocationAdminApp
        global SpecieAdminApp
        global SupplierAdminApp
        # global GroupAdminApp
