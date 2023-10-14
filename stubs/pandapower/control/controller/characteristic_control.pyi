from _typeshed import Incomplete

from pandapower.control.basic_controller import Controller

class CharacteristicControl(Controller):
    input_element: Incomplete
    input_element_index: Incomplete
    output_element: Incomplete
    output_element_index: Incomplete
    characteristic_index: Incomplete
    tol: Incomplete
    applied: bool
    values: Incomplete
    def __init__(
        self,
        net,
        output_element,
        output_variable,
        output_element_index,
        input_element,
        input_variable,
        input_element_index,
        characteristic_index,
        tol: float = 0.001,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    def is_converged(self, net): ...
    def control_step(self, net) -> None: ...
