from collections.abc import Collection
from typing import Literal

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def create_switch(
    net: pandapowerNet,
    bus: Int,
    element: Int,
    et: Literal["l", "t", "t3", "b"],
    closed: Bool = True,
    type: Literal["LS", "CB", "LBS", "DS"] | None = None,
    name: str | None = None,
    index: Int | None = None,
    z_ohm: Float = 0,
    in_ka: Float | None = ...,
    **kwargs,
) -> np.int64: ...
def create_switches(
    net: pandapowerNet,
    buses: Collection[Int],
    elements: Collection[Int],
    et: ScalarOrVector[Literal["l", "t", "t3", "b"]],
    closed: ScalarOrVector[Bool] = True,
    type: ScalarOrVector[Literal["LS", "CB", "LBS", "DS"]] | None = None,
    name: ScalarOrVector[str] | None = None,
    index: Collection[Int] | None = None,
    z_ohm: ScalarOrVector[Float] = 0,
    in_ka: ScalarOrVector[Float] | None = ...,
    **kwargs,
) -> Array1D[np.int64]: ...
