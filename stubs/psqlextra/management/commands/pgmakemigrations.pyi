from typing import Any

from django.core.management.commands import makemigrations

class Command(makemigrations.Command):
    help: str
    def handle(self, *app_labels: str, **options: Any) -> None: ...
