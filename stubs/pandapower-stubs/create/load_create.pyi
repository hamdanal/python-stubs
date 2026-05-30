from collections.abc import Collection

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import UnderOverExcitedType, WyeDeltaType

def create_load(
    net: pandapowerNet,
    bus: Int,
    p_mw: Float,
    q_mvar: Float = 0,
    const_z_p_percent: Float = 0,
    const_i_p_percent: Float = 0,
    const_z_q_percent: Float = 0,
    const_i_q_percent: Float = 0,
    sn_mva: Float = ...,
    name: str | None = None,
    scaling: Float = 1.0,
    index: Int | None = None,
    in_service: Bool = True,
    type: WyeDeltaType = "wye",
    max_p_mw: Float = ...,
    min_p_mw: Float = ...,
    max_q_mvar: Float = ...,
    min_q_mvar: Float = ...,
    controllable: Bool | float = ...,  # float because default value is nan
    **kwargs,
) -> np.int64: ...
def create_loads(
    net: pandapowerNet,
    buses: Collection[Int],
    p_mw: ScalarOrVector[Float],
    q_mvar: ScalarOrVector[Float] = 0,
    const_z_p_percent: ScalarOrVector[Float] = 0,
    const_i_p_percent: ScalarOrVector[Float] = 0,
    const_z_q_percent: ScalarOrVector[Float] = 0,
    const_i_q_percent: ScalarOrVector[Float] = 0,
    sn_mva: ScalarOrVector[Float] = ...,
    name: ScalarOrVector[str] | None = None,
    scaling: ScalarOrVector[Float] = 1.0,
    index: Collection[Int] | None = None,
    in_service: ScalarOrVector[Bool] = True,
    type: ScalarOrVector[WyeDeltaType] | None = "wye",
    max_p_mw: ScalarOrVector[Float] = ...,
    min_p_mw: ScalarOrVector[Float] = ...,
    max_q_mvar: ScalarOrVector[Float] = ...,
    min_q_mvar: ScalarOrVector[Float] = ...,
    controllable: ScalarOrVector[Bool] | float = ...,  # float because default value is nan
    **kwargs,
) -> Array1D[np.int64]: ...
def create_asymmetric_load(
    net: pandapowerNet,
    bus: Int,
    p_a_mw: Float = 0,
    p_b_mw: Float = 0,
    p_c_mw: Float = 0,
    q_a_mvar: Float = 0,
    q_b_mvar: Float = 0,
    q_c_mvar: Float = 0,
    sn_a_mva: Float = ...,
    sn_b_mva: Float = ...,
    sn_c_mva: Float = ...,
    sn_mva: Float = ...,
    name: str | None = None,
    scaling: Float = 1.0,
    index: Int | None = None,
    in_service: Bool = True,
    type: WyeDeltaType = "wye",
    **kwargs,
) -> np.int64: ...
def create_load_from_cosphi(
    net: pandapowerNet, bus: Int, sn_mva: Float, cos_phi: Float, mode: UnderOverExcitedType, **kwargs
) -> np.int64: ...
def create_load_dc(
    net: pandapowerNet,
    bus_dc: Int,
    p_dc_mw: Float,
    scaling: Float = 1.0,
    type: str | None = None,
    index: Int | None = None,
    name: str | None = None,
    in_service: Bool = True,
    controllable: Bool = False,
    **kwargs,
) -> np.int64: ...
