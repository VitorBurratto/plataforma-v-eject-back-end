from django.apps import AppConfig

class PlataformaVConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'plataformav' 
    
    def ready(self):
        import plataformav.signals