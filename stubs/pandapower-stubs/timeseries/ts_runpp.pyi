from _typeshed import Incomplete, Unused

from pandapower.auxiliary import pandapowerNet
from pandapower.timeseries.output_writer import OutputWriter

class TimeSeriesRunpp:
    net: pandapowerNet
    output_writer: OutputWriter[Incomplete]
    update_pq: bool
    update_trafo: bool
    baseMVA: Incomplete | None
    ref: Incomplete | None
    pv: Incomplete | None
    pq: Incomplete | None
    V: Incomplete | None
    ppc: Incomplete | None
    ppci: Incomplete | None
    Ybus: Incomplete | None
    Yf: Incomplete | None
    Yt: Incomplete | None
    Ibus: Incomplete | None
    Cg: Incomplete | None
    def __init__(self, net: pandapowerNet) -> None: ...
    def ts_newtonpf(self, net: pandapowerNet) -> pandapowerNet: ...
    def get_branch_results(self, net: pandapowerNet, ppc: Incomplete, branch_update: Incomplete) -> None: ...
    def init_timeseries_newton(self) -> pandapowerNet: ...
    def cleanup(self) -> None: ...
    def ts_runpp(self, net: pandapowerNet, **kwargs: Unused) -> pandapowerNet: ...
    def init_newton_variables(self) -> None: ...
    def update_trafos(self) -> None: ...
    def get_update_ctrl(self) -> None: ...
