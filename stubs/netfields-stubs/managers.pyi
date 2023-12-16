from typing import TypeVar
from typing_extensions import Literal

from django.db import models

_T = TypeVar("_T", bound=models.Model)

class NetManager(models.Manager[_T]):
    use_for_related_fields: Literal[True]
