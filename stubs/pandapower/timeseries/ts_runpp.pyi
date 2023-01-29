from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet
from pandapower.pypower.idx_brch import (
    BR_B as BR_B,
    BR_R as BR_R,
    BR_STATUS as BR_STATUS,
    BR_X as BR_X,
    F_BUS as F_BUS,
    RATE_A as RATE_A,
    SHIFT as SHIFT,
    T_BUS as T_BUS,
    TAP as TAP,
)
from pandapower.results_bus import write_pq_results_to_element as write_pq_results_to_element
from pandapower.timeseries.output_writer import OutputWriter as OutputWriter

class TimeSeriesRunpp:
    net: pandapowerNet
    output_writer: OutputWriter
    update_pq: bool
    update_trafo: bool
    def __init__(self, net: pandapowerNet) -> None: ...
    ppc: Incomplete | None
    V: Incomplete | None
    def ts_newtonpf(self, net: pandapowerNet) -> pandapowerNet: ...
    def get_branch_results(self, net: pandapowerNet, ppc: Incomplete, branch_update: Incomplete) -> None: ...
    Ibus: Incomplete | None
    def init_timeseries_newton(self) -> pandapowerNet: ...
    def cleanup(self) -> None: ...
    def ts_runpp(self, net: pandapowerNet, **kwargs: Incomplete) -> pandapowerNet: ...
    baseMVA: Incomplete | None
    ref: Incomplete | None
    pv: Incomplete | None
    pq: Incomplete | None
    ppci: Incomplete | None
    Ybus: Incomplete | None
    Yf: Incomplete | None
    Yt: Incomplete | None
    Cg: Incomplete | None
    def init_newton_variables(self) -> None: ...
    def update_trafos(self) -> None: ...
    def get_update_ctrl(self) -> None: ...
