from _typeshed import Incomplete
from typing import Literal

from pandapower.auxiliary import pandapowerNet

def ieee_european_lv_asymmetric(
    scenario: Literal["off_peak_1", "on_peak_566", "off_peak_1440"] = "on_peak_566", **kwargs: Incomplete
) -> pandapowerNet: ...
