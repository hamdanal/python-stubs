from _typeshed import Incomplete
from collections.abc import Collection
from typing import Literal, TypeVar

import numpy as np
from numpy.typing import NDArray

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

_T = TypeVar("_T")

def ds_find(ar, bus): ...
def ds_union(ar, bus1: Int, bus2: Int, bus_is_pv, bus_is_active, merged_bus) -> None: ...
def ds_create(
    ar,
    switch_bus: Collection[Int],
    switch_elm: Collection[Int],
    switch_et_bus: Collection[Int],
    switch_closed: Collection[Bool],
    switch_z_ohm: Collection[Float],
    bus_is_pv,
    bus_is_active,
    bus_in_service,
    merged_bus,
) -> None: ...
def fill_bus_lookup(ar, bus_lookup, bus_index: Collection[Int]) -> None: ...
def create_bus_lookup_numba(
    net: pandapowerNet, bus_index: Collection[Int], bus_is_idx: ScalarOrVector[Int]
) -> tuple[Array1D[np.int64], Array1D[np.bool]]: ...

class DisjointSet(dict[_T, _T]):
    def add(self, item: _T) -> None: ...
    def find(self, item: _T) -> _T: ...
    def union(self, item1: _T, item2: _T) -> None: ...

def create_consecutive_bus_lookup(net: pandapowerNet, bus_index: Collection[Int]) -> Array1D[np.int64]: ...
def create_bus_lookup_numpy(
    net: pandapowerNet, bus_index: Collection[Int], closed_bb_switch_mask: NDArray[np.bool]
) -> tuple[Array1D[np.int64], Array1D[np.bool]]: ...
def create_bus_lookup(
    net: pandapowerNet, bus_index: Collection[Int], bus_is_idx: ScalarOrVector[Int], numba: Bool
) -> tuple[Array1D[np.int64], Array1D[np.bool]]: ...
def get_voltage_init_vector(
    net: pandapowerNet, init_v, mode: Literal["magnitude", "angle"], sequence: Incomplete | None = None
): ...
def set_reference_buses(net: pandapowerNet, ppc, bus_lookup, mode: str) -> None: ...
def set_reference_buses_dc(net: pandapowerNet, ppc, bus_lookup, mode: str) -> None: ...
