from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet

def create_gen(
    net: pandapowerNet,
    bus: Int,
    p_mw: Float,
    vm_pu: Float = 1.0,
    sn_mva: Float = ...,
    name: str | None = None,
    index: Int | None = None,
    max_q_mvar: Float = ...,
    min_q_mvar: Float = ...,
    min_p_mw: Float = ...,
    max_p_mw: Float = ...,
    min_vm_pu: Float = ...,
    max_vm_pu: Float = ...,
    scaling: Float = 1.0,
    type: str | None = None,
    slack: Bool = False,
    id_q_capability_characteristic: Int | None = None,
    reactive_capability_curve: Bool = False,
    curve_style: str | None = None,
    controllable: Bool | float = ...,  # float because default value is nan
    vn_kv: Float = ...,
    xdss_pu: Float = ...,
    rdss_ohm: Float = ...,
    cos_phi: Float = ...,
    pg_percent: Float = ...,
    power_station_trafo: Int | float = ...,  # float because default value is nan
    in_service: Bool = True,
    slack_weight: Float = 0.0,
    **kwargs,
) -> np.int64: ...
def create_gens(
    net: pandapowerNet,
    buses: Collection[Int],
    p_mw: ScalarOrVector[Float],
    vm_pu: ScalarOrVector[Float] = 1.0,
    sn_mva: ScalarOrVector[Float] = ...,
    name: ScalarOrVector[str] | None = None,
    index: Collection[Int] | None = None,
    max_q_mvar: ScalarOrVector[Float] = ...,
    min_q_mvar: ScalarOrVector[Float] = ...,
    min_p_mw: ScalarOrVector[Float] = ...,
    max_p_mw: ScalarOrVector[Float] = ...,
    min_vm_pu: ScalarOrVector[Float] = ...,
    max_vm_pu: ScalarOrVector[Float] = ...,
    scaling: ScalarOrVector[Float] = 1.0,
    type: ScalarOrVector[str] | None = None,
    slack: ScalarOrVector[Bool] = False,
    id_q_capability_characteristic: ScalarOrVector[Int] | None = None,
    reactive_capability_curve: ScalarOrVector[Bool] = False,
    curve_style: ScalarOrVector[str] | None = None,
    controllable: ScalarOrVector[Bool] | float = ...,  # float because default value is nan
    vn_kv: ScalarOrVector[Float] = ...,
    xdss_pu: ScalarOrVector[Float] = ...,
    rdss_ohm: ScalarOrVector[Float] = ...,
    cos_phi: ScalarOrVector[Float] = ...,
    pg_percent: ScalarOrVector[Float] = ...,
    power_station_trafo: ScalarOrVector[Int] | float = ...,  # float because default value is nan
    in_service: ScalarOrVector[Bool] = True,
    slack_weight: ScalarOrVector[Float] = 0.0,
    **kwargs,
) -> Array1D[np.int64]: ...
