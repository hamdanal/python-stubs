from typing import Literal

from pandapower.auxiliary import pandapowerNet

def create_synthetic_voltage_control_lv_network(
    network_class: Literal["rural_1", "rural_2", "village_1", "village_2", "suburb_1"] = "rural_1"
) -> pandapowerNet: ...
