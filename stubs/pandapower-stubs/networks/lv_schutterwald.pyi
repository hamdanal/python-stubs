from typing import Unpack

from pandapower._typing import FromJsonKwds
from pandapower.auxiliary import pandapowerNet

def lv_schutterwald(
    separation_by_sub: bool = False, include_heat_pumps: bool = False, **kwargs: Unpack[FromJsonKwds]
) -> pandapowerNet: ...
