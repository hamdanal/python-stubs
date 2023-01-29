from _typeshed import Incomplete

from pandapower.control.controller.characteristic_control import CharacteristicControl
from pandapower.control.util.characteristic import Characteristic as Characteristic

class VmSetTapControl(CharacteristicControl):
    def __init__(
        self,
        net,
        controller_index,
        characteristic_index,
        variable: str = ...,
        tol: float = ...,
        in_service: bool = ...,
        order: int = ...,
        level: int = ...,
        drop_same_existing_ctrl: bool = ...,
        matching_params: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
