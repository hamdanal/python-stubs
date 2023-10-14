from _typeshed import Incomplete

from pandapower.control.controller.characteristic_control import CharacteristicControl
from pandapower.control.util.characteristic import Characteristic as Characteristic

class TapDependentImpedance(CharacteristicControl):
    restore: Incomplete
    initial_values: Incomplete
    def __init__(
        self,
        net,
        transformer_index,
        characteristic_index,
        trafotable: str = "trafo",
        output_variable: str = "vk_percent",
        tol: float = 0.001,
        restore: bool = True,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    def finalize_control(self, net) -> None: ...
