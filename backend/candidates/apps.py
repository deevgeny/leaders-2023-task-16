from django.apps import AppConfig


class CandidatesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidates'
    verbose_name = "Кандидаты"

    def ready(self):
        """Register signals."""
        from . import signals
