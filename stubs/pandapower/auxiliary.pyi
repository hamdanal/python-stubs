from _typeshed import _KT, _VT, Incomplete
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence, Sized
from typing import Any, NoReturn, SupportsInt, TypeVar
from typing_extensions import Self

from numpy import complexfloating, floating, integer
from numpy.typing import ArrayLike, NDArray
from pandas import DataFrame

_T = TypeVar("_T")

def soft_dependency_error(fct_name: str, required_packages: str | Iterable[str]) -> NoReturn: ...
def warn_and_fix_parameter_renaming(
    old_parameter_name: str, new_parameter_name: str, new_parameter: _T, default_value: _T, category: Warning = ..., **kwargs: Any
) -> _T: ...

class ADict(dict[_KT, _VT], MutableMapping[_KT, _VT]):
    def __call__(self, key: _KT) -> _VT: ...

class pandapowerNet(ADict[str, DataFrame]):
    # These attributes are not defined in the class body, but are added dynamically
    asymmetric_load: DataFrame
    asymmetric_sgen: DataFrame
    bus: DataFrame
    bus_geodata: DataFrame
    characteristic: DataFrame
    controller: DataFrame
    converged: bool
    dcline: DataFrame
    ext_grid: DataFrame
    f_hz: float
    format_version: str
    gen: DataFrame
    group: DataFrame
    impedance: DataFrame
    line: DataFrame
    line_geodata: DataFrame
    load: DataFrame
    measurement: DataFrame
    motor: DataFrame
    name: str
    poly_cost: DataFrame
    pwl_cost: DataFrame
    res_asymmetric_load: DataFrame
    res_asymmetric_load_3ph: DataFrame
    res_asymmetric_sgen: DataFrame
    res_asymmetric_sgen_3ph: DataFrame
    res_bus: DataFrame
    res_bus_3ph: DataFrame
    res_bus_est: DataFrame
    res_bus_sc: DataFrame
    res_dcline: DataFrame
    res_ext_grid: DataFrame
    res_ext_grid_3ph: DataFrame
    res_ext_grid_sc: DataFrame
    res_gen: DataFrame
    res_gen_sc: DataFrame
    res_impedance: DataFrame
    res_impedance_est: DataFrame
    res_line: DataFrame
    res_line_3ph: DataFrame
    res_line_est: DataFrame
    res_line_sc: DataFrame
    res_load: DataFrame
    res_load_3ph: DataFrame
    res_motor: DataFrame
    res_sgen: DataFrame
    res_sgen_3ph: DataFrame
    res_sgen_sc: DataFrame
    res_shunt: DataFrame
    res_shunt_3ph: DataFrame
    res_storage: DataFrame
    res_storage_3ph: DataFrame
    res_switch: DataFrame
    res_switch_est: DataFrame
    res_switch_sc: DataFrame
    res_trafo: DataFrame
    res_trafo3w: DataFrame
    res_trafo3w_est: DataFrame
    res_trafo3w_sc: DataFrame
    res_trafo_3ph: DataFrame
    res_trafo_est: DataFrame
    res_trafo_sc: DataFrame
    res_ward: DataFrame
    res_xward: DataFrame
    sgen: DataFrame
    shunt: DataFrame
    sn_mva: float
    std_types: dict[str, dict[str, Incomplete]]
    storage: DataFrame
    switch: DataFrame
    trafo: DataFrame
    trafo3w: DataFrame
    user_pf_options: dict[Incomplete, Incomplete]
    version: str
    ward: DataFrame
    xward: DataFrame
    def deepcopy(self) -> Self: ...

def get_free_id(df: Sized) -> int: ...

class ppException(Exception): ...

def get_indices(
    selection: Iterable[int], lookup: Mapping[int, int] | Mapping[str, Mapping[int, int]], fused_indices: bool = ...
) -> NDArray[integer]: ...
def ensure_iterability(var: _T | Iterable[_T], len_: int | None = ...) -> Iterable[_T]: ...
def get_values(source: Incomplete, selection: Iterable[SupportsInt], lookup: Mapping[int, int]) -> NDArray[integer]: ...
def set_elements_oos(ti: Sized, tis: Incomplete, bis: Incomplete, lis: MutableSequence[bool]) -> None: ...
def set_isolated_buses_oos(
    bus_in_service: MutableSequence[bool], ppc_bus_isolated: Incomplete, bus_lookup: Incomplete
) -> None: ...
def X012_to_X0(X012: ArrayLike) -> NDArray[complexfloating]: ...
def X012_to_X1(X012: ArrayLike) -> NDArray[complexfloating]: ...
def X012_to_X2(X012: ArrayLike) -> NDArray[complexfloating]: ...
def combine_X012(X0: ArrayLike, X1: ArrayLike, X2: ArrayLike) -> NDArray[complexfloating]: ...
def phase_shift_unit_operator(angle_deg: float) -> float: ...

a: float
asq: float
Tabc: NDArray[floating]
T012: NDArray[floating]

def sequence_to_phase(X012: ArrayLike) -> NDArray[floating]: ...
def phase_to_sequence(Xabc: ArrayLike) -> NDArray[floating]: ...
def I0_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[complexfloating]: ...
def I1_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[complexfloating]: ...
def I2_from_V012(V012: ArrayLike, Y: ArrayLike) -> NDArray[complexfloating]: ...
def V1_from_ppc(ppc: Mapping[str, ArrayLike]) -> NDArray[complexfloating]: ...
def V_from_I(Y: ArrayLike, I: ArrayLike) -> NDArray[complexfloating]: ...
def I_from_V(Y: ArrayLike, V: ArrayLike) -> NDArray[complexfloating]: ...
def S_from_VI_elementwise(V: ArrayLike, I: ArrayLike) -> NDArray[complexfloating]: ...
def I_from_SV_elementwise(S: ArrayLike, V: ArrayLike) -> NDArray[complexfloating]: ...
def SVabc_from_SV012(
    S012: ArrayLike, V012: ArrayLike, n_res: int | None = ..., idx: int | ArrayLike | None = ...
) -> tuple[NDArray[complexfloating], NDArray[complexfloating]]: ...
