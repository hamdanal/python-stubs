from typing import ClassVar
from typing_extensions import Self

from django.db import models

from psqlextra.manager import PostgresManager

class PostgresModel(models.Model):
    class Meta:
        abstract: bool
        base_manager_name: str
    objects: ClassVar[PostgresManager[Self]]
