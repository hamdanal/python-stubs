from collections.abc import Iterable, Iterator, Mapping
from typing import Any, TypeVar

from django.db import models

_M = TypeVar("_M", bound=models.Model)

def models_from_cursor(model: type[_M], cursor, *, related_fields: Iterable[str] = []) -> Iterator[_M]: ...
def model_from_cursor(model: type[_M], cursor, *, related_fields: Iterable[str] = []) -> _M | None: ...
def model_from_dict(model: type[_M], row: Mapping[str, Any], *, apply_converters: bool = True) -> _M: ...
