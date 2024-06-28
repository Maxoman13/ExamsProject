from django.apps import AppConfig


class WorksConfig(AppConfig):
    verbose_name = 'Агенство Cadengee'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'works'

    def ready(self):
        import works.signals