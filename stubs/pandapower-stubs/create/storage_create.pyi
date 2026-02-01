from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def create_storage(
    net: pandapowerNet,
    bus: Int,
    p_mw: Float,
    max_e_mwh: Float,
    q_mvar: Float = 0,
    sn_mva: Float = ...,
    soc_percent: Float = ...,
    min_e_mwh: Float = 0.0,
    name: str | None = None,
    index: Int | None = None,
    scaling: Float = 1.0,
    type: str | None = None,
    in_service: Bool = True,
    max_p_mw: Float = ...,
    min_p_mw: Float = ...,
    max_q_mvar: Float = ...,
    min_q_mvar: Float = ...,
    controllable: Bool | float = ...,  # float because default value is nan
    **kwargs,
) -> np.int64: ...
def create_storages(
    net: pandapowerNet,
    buses: Collection[Int],
    p_mw: ScalarOrVector[Float],
    max_e_mwh: ScalarOrVector[Float],
    q_mvar: ScalarOrVector[Float] = 0,
    sn_mva: ScalarOrVector[Float] = ...,
    soc_percent: ScalarOrVector[Float] = ...,
    min_e_mwh: ScalarOrVector[Float] = 0.0,
    name: ScalarOrVector[str] | None = None,
    index: Collection[Int] | None = None,
    scaling: ScalarOrVector[Float] = 1.0,
    type: ScalarOrVector[str] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    max_p_mw: ScalarOrVector[Float] = ...,
    min_p_mw: ScalarOrVector[Float] = ...,
    max_q_mvar: ScalarOrVector[Float] = ...,
    min_q_mvar: ScalarOrVector[Float] = ...,
    controllable: ScalarOrVector[Bool] | float = ...,  # float because default value is nan
    **kwargs,
) -> Array1D[np.int64]: ...
