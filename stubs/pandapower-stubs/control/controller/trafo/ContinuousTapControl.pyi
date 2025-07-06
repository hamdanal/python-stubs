from _typeshed import Incomplete

import numpy as np

from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.trafo_control import TrafoController

class ContinuousTapControl(TrafoController):
    check_tap_bounds: Incomplete
    vm_set_pu: Incomplete
    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        vm_set_pu,
        tol: float = 1e-3,
        side: str = "lv",
        element: str = "trafo",
        in_service: bool = True,
        check_tap_bounds: bool = True,
        level: int = 0,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    tap_pos: Incomplete
    def control_step(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool | np.bool: ...
