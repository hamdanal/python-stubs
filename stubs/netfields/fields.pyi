from _typeshed import Unused
from collections.abc import Callable, Iterable
from ipaddress import IPv4Interface, IPv4Network, IPv6Interface, IPv6Network
from typing import Literal, TypeVar, overload

from django.db.models.expressions import Combinable
from django.db.models.fields import Field, _ErrorMessagesToOverride, _ValidatorCallable
from netaddr import EUI

from .forms import CidrAddressFormField, InetAddressFormField, NoPrefixInetAddressFormField

NET_OPERATORS: dict[str, str]
NET_TEXT_OPERATORS: list[str]
_I = TypeVar("_I", bound=IPv4Interface | IPv6Interface | None)

class InetAddressField(Field[_I | Combinable, _I]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[False] = False,
        db_index: bool = False,
        default: _I | Callable[[], _I] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
        store_prefix_length: bool = True,
    ) -> InetAddressField[IPv4Interface | IPv6Interface]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        *,
        null: Literal[True],
        db_index: bool = False,
        default: _I | Callable[[], _I] = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_I, str] | tuple[str, Iterable[tuple[_I, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
        store_prefix_length: bool = ...,
    ) -> InetAddressField[IPv4Interface | IPv6Interface | None]: ...
    def python_type(self) -> Callable[..., IPv4Interface | IPv6Interface]: ...
    def form_class(self) -> type[InetAddressFormField | NoPrefixInetAddressFormField]: ...

_N = TypeVar("_N", bound=IPv4Network | IPv6Network | None)

class CidrAddressField(Field[_N | Combinable, _N]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[False] = False,
        db_index: bool = False,
        default: _N | Callable[[], _N] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_N, str] | tuple[str, Iterable[tuple[_N, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> CidrAddressField[IPv4Network | IPv6Network]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        *,
        null: Literal[True],
        db_index: bool = False,
        default: _N | Callable[[], _N] = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_N, str] | tuple[str, Iterable[tuple[_N, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> CidrAddressField[IPv4Network | IPv6Network | None]: ...
    def python_type(self) -> Callable[..., IPv4Network | IPv6Network]: ...
    def form_class(self) -> type[CidrAddressFormField]: ...

_E = TypeVar("_E", bound=EUI | None)

class MACAddressField(Field[_E | Combinable, _E]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[False] = False,
        db_index: bool = False,
        default: _E | Callable[[], _E] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_E, str] | tuple[str, Iterable[tuple[_E, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> MACAddressField[EUI]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        *,
        null: Literal[True],
        db_index: bool = False,
        default: _E | Callable[[], _E] = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_E, str] | tuple[str, Iterable[tuple[_E, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> MACAddressField[EUI | None]: ...
    def from_db_value(self, value: str, expression: Unused, connection: Unused, *args: Unused) -> EUI | None: ...
    def get_db_prep_value(self, value: int | str | EUI | None, connection: Unused, prepared: bool = False) -> str: ...

class MACAddress8Field(Field[_E | Combinable, _E]):
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        null: Literal[False] = False,
        db_index: bool = False,
        default: _E | Callable[[], _E] | None = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_E, str] | tuple[str, Iterable[tuple[_E, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> MACAddress8Field[EUI]: ...
    @overload
    def __new__(
        cls,
        verbose_name: str | None = None,
        name: str | None = None,
        primary_key: bool = False,
        max_length: int | None = None,
        unique: bool = False,
        blank: bool = False,
        *,
        null: Literal[True],
        db_index: bool = False,
        default: _E | Callable[[], _E] = ...,
        editable: bool = True,
        auto_created: bool = False,
        serialize: bool = True,
        unique_for_date: str | None = None,
        unique_for_month: str | None = None,
        unique_for_year: str | None = None,
        choices: Iterable[tuple[_E, str] | tuple[str, Iterable[tuple[_E, str]]]] | None = None,
        help_text: str = "",
        db_column: str | None = None,
        db_tablespace: str | None = None,
        validators: Iterable[_ValidatorCallable] = (),
        error_messages: _ErrorMessagesToOverride | None = None,
    ) -> MACAddress8Field[EUI | None]: ...
    def from_db_value(self, value: str, expression: Unused, connection: Unused, *args: Unused) -> EUI | None: ...
    def get_db_prep_value(self, value: int | str | EUI | None, connection: Unused, prepared: bool = False) -> str: ...
