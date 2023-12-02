from _typeshed import Unused

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help: str
    def handle(
        self, dry: bool, yes: bool, using: str | None, skip_create: bool, skip_delete: bool, *args: Unused, **kwargs: Unused
    ) -> None: ...
