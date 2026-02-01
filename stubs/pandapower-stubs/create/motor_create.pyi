import numpy as np

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet

def create_motor(
    net: pandapowerNet,
    bus: Int,
    pn_mech_mw: Float,
    cos_phi: Float,
    efficiency_percent: Float = 100.0,
    loading_percent: Float = 100.0,
    name: str | None = None,
    lrc_pu: Float = ...,
    scaling: Float = 1.0,
    vn_kv: Float = ...,
    rx: Float = ...,
    index: Int | None = None,
    in_service: Bool = True,
    cos_phi_n: Float = ...,
    efficiency_n_percent: Float = ...,
    **kwargs,
) -> np.int64: ...
