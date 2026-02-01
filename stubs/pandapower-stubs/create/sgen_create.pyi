from collections.abc import Collection
from typing import Literal

import numpy as np

from pandapower._typing import Array1D, Bool, Float, Int, ScalarOrVector
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import GeneratorType

def create_sgen(
    net: pandapowerNet,
    bus: Int,
    p_mw: Float,
    q_mvar: Float = 0,
    sn_mva: Float = ...,
    name: str | None = None,
    index: Int | None = None,
    scaling: Float = 1.0,
    type: Literal["wye", "delta", "motor"] | None = "wye",  # TODO: is "motor" valid here?
    in_service: Bool = True,
    max_p_mw: Float = ...,
    min_p_mw: Float = ...,
    max_q_mvar: Float = ...,
    min_q_mvar: Float = ...,
    controllable: Bool | float = ...,  # float because default value is nan
    k: Float = ...,
    rx: Float = ...,
    id_q_capability_characteristic: Int | None = None,
    reactive_capability_curve: Bool = False,
    curve_style: str | None = None,
    current_source: Bool = True,
    generator_type: GeneratorType | None = None,
    max_ik_ka: Float = ...,
    kappa: Float = ...,
    lrc_pu: Float = ...,
    **kwargs,
) -> np.int64: ...
def create_sgens(
    net: pandapowerNet,
    buses: Collection[Int],
    p_mw: ScalarOrVector[Float],
    q_mvar: ScalarOrVector[Float] = 0,
    sn_mva: ScalarOrVector[Float] = ...,
    name: ScalarOrVector[str] | None = None,
    index: Collection[Int] | None = None,
    scaling: ScalarOrVector[Float] = 1.0,
    type: ScalarOrVector[Literal["wye", "delta", "motor"]] | None = "wye",
    in_service: ScalarOrVector[Bool] = True,
    max_p_mw: ScalarOrVector[Float] = ...,
    min_p_mw: ScalarOrVector[Float] = ...,
    max_q_mvar: ScalarOrVector[Float] = ...,
    min_q_mvar: ScalarOrVector[Float] = ...,
    controllable: ScalarOrVector[Bool] | float = ...,  # float because default value is nan
    k: ScalarOrVector[Float] = ...,
    rx: ScalarOrVector[Float] = ...,
    id_q_capability_characteristic: ScalarOrVector[Int] | None = None,
    reactive_capability_curve: ScalarOrVector[Bool] = False,
    curve_style: ScalarOrVector[str] | None = None,
    current_source: ScalarOrVector[Bool] = True,
    generator_type: ScalarOrVector[GeneratorType] = "current_source",
    max_ik_ka: ScalarOrVector[Float] = ...,
    kappa: ScalarOrVector[Float] = ...,
    lrc_pu: ScalarOrVector[Float] = ...,
    **kwargs,
) -> Array1D[np.int64]: ...
def create_asymmetric_sgen(
    net: pandapowerNet,
    bus: Int,
    p_a_mw: Float = 0,
    p_b_mw: Float = 0,
    p_c_mw: Float = 0,
    q_a_mvar: Float = 0,
    q_b_mvar: Float = 0,
    q_c_mvar: Float = 0,
    sn_mva: Float = ...,
    name: str | None = None,
    index: Int | None = None,
    scaling: Float = 1.0,
    type: Literal["wye", "delta"] = "wye",
    in_service: Bool = True,
    **kwargs,
) -> np.int64: ...
def create_sgen_from_cosphi(
    net: pandapowerNet, bus: Int, sn_mva: Float, cos_phi: Float, mode: Literal["underexcited", "overexcited"], **kwargs
) -> np.int64: ...
