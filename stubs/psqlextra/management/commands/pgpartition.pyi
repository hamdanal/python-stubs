from typing import Optional

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help: str
    def add_arguments(self, parser) -> None: ...
    def handle(self, dry: bool, yes: bool, using: str | None, skip_create: bool, skip_delete: bool, *args, **kwargs): ...
