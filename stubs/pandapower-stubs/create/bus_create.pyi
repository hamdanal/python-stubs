from collections.abc import Collection
from typing import Final

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import BusType

BUSBAR_WARNING: Final[str]

def create_bus(
    net: pandapowerNet,
    vn_kv: Float,
    name: str | None = None,
    index: Int | None = None,
    geodata: tuple[Float, Float] | None = None,
    type: BusType = "b",
    zone: str | None = None,
    in_service: Bool = True,
    max_vm_pu: Float = ...,
    min_vm_pu: Float = ...,
    coords: Collection[tuple[Float, Float]] | None = None,
    **kwargs,
) -> np.int64: ...
def create_bus_dc(
    net: pandapowerNet,
    vn_kv: Float,
    name: str | None = None,
    index: Int | None = None,
    geodata: tuple[Float, Float] | None = None,
    type: BusType = "b",
    zone: str | None = None,
    in_service: Bool | None = True,
    max_vm_pu: Float = ...,
    min_vm_pu: Float = ...,
    coords: Collection[tuple[Float, Float]] | None = None,
    **kwargs,
) -> np.int64: ...
def create_buses(
    net: pandapowerNet,
    nr_buses: Int,
    vn_kv: ScalarOrVector[Float],
    index: ScalarOrVector[Int] | None = None,
    name: ScalarOrVector[str] | None = None,
    type: ScalarOrVector[BusType] = "b",
    geodata: ScalarOrVector[tuple[Float, Float]] | None = None,
    zone: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    max_vm_pu: ScalarOrVector[Float] = ...,
    min_vm_pu: ScalarOrVector[Float] = ...,
    coords: ScalarOrVector[Collection[tuple[Float, Float]]] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_buses_dc(
    net: pandapowerNet,
    nr_buses_dc: Int,
    vn_kv: ScalarOrVector[Float],
    index: ScalarOrVector[Int] | None = None,
    name: ScalarOrVector[str] | None = None,
    type: ScalarOrVector[BusType] = "b",
    geodata: ScalarOrVector[tuple[Float, Float]] | None = None,
    zone: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    max_vm_pu: ScalarOrVector[Float] = ...,
    min_vm_pu: ScalarOrVector[Float] = ...,
    coords: ScalarOrVector[Collection[tuple[Float, Float]]] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
