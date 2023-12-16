from _typeshed import Incomplete

from pandapower.control.controller.trafo_control import TrafoController

class ContinuousTapControl(TrafoController):
    check_tap_bounds: Incomplete
    vm_set_pu: Incomplete
    def __init__(
        self,
        net,
        tid,
        vm_set_pu,
        tol: float = 0.001,
        side: str = "lv",
        trafotype: str = "2W",
        in_service: bool = True,
        check_tap_bounds: bool = True,
        level: int = 0,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    tap_pos: Incomplete
    def control_step(self, net) -> None: ...
    def is_converged(self, net): ...
