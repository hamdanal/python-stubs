from _typeshed import StrOrBytesPath, SupportsRead, SupportsWrite
from collections.abc import Iterable, Mapping, MutableMapping
from typing import Any, overload

from pandapower.auxiliary import pandapowerNet

xlsxwriter_INSTALLED: bool
openpyxl_INSTALLED: bool

def to_pickle(net: pandapowerNet, filename: SupportsWrite[bytes] | str) -> None: ...
def to_excel(
    net: pandapowerNet, filename: StrOrBytesPath, include_empty_tables: bool = False, include_results: bool = True
) -> None: ...
@overload
def to_json(
    net: pandapowerNet,
    filename: None = None,
    encryption_key: str | None = None,
    indent: int | str | None = 2,
    sort_keys: bool = False,
) -> str: ...
@overload
def to_json(
    net: pandapowerNet,
    filename: SupportsWrite[str] | StrOrBytesPath,
    encryption_key: str | None = None,
    indent: int | str | None = 2,
    sort_keys: bool = False,
) -> None: ...
@overload
def to_json(
    net: pandapowerNet,
    filename: SupportsWrite[str] | StrOrBytesPath | None = None,
    encryption_key: str | None = None,
    indent: int | str | None = 2,
    sort_keys: bool = False,
) -> str | None: ...
def from_pickle(filename: SupportsRead[bytes] | StrOrBytesPath, convert: bool = True) -> pandapowerNet: ...
def from_excel(filename: StrOrBytesPath, convert: bool = True) -> pandapowerNet: ...
def from_json(  # keep inline with pandapower._typing.FromJsonKwds
    filename_or_str: SupportsRead[str] | StrOrBytesPath,
    convert: bool = True,
    encryption_key: str | None = None,
    elements_to_deserialize: Iterable[str] | None = None,
    keep_serialized_elements: bool = True,
    add_basic_std_types: bool = False,
    replace_elements: Mapping[str, str] | None = None,
    empty_dict_like_object: MutableMapping[str, Any] | None = None,
    ignore_unknown_objects: bool = False,
) -> pandapowerNet: ...
def from_json_string(
    json_string: str,
    convert: bool = False,
    encryption_key: str | None = None,
    elements_to_deserialize: Iterable[str] | None = None,
    keep_serialized_elements: bool = True,
    add_basic_std_types: bool = False,
    replace_elements: Mapping[str, str] | None = None,
    empty_dict_like_object: MutableMapping[str, Any] | None = None,
    ignore_unknown_objects: bool = False,
) -> pandapowerNet: ...
def from_json_dict(json_dict: Mapping[str, Any]) -> pandapowerNet: ...
