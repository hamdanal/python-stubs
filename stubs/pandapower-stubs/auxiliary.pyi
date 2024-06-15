from _typeshed import _KT, _VT, Incomplete
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence, Sized
from typing import Any, NoReturn, SupportsInt, TypeVar
from typing_extensions import Self

import numpy as np
import pandas as pd
from numpy.typing import ArrayLike, NDArray

from pandapower.std_types import _StdTypes

_T = TypeVar("_T")

def soft_dependency_error(fct_name: str, required_packages: str | Iterable[str]) -> NoReturn: ...
def warn_and_fix_parameter_renaming(
    old_parameter_name: str, new_parameter_name: str, new_parameter: _T, default_value: _T, category: Warning = ..., **kwargs: Any
) -> _T: ...

class ADict(dict[_KT, _VT], MutableMapping[_KT, _VT]):
    def __call__(self, key: _KT) -> _VT: ...

class pandapowerNet(ADict[str, pd.DataFrame]):
    # These attributes are not defined in the class body, but are added dynamically
    asymmetric_load: pd.DataFrame
    asymmetric_sgen: pd.DataFrame
    bus: pd.DataFrame
    bus_geodata: pd.DataFrame
    characteristic: pd.DataFrame
    controller: pd.DataFrame
    converged: bool
    dcline: pd.DataFrame
    ext_grid: pd.DataFrame
    f_hz: float
    format_version: str
    gen: pd.DataFrame
    group: pd.DataFrame
    impedance: pd.DataFrame
    line: pd.DataFrame
    line_geodata: pd.DataFrame
    load: pd.DataFrame
    measurement: pd.DataFrame
    motor: pd.DataFrame
    name: str
    poly_cost: pd.DataFrame
    pwl_cost: pd.DataFrame
    res_asymmetric_load: pd.DataFrame
    res_asymmetric_load_3ph: pd.DataFrame
    res_asymmetric_sgen: pd.DataFrame
    res_asymmetric_sgen_3ph: pd.DataFrame
    res_bus: pd.DataFrame
    res_bus_3ph: pd.DataFrame
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
    res_storage: pd.DataFrame
    res_storage_3ph: pd.DataFrame
    res_switch: pd.DataFrame
    res_switch_est: pd.DataFrame
    res_switch_sc: pd.DataFrame
    res_trafo: pd.DataFrame
    res_trafo3w: pd.DataFrame
    res_trafo3w_est: pd.DataFrame
    res_trafo3w_sc: pd.DataFrame
    res_trafo_3ph: pd.DataFrame
    res_trafo_est: pd.DataFrame
    res_trafo_sc: pd.DataFrame
    res_ward: pd.DataFrame
    res_xward: pd.DataFrame
    sgen: pd.DataFrame
    shunt: pd.DataFrame
    sn_mva: float
    std_types: _StdTypes
    storage: pd.DataFrame
    switch: pd.DataFrame
    trafo: pd.DataFrame
    trafo3w: pd.DataFrame
    user_pf_options: dict[Incomplete, Incomplete]
    version: str
    ward: pd.DataFrame
    xward: pd.DataFrame
    def deepcopy(self) -> Self: ...
    # Account for dynamic attributes
    def __getattr__(self, name: str) -> Any: ...

def get_free_id(df: Sized) -> int: ...

class ppException(Exception): ...

def get_indices(
    selection: Iterable[int], lookup: Mapping[int, int] | Mapping[str, Mapping[int, int]], fused_indices: bool = True
) -> NDArray[np.int_]: ...
def ensure_iterability(var: _T | Iterable[_T], len_: int | None = None) -> Iterable[_T]: ...
def get_values(source: Incomplete, selection: Iterable[SupportsInt], lookup: Mapping[int, int]) -> NDArray[np.int_]: ...
def set_elements_oos(ti: Sized, tis: Incomplete, bis: Incomplete, lis: MutableSequence[bool]) -> None: ...
def set_isolated_buses_oos(
    bus_in_service: MutableSequence[bool], ppc_bus_isolated: Incomplete, bus_lookup: Incomplete
) -> None: ...
def X012_to_X0(X012: ArrayLike) -> NDArray[np.complex128]: ...
def X012_to_X1(X012: ArrayLike) -> NDArray[np.complex128]: ...
def X012_to_X2(X012: ArrayLike) -> NDArray[np.complex128]: ...
def combine_X012(X0: ArrayLike, X1: ArrayLike, X2: ArrayLike) -> NDArray[np.complex128]: ...
def phase_shift_unit_operator(angle_deg: float) -> float: ...

a: float
asq: float
Tabc: NDArray[np.float64]
T012: NDArray[np.float64]

def sequence_to_phase(X012: ArrayLike) -> NDArray[np.float64]: ...
def phase_to_sequence(Xabc: ArrayLike) -> NDArray[np.float64]: ...
def I0_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def I1_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def I2_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[np.complex128]: ...
def V1_from_ppc(ppc: Mapping[str, ArrayLike]) -> NDArray[np.complex128]: ...
def V_from_I(Y: ArrayLike, I: ArrayLike) -> NDArray[np.complex128]: ...
def I_from_V(Y: ArrayLike, V: ArrayLike) -> NDArray[np.complex128]: ...
def S_from_VI_elementwise(V: ArrayLike, I: ArrayLike) -> NDArray[np.complex128]: ...
def I_from_SV_elementwise(S: ArrayLike, V: ArrayLike) -> NDArray[np.complex128]: ...
def SVabc_from_SV012(
    S012: ArrayLike, V012: ArrayLike, n_res: int | None = None, idx: int | ArrayLike | None = None
) -> tuple[NDArray[np.complex128], NDArray[np.complex128]]: ...
