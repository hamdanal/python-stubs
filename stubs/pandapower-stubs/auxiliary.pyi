import logging
from collections.abc import Iterable, Mapping, MutableMapping
from typing import Any, Final, Literal, NoReturn, TypeVar, overload
from typing_extensions import Self, deprecated

import geopandas as gpd
import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, DTypeLike, NDArray
from shapely.geometry.base import BaseGeometry

from pandapower._typing import Array2D, Float, Int
from pandapower.std_types import _StdTypes

_T = TypeVar("_T")

def log_to_level(msg: str, passed_logger: logging.Logger, level: str) -> None: ...
def version_check(package_name: str, level: str = "UserWarning", ignore_not_installed: bool = False) -> None: ...
def soft_dependency_error(fct_name: str, required_packages: str | Iterable[str]) -> NoReturn: ...
def warn_and_fix_parameter_renaming(
    old_parameter_name: str,
    new_parameter_name: str,
    new_parameter: _T,
    default_value: _T,
    category: type[Warning] = ...,
    **kwargs: Any,
) -> _T: ...

class ADict(dict[str, _T], MutableMapping[str, _T]):
    def __setattr__(self, key: str, value: _T) -> None: ...
    def __delattr__(self, key: str, force: bool = False) -> None: ...
    def __call__(self, key: str) -> _T: ...
    def __getattr__(self, key: str) -> _T: ...
    def __deepcopy__(self, memo: dict[int, Any] | None) -> Self: ...

class pandapowerNet(ADict[pd.DataFrame]):
    # These attributes are not defined in the class body, but are added via __getitem__
    bus: pd.DataFrame
    bus_dc: pd.DataFrame
    load: pd.DataFrame
    sgen: pd.DataFrame
    motor: pd.DataFrame
    asymmetric_load: pd.DataFrame
    asymmetric_sgen: pd.DataFrame
    storage: pd.DataFrame
    gen: pd.DataFrame
    switch: pd.DataFrame
    shunt: pd.DataFrame
    svc: pd.DataFrame
    ssc: pd.DataFrame
    vsc: pd.DataFrame
    ext_grid: pd.DataFrame
    line: pd.DataFrame
    line_dc: pd.DataFrame
    trafo: pd.DataFrame
    trafo3w: pd.DataFrame
    impedance: pd.DataFrame
    tcsc: pd.DataFrame
    dcline: pd.DataFrame
    ward: pd.DataFrame
    xward: pd.DataFrame
    measurement: pd.DataFrame
    pwl_cost: pd.DataFrame
    poly_cost: pd.DataFrame
    characteristic: pd.DataFrame
    controller: pd.DataFrame
    group: pd.DataFrame
    version: str
    format_version: str
    converged: bool
    OPF_converged: bool
    name: str
    f_hz: float
    sn_mva: float
    std_types: _StdTypes
    user_pf_options: dict[str, Any]

    res_asymmetric_load: pd.DataFrame
    res_asymmetric_load_3ph: pd.DataFrame
    res_asymmetric_sgen: pd.DataFrame
    res_asymmetric_sgen_3ph: pd.DataFrame
    res_bus: pd.DataFrame
    res_bus_3ph: pd.DataFrame
    res_bus_dc: pd.DataFrame
    res_bus_est: pd.DataFrame
    res_bus_sc: pd.DataFrame
    res_dcline: pd.DataFrame
    res_ext_grid: pd.DataFrame
    res_ext_grid_3ph: pd.DataFrame
    res_ext_grid_sc: pd.DataFrame
    res_gen: pd.DataFrame
    res_gen_sc: pd.DataFrame
    res_impedance: pd.DataFrame
    res_impedance_est: pd.DataFrame
    res_line: pd.DataFrame
    res_line_3ph: pd.DataFrame
    res_line_dc: pd.DataFrame
    res_line_est: pd.DataFrame
    res_line_sc: pd.DataFrame
    res_load: pd.DataFrame
    res_load_3ph: pd.DataFrame
    res_motor: pd.DataFrame
    res_sgen: pd.DataFrame
    res_sgen_3ph: pd.DataFrame
    res_sgen_sc: pd.DataFrame
    res_shunt: pd.DataFrame
    res_shunt_3ph: pd.DataFrame
    res_ssc: pd.DataFrame
    res_storage: pd.DataFrame
    res_storage_3ph: pd.DataFrame
    res_svc: pd.DataFrame
    res_switch: pd.DataFrame
    res_switch_est: pd.DataFrame
    res_switch_sc: pd.DataFrame
    res_tcsc: pd.DataFrame
    res_trafo: pd.DataFrame
    res_trafo3w: pd.DataFrame
    res_trafo3w_est: pd.DataFrame
    res_trafo3w_sc: pd.DataFrame
    res_trafo_3ph: pd.DataFrame
    res_trafo_est: pd.DataFrame
    res_trafo_sc: pd.DataFrame
    res_vsc: pd.DataFrame
    res_ward: pd.DataFrame
    res_xward: pd.DataFrame
    res_protection: pd.DataFrame  # Optional?
    @deprecated("Use copy.deepcopy(net) instead of net.deepcopy()")
    def deepcopy(self) -> Self: ...

