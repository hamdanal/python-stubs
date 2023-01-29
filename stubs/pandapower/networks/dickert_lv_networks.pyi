from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Literal

from pandapower.auxiliary import pandapowerNet

def create_dickert_lv_feeders(
    net: pandapowerNet,
    busbar_index: int,
    feeders_range: Literal["short", "middle", "long"] = "short",
    linetype: Literal["cable", "C&OHL"] = "cable",
    customer: Literal["single", "multiple"] = "single",
    case: Literal["good", "average", "worse"] = "good",
) -> None: ...
def create_dickert_lv_network(
    feeders_range: Literal["short", "middle", "long"] = "short",
    linetype: Literal["cable", "C&OHL"] = "cable",
    customer: Literal["single", "multiple"] = "single",
    case: Literal["good", "average", "worse"] = "good",
    trafo_type_name: str = "0.4 MVA 20/0.4 kV",
    trafo_type_data: Mapping[Incomplete, Incomplete] | None = ...,
) -> pandapowerNet: ...
