from django.apps import AppConfig


class FlyDBConfig(AppConfig):
    name = "flydb"
    verbose_name = "Fly DB"

    def ready(self):
        # from .dashboard import FlyDashboard
        from .fly.fly_list import FlyApp
        from .categories import FlyCategoryApp
        from .legacysources import FlyLegacySourceApp
        # from .location_app import LocationAdminApp
        from .source_app import SourceAdminApp
        from .specie_app import SpecieAdminApp
        # from .supplier_app import SupplierAdminApp  # FIXME no data -> delete
        # from .group import GroupAdminApp

        global FlyApp
        global FlyLegacySourceApp
        global FlyCategoryApp
        # global LocationAdminApp
        global SourceAdminApp
        global SpecieAdminApp
        global SupplierAdminApp
        # global GroupAdminApp
