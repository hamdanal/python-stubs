from _typeshed import Incomplete
from typing import Literal, overload

from pandapower.auxiliary import pandapowerNet

@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    *,
    separation_by_sub: Literal[True],
    **kwargs: Incomplete,
) -> tuple[pandapowerNet, pandapowerNet]: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    separation_by_sub: Literal[False] = False,
    **kwargs: Incomplete,
) -> pandapowerNet: ...
@overload
def mv_oberrhein(
    scenario: Literal["load", "generation"] = "load",
    cosphi_load: float = 0.98,
    cosphi_pv: float = 1,
    include_substations: bool = False,
    separation_by_sub: bool = False,
    **kwargs: Incomplete,
) -> pandapowerNet | tuple[pandapowerNet, pandapowerNet]: ...
