from _typeshed import Incomplete, StrOrBytesPath, SupportsRead, SupportsWrite
from collections.abc import Mapping
from typing import TypedDict, overload

from pandapower.auxiliary import pandapowerNet

xlsxwriter_INSTALLED: bool
openpyxl_INSTALLED: bool

def to_pickle(net: pandapowerNet, filename: SupportsWrite[bytes] | str) -> None: ...
def to_excel(
    net: pandapowerNet, filename: StrOrBytesPath, include_empty_tables: bool = False, include_results: bool = True
) -> None: ...
@overload
def to_json(
    net: pandapowerNet, filename: None = None, encryption_key: str | None = None, store_index_names: bool = False
) -> str: ...
@overload
def to_json(
    net: pandapowerNet,
    filename: SupportsWrite[str] | StrOrBytesPath,
    encryption_key: str | None = None,
    store_index_names: bool = False,
) -> None: ...
@overload
def to_json(
    net: pandapowerNet,
    filename: SupportsWrite[str] | StrOrBytesPath | None = None,
    encryption_key: str | None = None,
    store_index_names: bool = False,
) -> str | None: ...
def from_pickle(filename: SupportsRead[bytes] | StrOrBytesPath, convert: bool = True) -> pandapowerNet: ...
def from_excel(filename: StrOrBytesPath, convert: bool = True) -> pandapowerNet: ...

class _FromJsonKwds(TypedDict, total=False):  # noqa: PYI049
    convert: bool
    encryption_key: str | None
    elements_to_deserialize: Incomplete | None
    keep_serialized_elements: bool
    add_basic_std_types: bool
    replace_elements: Mapping[str, str] | None
    empty_dict_like_object: Incomplete | None

def from_json(
    filename: SupportsRead[str] | StrOrBytesPath,
    convert: bool = True,
    encryption_key: str | None = None,
    elements_to_deserialize: Incomplete | None = None,
    keep_serialized_elements: bool = True,
    add_basic_std_types: bool = False,
    replace_elements: Mapping[str, str] | None = None,
    empty_dict_like_object: Incomplete | None = None,
) -> pandapowerNet: ...
def from_json_string(
    json_string: str,
    convert: bool = True,
    encryption_key: str | None = None,
    elements_to_deserialize: Incomplete | None = None,
    keep_serialized_elements: bool = True,
    add_basic_std_types: bool = False,
    replace_elements: Mapping[str, str] | None = None,
    empty_dict_like_object: Incomplete | None = None,
) -> pandapowerNet: ...
def from_json_dict(json_dict: Mapping[str, Incomplete]) -> pandapowerNet: ...
