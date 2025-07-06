from _typeshed import Incomplete

import numpy as np

from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller

class CharacteristicControl(Controller):
    input_element: str
    input_element_index: Incomplete
    output_element: str
    output_element_index: Incomplete
    characteristic_index: Incomplete
    tol: float
    applied: bool
    values: Incomplete
    def __init__(
        self,
        net: pandapowerNet,
        output_element: str,
        output_variable: str,
        output_element_index,
        input_element: str,
        input_variable: str,
        input_element_index,
        characteristic_index,
        tol: float = 0.001,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool | np.bool: ...
    def control_step(self, net: pandapowerNet) -> None: ...
