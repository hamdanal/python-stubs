from django.core.management.commands import makemigrations

class Command(makemigrations.Command):
    help: str
    def handle(self, *app_labels, **options): ...
