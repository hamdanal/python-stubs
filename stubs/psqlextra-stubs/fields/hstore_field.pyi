from collections.abc import Callable, Iterable
from typing import TypeVar, overload
from typing_extensions import Literal

from django.contrib.postgres.fields import HStoreField as DjangoHStoreField
from django.db.models.fields import _ErrorMessagesToOverride, _ValidatorCallable

_T = TypeVar("_T", bound=dict[str, str | None] | None)

class HStoreField(DjangoHStoreField[_T]):
    uniqueness: list[str | tuple[str, ...]] | None
    required: list[str] | None
    @overload
    def __init__(
        self: HStoreField[dict[str, str | None]],
        verbose_name: str | bytes | None = None,
        name: str | None = None,
        *,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[False] = False,
        db_index: bool = False,
        default: _T | Callable[[], _T] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_T, str] | tuple[str, Iterable[tuple[_T, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
        uniqueness: list[str | tuple[str, ...]] | None = None,
        required: list[str] | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self: HStoreField[dict[str, str | None] | None],
        verbose_name: str | bytes | None = None,
        name: str | None = None,
        *,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[True],
        db_index: bool = False,
        default: _T | Callable[[], _T] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_T, str] | tuple[str, Iterable[tuple[_T, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
        uniqueness: list[str | tuple[str, ...]] | None = None,
        required: list[str] | None = None,
    ) -> None: ...
