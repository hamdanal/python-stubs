from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.characteristic_control import CharacteristicControl

class TapDependentImpedance(CharacteristicControl):
    restore: bool
    initial_values: Incomplete
    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        characteristic_index,
        element: str = "trafo",
        output_variable: str = "vk_percent",
        tol: float = 0.001,
        restore: bool = True,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def finalize_control(self, net: pandapowerNet) -> None: ...
