from _typeshed import Incomplete

from django.db.models import BooleanField, Func, IntegerField, TextField
from netfields.fields import CidrAddressField, InetAddressField, MACAddress8Field

class Abbrev(Func):
    arity: int
    function: str
    output_field: TextField[Incomplete]

class Broadcast(Func):
    arity: int
    function: str
    output_field: InetAddressField[Incomplete]

class Family(Func):
    arity: int
    function: str
    output_field: IntegerField[Incomplete]

class Host(Func):
    arity: int
    function: str
    output_field: TextField[Incomplete]

class Hostmask(Func):
    arity: int
    function: str
    output_field: InetAddressField[Incomplete]

class Masklen(Func):
    arity: int
    function: str
    output_field: IntegerField[Incomplete]

class Netmask(Func):
    arity: int
    function: str
    output_field: InetAddressField[Incomplete]

class Network(Func):
    arity: int
    function: str
    output_field: CidrAddressField[Incomplete]

class SetMasklen(Func):
    arity: int
    function: str
    output_field: InetAddressField[Incomplete]

class AsText(Func):
    arity: int
    function: str
    output_field: TextField[Incomplete]

class IsSameFamily(Func):
    arity: int
    function: str
    output_field: BooleanField[Incomplete]

class Merge(Func):
    arity: int
    function: str
    output_field: CidrAddressField[Incomplete]

class Trunc(Func):
    arity: int
    function: str

class Macaddr8Set7bit(Func):
    arity: int
    function: str
    output_field: MACAddress8Field[Incomplete]
