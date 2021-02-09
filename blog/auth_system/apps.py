from django.apps import AppConfig


class AuthSystemConfig(AppConfig):
    name = 'auth_system'
    
    def ready(self):
        from . import signals
