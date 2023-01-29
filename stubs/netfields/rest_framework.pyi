from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network

from netaddr import EUI
from rest_framework.fields import Field, _DefaultInitial
from rest_framework.serializers import ModelSerializer

class InetAddressField(
    Field[IPv4Address | IPv6Address | None, IPv4Address | IPv6Address | int | str | None, str | None, Incomplete]
):
    store_prefix: bool
    def __init__(
        self,
        store_prefix: bool = True,
        read_only: bool = ...,
        write_only: bool = ...,
        required: bool = ...,
        default: _DefaultInitial[IPv4Address | IPv6Address | None] = ...,
        initial: _DefaultInitial[IPv4Address | IPv6Address | None] = ...,
        source: str = ...,
        label: str = ...,
        help_text: str = ...,
        style: dict[str, Incomplete] = ...,
        error_messages: dict[str, str] = ...,
        validators: Sequence[Callable[..., Incomplete]] = ...,
        allow_null: bool = ...,
    ) -> None: ...

class CidrAddressField(
    Field[IPv4Network | IPv6Network | None, IPv4Network | IPv6Network | int | str | None, str | None, Incomplete]
): ...
class MACAddressField(Field[EUI | None, EUI | str | None, str | None, Incomplete]): ...
class MACAddress8Field(Field[EUI | None, EUI | str | None, str | None, Incomplete]): ...
class NetModelSerializer(ModelSerializer): ...
