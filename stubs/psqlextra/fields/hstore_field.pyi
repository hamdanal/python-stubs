from collections.abc import Iterable
from typing import Any, TypeVar, overload
from typing_extensions import Literal

from django.contrib.postgres.fields import HStoreField as DjangoHStoreField
from django.db.models.fields import _ErrorMessagesToOverride, _ValidatorCallable

_T = TypeVar("_T", bound=dict[str, str | None] | None)

class HStoreField(DjangoHStoreField[_T]):
    uniqueness: list[str | tuple[str, ...]] | None
    required: list[str] | None
    @overload
    def __new__(
        cls,
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[False] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_T, str] | tuple[str, Iterable[tuple[_T, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        *,
        uniqueness: list[str | tuple[str, ...]] | None = ...,
        required: list[str] | None = ...,
    ) -> HStoreField[dict[str, str | None]]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | bytes | None = ...,
        name: str | None = ...,
        primary_key: bool = ...,
        max_length: int | None = ...,
        unique: bool = ...,
        blank: bool = ...,
        null: Literal[True] = ...,
        db_index: bool = ...,
        default: Any = ...,
        editable: bool = ...,
        auto_created: bool = ...,
        serialize: bool = ...,
        unique_for_date: str | None = ...,
        unique_for_month: str | None = ...,
        unique_for_year: str | None = ...,
        choices: Iterable[tuple[_T, str] | tuple[str, Iterable[tuple[_T, str]]]] = ...,
        help_text: str = ...,
        db_column: str | None = ...,
        db_tablespace: str | None = ...,
        validators: Iterable[_ValidatorCallable] = ...,
        error_messages: _ErrorMessagesToOverride | None = ...,
        *,
        uniqueness: list[str | tuple[str, ...]] | None = ...,
        required: list[str] | None = ...,
    ) -> HStoreField[dict[str, str | None] | None]: ...
