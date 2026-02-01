from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def create_ward(
    net: pandapowerNet,
    bus: Int,
    ps_mw: Float,
    qs_mvar: Float,
    pz_mw: Float,
    qz_mvar: Float,
    name: str | None = None,
    in_service: Bool = True,
    index: Int | None = None,
    **kwargs,
) -> np.int64: ...
def create_wards(
    net: pandapowerNet,
    buses: Collection[Int],
    ps_mw: ScalarOrVector[Float],
    qs_mvar: ScalarOrVector[Float],
    pz_mw: ScalarOrVector[Float],
    qz_mvar: ScalarOrVector[Float],
    name: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    index: Collection[Int] | None = None,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_xward(
    net: pandapowerNet,
    bus: Int,
    ps_mw: Float,
    qs_mvar: Float,
    pz_mw: Float,
    qz_mvar: Float,
    r_ohm: Float,
    x_ohm: Float,
    vm_pu: Float,
    in_service: Bool = True,
    name: str | None = None,
    index: Int | None = None,
    slack_weight: Float = 0.0,
    **kwargs,
) -> np.int64: ...
