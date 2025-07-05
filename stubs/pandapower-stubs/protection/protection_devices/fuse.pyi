from typing import Any, Literal

from pandapower._typing import Bool, Float, Int
from pandapower.auxiliary import pandapowerNet
from pandapower.protection.basic_protection_device import ProtectionDevice

class Fuse(ProtectionDevice):
    switch_index: Int
    fuse_type: str
    in_service: bool
    name: str
    rated_i_a: float
    characteristic_index: int
    i_start_a: float | None = None
    i_stop_a: float | None = None
    activation_parameter: str
    tripped: bool
    z_ohm: float
    def __init__(
        self,
        net: pandapowerNet,
        switch_index: Int,
        fuse_type: str = "none",
        rated_i_a: Float = 0,
        characteristic_index: Int | None = None,
        in_service: Bool = True,
        overwrite: Bool = False,
        curve_select: Int = 0,
        z_ohm: Float = 0.0001,
        name: str | None = None,
        **kwargs,
    ) -> None: ...
    def create_characteristic(self, net, x_values, y_values, interpolator_kind="Pchip", **kwargs) -> None: ...
    def reset_device(self) -> None: ...
    def has_tripped(self) -> bool: ...
    def status_to_net(self, net: pandapowerNet) -> None: ...
    def protection_function(self, net: pandapowerNet, scenario: Literal["sc", "pp"] = "sc") -> dict[str, Any]: ...
    def plot_protection_characteristic(
        self,
        net: pandapowerNet,
        num: Int = 35,
        xlabel: str = "I [A]",
        ylabel: str = "time [s]",
        title: str = "Time-Current Characteristic of Fuse",
    ) -> None: ...