class GeoAccessor:
    def __init__(self, pandas_obj) -> None: ...
    @property
    def as_geo_obj(self): ...
    @property
    def type(self) -> str: ...
    @property
    def as_shapely_obj(self) -> pd.Series[BaseGeometry]: ...  # type: ignore[type-var] # pyright: ignore[reportInvalidTypeArguments]
    @property
    def as_geoseries(self) -> gpd.GeoSeries: ...
    def __getattr__(self, item: str) -> Any: ...

def plural_s(number: Int) -> str: ...
@overload
def ets_to_element_types(ets: None = None) -> pd.Series[str]: ...
@overload
def ets_to_element_types(ets: str) -> str: ...
@overload
def ets_to_element_types(ets: list[str] | pd.Series[str] | pd.Index[str] | NDArray[np.str_]) -> list[str]: ...
@overload
def element_types_to_ets(element_types: None = None) -> pd.Series[str]: ...
@overload
def element_types_to_ets(element_types: str) -> str: ...
@overload
def element_types_to_ets(element_types: list[str] | pd.Series[str] | pd.Index[str] | NDArray[np.str_]) -> list[str]: ...
def empty_defaults_per_dtype(dtype: DTypeLike) -> float | Literal[""] | None: ...
def get_free_id(df: pd.DataFrame) -> np.int64: ...

class ppException(Exception): ...
class AlgorithmUnknown(ppException): ...
class LoadflowNotConverged(ppException): ...
class ControllerNotConverged(ppException): ...
class NetCalculationNotConverged(ppException): ...
class OPFNotConverged(ppException): ...
class MapboxTokenMissing(ppException): ...

def get_indices(
    selection: Iterable[Int], lookup: Mapping[Int, Int] | Mapping[str, Mapping[Int, Int]], fused_indices: bool = True
) -> NDArray[np.int64]: ...
def ensure_iterability(var: _T | Iterable[_T], len_: Int | None = None) -> Iterable[_T]: ...
def read_from_net(
    net: pandapowerNet,
    element: str,
    index: Int | ArrayLike | pd.Index[int],
    variable: str,
    flag: Literal["auto", "single_index", "all_index", "loc", "object"] = "auto",
) -> Any: ...
def write_to_net(
    net: pandapowerNet,
    element: str,
    index: Int | ArrayLike | pd.Index[int],
    variable: str,
    values: Any,
    flag: Literal["auto", "single_index", "all_index", "loc", "object"] = "auto",
) -> None: ...

# jit-ted functions
def get_values(source, selection, lookup) -> NDArray[np.int64]: ...
def set_elements_oos(ti, tis, bis, lis) -> None: ...
def set_isolated_buses_oos(bus_in_service, ppc_bus_isolated, bus_lookup) -> None: ...
def X012_to_X0(X012: ArrayLike) -> NDArray[np.complex128]: ...
def X012_to_X1(X012: ArrayLike) -> NDArray[np.complex128]: ...
def X012_to_X2(X012: ArrayLike) -> NDArray[np.complex128]: ...
def combine_X012(X0: ArrayLike, X1: ArrayLike, X2: ArrayLike) -> NDArray[np.complex128]: ...
def phase_shift_unit_operator(angle_deg: Float) -> np.complex128: ...

a: Final[np.complex128]
asq: Final[np.complex128]
Tabc: Final[Array2D[np.complex128]]
T012: Final[Array2D[np.complex128]]

def sequence_to_phase(X012: ArrayLike) -> NDArray[np.complex128]: ...
def phase_to_sequence(Xabc: ArrayLike) -> NDArray[np.complex128]: ...
def I0_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def I1_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def I2_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def V1_from_ppc(ppc: Mapping[str, ArrayLike]) -> NDArray[np.complex128]: ...
def V_from_I(Y: ArrayLike, I: ArrayLike) -> NDArray[np.complex128]: ...
def I_from_V(Y: ArrayLike, V: ArrayLike) -> NDArray[np.complex128]: ...
def S_from_VI_elementwise(V: ArrayLike, I: ArrayLike) -> NDArray[np.complex128]: ...
def I_from_SV_elementwise(S: ArrayLike, V: ArrayLike) -> NDArray[np.complex128]: ...
def SVabc_from_SV012(
    S012: ArrayLike, V012: ArrayLike, n_res: Int | None = None, idx: Int | ArrayLike | None = None
) -> tuple[NDArray[np.complex128], NDArray[np.complex128]]: ...
