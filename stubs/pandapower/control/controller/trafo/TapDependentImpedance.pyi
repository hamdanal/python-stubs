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
        trafotable: str = ...,
        output_variable: str = ...,
        tol: float = ...,
        restore: bool = ...,
        in_service: bool = ...,
        order: int = ...,
        level: int = ...,
        drop_same_existing_ctrl: bool = ...,
        matching_params: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    def finalize_control(self, net) -> None: ...
