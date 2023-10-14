from typing import Literal

import pandas as pd
from pandapower.auxiliary import pandapowerNet

def add_gen_order(gen_order: dict[str, tuple[int, int]], element: str, _is_elements: pd.Series[bool], f: int) -> int: ...
def add_element_to_gen(
    net: pandapowerNet,
    ppc,
    element: Literal["ext_grid", "gen", "sgen_controllable", "load_controllable", "storage_controllable", "xward"],
    f: int,
    t: int,
) -> None: ...
def add_q_constraints(
    net: pandapowerNet, element: str, is_element, ppc, f: int, t: int, delta, inverted: bool = False
) -> None: ...
def add_p_constraints(
    net: pandapowerNet, element: str, is_element, ppc, f: int, t: int, delta, inverted: bool = False
) -> None: ...
