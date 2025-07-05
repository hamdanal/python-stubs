from collections.abc import Collection

from pandapower._typing import Bool, Int, RunPPFunc
from pandapower.auxiliary import pandapowerNet

def create_passive_external_net_for_ward_admittance(
    net: pandapowerNet,
    all_external_buses: Collection[Int],
    boundary_buses: Collection[Int] | object,  # not used!
    calc_volt_angles: Bool = True,
    runpp_fct: RunPPFunc = ...,
    **kwargs,
) -> None: ...
