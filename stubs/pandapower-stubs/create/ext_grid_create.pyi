import numpy as np

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet

def create_ext_grid(
    net: pandapowerNet,
    bus: Int,
    vm_pu: Float = 1.0,
    va_degree: Float = 0.0,
    name: str | None = None,
    in_service: Bool = True,
    s_sc_max_mva: Float = ...,
    s_sc_min_mva: Float = ...,
    rx_max: Float = ...,
    rx_min: Float = ...,
    max_p_mw: Float = ...,
    min_p_mw: Float = ...,
    max_q_mvar: Float = ...,
    min_q_mvar: Float = ...,
    index: Int | None = None,
    r0x0_max: Float = ...,
    x0x_max: Float = ...,
    controllable: Bool | float = ...,  # float because default value is nan
    slack_weight: Float = 1.0,
    **kwargs,
) -> np.int64: ...
