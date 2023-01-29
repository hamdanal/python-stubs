from _typeshed import Incomplete, StrOrBytesPath, SupportsRead

from pandapower.auxiliary import pandapowerNet

# TODO **kwargs below are those of pp.from_json(path, **kwargs)
def sorted_from_json(path: SupportsRead[str] | StrOrBytesPath, **kwargs: Incomplete) -> pandapowerNet: ...
def case4gs(**kwargs: Incomplete) -> pandapowerNet: ...
def case5(**kwargs: Incomplete) -> pandapowerNet: ...
def case6ww(**kwargs: Incomplete) -> pandapowerNet: ...
def case9(**kwargs: Incomplete) -> pandapowerNet: ...
def case11_iwamoto(**kwargs: Incomplete) -> pandapowerNet: ...
def case14(**kwargs: Incomplete) -> pandapowerNet: ...
def case24_ieee_rts(**kwargs: Incomplete) -> pandapowerNet: ...
def case30(**kwargs: Incomplete) -> pandapowerNet: ...
def case_ieee30(**kwargs: Incomplete) -> pandapowerNet: ...
def case33bw(**kwargs: Incomplete) -> pandapowerNet: ...
def case39(**kwargs: Incomplete) -> pandapowerNet: ...
def case57(
    vn_kv_area1: float = 115,
    vn_kv_area2: float = 500,
    vn_kv_area3: float = 138,
    vn_kv_area4: float = 345,
    vn_kv_area5: float = 230,
    vn_kv_area6: float = 161,
    **kwargs: Incomplete,
) -> pandapowerNet: ...
def case89pegase(**kwargs: Incomplete) -> pandapowerNet: ...
def case118(**kwargs: Incomplete) -> pandapowerNet: ...
def case145(**kwargs: Incomplete) -> pandapowerNet: ...
def case_illinois200(**kwargs: Incomplete) -> pandapowerNet: ...
def case300(**kwargs: Incomplete) -> pandapowerNet: ...
def case1354pegase(**kwargs: Incomplete) -> pandapowerNet: ...
def case1888rte(ref_bus_idx: int = ..., **kwargs: Incomplete) -> pandapowerNet: ...
def case2848rte(ref_bus_idx: int = ..., **kwargs: Incomplete) -> pandapowerNet: ...
def case2869pegase(**kwargs: Incomplete) -> pandapowerNet: ...
def case3120sp(**kwargs: Incomplete) -> pandapowerNet: ...
def case6470rte(ref_bus_idx: int = ..., **kwargs: Incomplete) -> pandapowerNet: ...
def case6495rte(ref_bus_idx: Incomplete | None = ..., **kwargs: Incomplete) -> pandapowerNet: ...
def case6515rte(ref_bus_idx: int = ..., **kwargs: Incomplete) -> pandapowerNet: ...
def case9241pegase(**kwargs: Incomplete) -> pandapowerNet: ...
def GBreducednetwork(**kwargs: Incomplete) -> pandapowerNet: ...
def GBnetwork(**kwargs: Incomplete) -> pandapowerNet: ...
def iceland(**kwargs: Incomplete) -> pandapowerNet: ...
