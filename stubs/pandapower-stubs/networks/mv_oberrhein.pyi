from typing import Literal, overload
from typing_extensions import Unpack

from pandapower.auxiliary import pandapowerNet
from pandapower.file_io import _FromJsonKwds

@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    *,
    separation_by_sub: Literal[True],
    **kwargs: Unpack[_FromJsonKwds],
) -> tuple[pandapowerNet, pandapowerNet]: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    separation_by_sub: Literal[False] = False,
    **kwargs: Unpack[_FromJsonKwds],
) -> pandapowerNet: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    separation_by_sub: bool = False,
    **kwargs: Unpack[_FromJsonKwds],
) -> pandapowerNet | tuple[pandapowerNet, pandapowerNet]: ...
