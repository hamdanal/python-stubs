from _typeshed import Incomplete
from typing import Any, Literal

import pandas as pd

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet
from pandapower.protection.basic_protection_device import ProtectionDevice

class OCRelay(ProtectionDevice):
    switch_index: Incomplete
    oc_relay_type: Incomplete
    time_settings: Incomplete
    overload_factor: Incomplete
    ct_current_factor: Incomplete
    safety_factor: Incomplete
    inverse_overload_factor: Incomplete
    pickup_current_manual: Incomplete
    sc_fraction: Incomplete
    curve_type: Incomplete
    kwargs: Incomplete

    activation_parameter: Incomplete
    tripped: Incomplete
    I_g: Incomplete
    I_gg: Incomplete
    I_s: Incomplete
    time_grading: Incomplete
    t_g: Incomplete
    t_gg: Incomplete
    t_grade: Incomplete
    tms: Incomplete
    def __init__(
        self,
        net: pandapowerNet,
        switch_index: Int,
        oc_relay_type: str,
        time_settings,
        overload_factor: Float = 1.2,
        ct_current_factor: Float = 1.25,
        safety_factor: Float = 1,
        inverse_overload_factor: Float = 1.2,
        pickup_current_manual: pd.DataFrame | None = None,
        in_service: Bool = True,
        overwrite: Bool = True,
        sc_fraction: Float = 0.95,
        curve_type: str = "standard_inverse",
        **kwargs,
    ) -> None: ...
    def create_protection_function(self, net: pandapowerNet) -> None: ...
    def reset_device(self) -> None: ...
    def has_tripped(self) -> bool: ...
    def status_to_net(self, net: pandapowerNet) -> None: ...
    def protection_function(self, net: pandapowerNet, scenario: Literal["sc", "pp"]) -> dict[str, Any]: ...
    def plot_protection_characteristic(
        self,
        net: pandapowerNet,
        num: Int = 60,
        xlabel: str = "I [A]",
        ylabel: str = "time [s]",
        xmin: Float = 10,
        xmax: Float = 10000,
        ymin: Float = 0.01,
        ymax: Float = 10000,
        title: str = "Time-Current Characteristic of OC Relay ",
    ) -> None: ...

def time_grading(net: pandapowerNet, time_settings) -> pd.DataFrame: ...
