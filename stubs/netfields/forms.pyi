from _typeshed import Incomplete
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network

from django import forms
from netaddr import EUI

class InetAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: Incomplete) -> IPv4Address | IPv6Address | None: ...

class NoPrefixInetAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: Incomplete) -> IPv4Address | IPv6Address | None: ...

class CidrAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: Incomplete) -> IPv4Network | IPv6Network | None: ...

class MACAddressFormField(forms.Field):
    default_error_messages: dict[str, str]
    def to_python(self, value: Incomplete) -> EUI | None: ...

class MACAddress8FormField(forms.Field):
    default_error_messages: dict[str, str]
    def to_python(self, value: Incomplete) -> EUI | None: ...
