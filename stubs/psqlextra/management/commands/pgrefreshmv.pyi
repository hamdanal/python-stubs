from _typeshed import Unused

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help: str
    def handle(self, *app_labels: Unused, app_label: str, model_name: str, concurrently: bool, **options: Unused) -> None: ...
