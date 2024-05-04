from _typeshed import Incomplete, Unused
from collections.abc import Callable, Sequence
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from typing import Any
from typing_extensions import TypeAlias

from netaddr import EUI
from rest_framework.fields import Field, empty
from rest_framework.serializers import ModelSerializer

_IPAddress: TypeAlias = IPv4Address | IPv6Address
_IPNetwork: TypeAlias = IPv4Network | IPv6Network
_InetDefaultInitial: TypeAlias = _IPAddress | None | Callable[[], _IPAddress | None] | type[empty]  # type: ignore[valid-type]  # pyright: ignore[reportInvalidTypeForm]

class InetAddressField(Field[_IPAddress | None, _IPAddress | int | str | None, str | None, Incomplete]):
    store_prefix: bool
    def __init__(
        self,
        store_prefix: bool = True,
        read_only: bool = False,
        write_only: bool = False,
        required: bool | None = None,
        default: _InetDefaultInitial = ...,
        initial: _InetDefaultInitial = ...,
        source: str | None = None,
        label: str | None = None,
        help_text: str | None = None,
        style: dict[str, Any] | None = None,
        error_messages: dict[str, str] | None = None,
        validators: Sequence[Callable[..., Unused]] | None = None,
        allow_null: bool = False,
    ) -> None: ...

class CidrAddressField(Field[_IPNetwork | None, _IPNetwork | int | str | None, str | None, Incomplete]): ...
class MACAddressField(Field[EUI | None, EUI | str | None, str | None, Incomplete]): ...
class MACAddress8Field(Field[EUI | None, EUI | str | None, str | None, Incomplete]): ...
class NetModelSerializer(ModelSerializer): ...
