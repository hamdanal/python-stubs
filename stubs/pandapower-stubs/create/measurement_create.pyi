import numpy as np

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet
from pandapower.pp_types import HVMVLVType, MeasurementElementType, MeasurementType

def create_measurement(
    net: pandapowerNet,
    meas_type: MeasurementType,
    element_type: MeasurementElementType,
    value: Float,
    std_dev: Float,
    element: Int,
    side: HVMVLVType | Int | None = None,
    check_existing: Bool = False,
    index: Int | None = None,
    name: str | None = None,
    **kwargs,
) -> np.int64: ...
