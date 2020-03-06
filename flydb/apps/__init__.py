from django.apps import AppConfig


class FlyDBConfig(AppConfig):
    name = "flydb"
    verbose_name = "Fly DB"

    def ready(self):
        # from .dashboard import FlyDashboard
        from .fly.fly_list import FlyApp
        from .species import FlySpeciesApp
        from .categories import FlyCategoryApp
        from .stockcenters import FlyStockCenterApp

        global FlyApp
        global FlySpeciesApp
        global FlyCategoryApp
        global FlyStockCenterApp
