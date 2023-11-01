from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network

from django import forms
from netaddr import EUI

class InetAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: str | IPv4Interface | IPv6Interface | None) -> IPv4Interface | IPv6Interface | None: ...

class NoPrefixInetAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: str | IPv4Address | IPv6Address | None) -> IPv4Address | IPv6Address | None: ...

class CidrAddressFormField(forms.Field):
    widget: type[forms.TextInput]
    default_error_messages: dict[str, str]
    def to_python(self, value: str | IPv4Network | IPv6Network | None) -> IPv4Network | IPv6Network | None: ...

class MACAddressFormField(forms.Field):
    default_error_messages: dict[str, str]
    def to_python(self, value: str | EUI | None) -> EUI | None: ...

class MACAddress8FormField(forms.Field):
    default_error_messages: dict[str, str]
    def to_python(self, value: str | EUI | None) -> EUI | None: ...
