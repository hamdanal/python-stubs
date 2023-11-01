from ipaddress import IPv4Interface, IPv4Network, IPv6Interface, IPv6Network

from django.db.models import BooleanField, Func, IntegerField, TextField
from netaddr import EUI

from .fields import CidrAddressField, InetAddressField, MACAddress8Field

class Abbrev(Func):
    arity: int
    function: str
    output_field: TextField[str]

class Broadcast(Func):
    arity: int
    function: str
    output_field: InetAddressField[IPv4Interface | IPv6Interface]

class Family(Func):
    arity: int
    function: str
    output_field: IntegerField[int]

class Host(Func):
    arity: int
    function: str
    output_field: TextField[str]

class Hostmask(Func):
    arity: int
    function: str
    output_field: InetAddressField[IPv4Interface | IPv6Interface]

class Masklen(Func):
    arity: int
    function: str
    output_field: IntegerField[int]

class Netmask(Func):
    arity: int
    function: str
    output_field: InetAddressField[IPv4Interface | IPv6Interface]

class Network(Func):
    arity: int
    function: str
    output_field: CidrAddressField[IPv4Network | IPv6Network]

class SetMasklen(Func):
    arity: int
    function: str
    output_field: InetAddressField[IPv4Interface | IPv6Interface]

class AsText(Func):
    arity: int
    function: str
    output_field: TextField[str]

class IsSameFamily(Func):
    arity: int
    function: str
    output_field: BooleanField[bool]

class Merge(Func):
    arity: int
    function: str
    output_field: CidrAddressField[IPv4Network | IPv6Network]

class Trunc(Func):
    arity: int
    function: str

class Macaddr8Set7bit(Func):
    arity: int
    function: str
    output_field: MACAddress8Field[EUI]
