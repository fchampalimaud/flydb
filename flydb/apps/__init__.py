from django.apps import AppConfig


class FlyDBConfig(AppConfig):
    name = "flydb"
    verbose_name = "Fly DB"

    def ready(self):
        # from .dashboard import FlyDashboard
        from .fly.fly_list import FlyApp
        from .species import FlySpeciesApp
        from .categories import FlyCategoryApp
        # from .legacysources import FlyLegacySourceApp
        # from .sources import FlySourceApp
        # from .location_app import LocationAdminApp
        # from .supplier_app import SupplierAdminApp  # FIXME no data -> delete

        global FlyApp
        global FlySpeciesApp
        global FlyCategoryApp
        # global FlyLegacySourceApp
        # global FlySourceApp
        # global LocationAdminApp
        # global SupplierAdminApp
