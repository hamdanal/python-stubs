from typing import Literal
from typing_extensions import Unpack

from pandapower.auxiliary import pandapowerNet
from pandapower.file_io import _FromJsonKwds

def ieee_european_lv_asymmetric(
    scenario: Literal["off_peak_1", "on_peak_566", "off_peak_1440"] = "on_peak_566", **kwargs: Unpack[_FromJsonKwds]
) -> pandapowerNet: ...
