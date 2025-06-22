from typing import Literal, overload
from typing_extensions import Unpack

from pandapower._typing import Float, FromJsonKwds
from pandapower.auxiliary import pandapowerNet

@overload
def mv_oberrhein(  # separation_by_sub=True positional
    scenario: Literal["load", "generation"],
    cosphi_load: Float,
    cosphi_pv: Float,
    include_substations: bool,
    separation_by_sub: Literal[True],
    **kwargs: Unpack[FromJsonKwds],
) -> tuple[pandapowerNet, pandapowerNet]: ...
@overload
def mv_oberrhein(  # separation_by_sub=True keyword
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: Float = 0.98,
    cosphi_pv: Float = 1.0,
    include_substations: bool = False,
    *,
    separation_by_sub: Literal[True],
    **kwargs: Unpack[FromJsonKwds],
) -> tuple[pandapowerNet, pandapowerNet]: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: Float = 0.98,
    cosphi_pv: Float = 1.0,
    include_substations: bool = False,
    separation_by_sub: Literal[False] = False,
    **kwargs: Unpack[FromJsonKwds],
) -> pandapowerNet: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: Float = 0.98,
    cosphi_pv: Float = 1.0,
    include_substations: bool = False,
    separation_by_sub: bool = False,
    **kwargs: Unpack[FromJsonKwds],
) -> pandapowerNet | tuple[pandapowerNet, pandapowerNet]: ...
