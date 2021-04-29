from django.apps import AppConfig


class CteConfig(AppConfig):
    name = 'cte'

    def ready(self):
        from cte import updater
        updater.start()