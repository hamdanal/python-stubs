import numpy as np

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet

def create_source_dc(
    net: pandapowerNet,
    bus_dc: Int,
    vm_pu: Float = 1.0,
    index: Int | None = None,
    name: str | None = None,
    in_service: Bool = True,
    type: str | None = None,
    **kwargs,
) -> np.int64: ...
