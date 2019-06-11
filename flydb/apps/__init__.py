from django.apps import AppConfig


class FlyDBConfig(AppConfig):
    name = "flydb"
    verbose_name = "Fly DB"

    def ready(self):
        # from .dashboard import FlyDashboard
        from .legacysource_app import LegacySourceAdminApp
        from .location_app import LocationAdminApp
        from .source_app import SourceAdminApp
        from .specie_app import SpecieAdminApp
        from .fly.fly_list import FlyAdminApp
        # from .supplier_app import SupplierAdminApp  # FIXME no data -> delete
        # from .group import GroupAdminApp
        from .category import CategoryAdminApp

        global LegacySourceAdminApp
        global LocationAdminApp
        global SourceAdminApp
        global SpecieAdminApp
        global FlyAdminApp
        global SupplierAdminApp
        # global GroupAdminApp
        global CategoryAdminApp
