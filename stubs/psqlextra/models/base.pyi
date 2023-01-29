from _typeshed import Incomplete

from django.db import models

class PostgresModel(models.Model):
    class Meta:
        abstract: bool
        base_manager_name: str
    objects: Incomplete
