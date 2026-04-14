from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from .firebase import initialize_firebase
        initialize_firebase()