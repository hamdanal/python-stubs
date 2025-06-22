from _typeshed import SupportsItems
from typing import Any, Literal, TypedDict, overload, type_check_only
from typing_extensions import TypeAlias

import pandas as pd

from pandapower._typing import Float
from pandapower.auxiliary import pandapowerNet

_Element: TypeAlias = Literal["line", "line_dc", "trafo", "trafo3w", "fuse"]
_StdType: TypeAlias = dict[str, Any]

@type_check_only
class _StdLineType(TypedDict, total=False):
    c_nf_per_km: float
    r_ohm_per_km: float
    x_ohm_per_km: float
    c0_nf_per_km: float
    r0_ohm_per_km: float
    x0_ohm_per_km: float
    max_i_ka: float
    type: str
    q_mm2: int
    alpha: float

@type_check_only
class _StdLineDcType(TypedDict, total=False):
    r_ohm_per_km: float
    max_i_ka: float
    type: str
    q_mm2: float
    alpha: float

@type_check_only
class _StdTrafoType(TypedDict, total=False):
    i0_percent: float
    pfe_kw: float
    vkr_percent: float
    sn_mva: float
    vn_lv_kv: float
    vn_hv_kv: float
    vk_percent: float
    shift_degree: int
    vector_group: str
    tap_side: str
    tap_neutral: int
    tap_min: int
    tap_max: int
    tap_step_degree: int
    tap_step_percent: float
    tap_phase_shifter: bool

@type_check_only
class _StdTrafo3wType(TypedDict, total=False):
    sn_hv_mva: int
    sn_mv_mva: int
    sn_lv_mva: int
    vn_hv_kv: int
    vn_mv_kv: int
    vn_lv_kv: int
    vk_hv_percent: float
    vk_mv_percent: float
    vk_lv_percent: float
    vkr_hv_percent: float
    vkr_mv_percent: float
    vkr_lv_percent: float
    pfe_kw: int
    i0_percent: float
    shift_mv_degree: int
    shift_lv_degree: int
    vector_group: str
    tap_side: str
    tap_neutral: int
    tap_min: int
    tap_max: int
    tap_step_percent: float

@type_check_only
class _StdFuseType(TypedDict, total=False):
    fuse_type: str
    i_rated_a: float
    t_avg: float | list[float]
    t_min: float | list[float]
    t_total: float | list[float]
    x_avg: float | list[float]
    x_min: float | list[float]
    x_total: float | list[float]

_StdLineTypes: TypeAlias = dict[str, _StdLineType]
_StdLineDcTypes: TypeAlias = dict[str, _StdLineDcType]
_StdTrafoTypes: TypeAlias = dict[str, _StdTrafoType]
_StdTrafo3wTypes: TypeAlias = dict[str, _StdTrafo3wType]
_StdFuseTypes: TypeAlias = dict[str, _StdFuseType]

@type_check_only
class _StdTypes(TypedDict):
    line: _StdLineTypes
    line_dc: _StdLineDcTypes
    trafo: _StdTrafoTypes
    trafo3w: _StdTrafo3wTypes
    fuse: _StdFuseTypes

def required_std_type_parameters(element: _Element = "line") -> list[str]: ...
def create_std_type(
    net: pandapowerNet, data: _StdType, name: str, element: _Element = "line", overwrite: bool = True, check_required: bool = True
) -> None: ...
def create_std_types(
    net: pandapowerNet,
    data: SupportsItems[str, _StdType],
    element: _Element = "line",
    overwrite: bool = True,
    check_required: bool = True,
) -> None: ...
def copy_std_types(
    to_net: pandapowerNet, from_net: pandapowerNet, element: _Element = "line", overwrite: bool = True
) -> None: ...
@overload
def load_std_type(net: pandapowerNet, name: str, element: Literal["line"] = "line") -> _StdLineType: ...
@overload
def load_std_type(net: pandapowerNet, name: str, element: Literal["line_dc"]) -> _StdLineDcType: ...
@overload
def load_std_type(net: pandapowerNet, name: str, element: Literal["trafo"]) -> _StdTrafoType: ...
@overload
def load_std_type(net: pandapowerNet, name: str, element: Literal["trafo3w"]) -> _StdTrafo3wType: ...
@overload
def load_std_type(net: pandapowerNet, name: str, element: Literal["fuse"]) -> _StdFuseType: ...
def std_type_exists(net: pandapowerNet, name: str, element: _Element = "line") -> bool: ...
def delete_std_type(net: pandapowerNet, name: str, element: _Element = "line") -> None: ...
def rename_std_type(net: pandapowerNet, old_name: str, new_name: str, element: _Element = "line") -> None: ...
def available_std_types(net: pandapowerNet, element: _Element = "line") -> pd.DataFrame: ...
def parameter_from_std_type(net: pandapowerNet, parameter: str, element: _Element = "line", fill: Any | None = None) -> None: ...
def change_std_type(net: pandapowerNet, eid: int, name: str, element: _Element = "line") -> None: ...
def find_std_type_by_parameter(
    net: pandapowerNet, data: _StdType, element: _Element = "line", epsilon: Float = 0.0
) -> list[str]: ...
def find_std_type_alternative(
    net: pandapowerNet, data, element: _Element = "line", voltage_rating: str = "", epsilon: Float = 0.0
) -> list[str]: ...
def add_zero_impedance_parameters(net: pandapowerNet) -> None: ...
def add_temperature_coefficient(net: pandapowerNet, fill: Float | None = None) -> None: ...
def basic_line_std_types() -> _StdLineTypes: ...
def basic_line_dc_std_types() -> _StdLineDcTypes: ...
def basic_trafo_std_types() -> _StdTrafoTypes: ...
def basic_trafo3w_std_types() -> _StdTrafo3wTypes: ...
def basic_fuse_std_types() -> _StdFuseTypes: ...
def basic_std_types() -> _StdTypes: ...
def add_basic_std_types(
    net: pandapowerNet,
) -> tuple[_StdLineTypes, _StdLineDcTypes, _StdTrafoTypes, _StdTrafo3wTypes, _StdFuseTypes]: ...
