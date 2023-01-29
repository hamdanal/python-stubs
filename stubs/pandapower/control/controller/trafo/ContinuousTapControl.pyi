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
        tol: float = ...,
        side: str = ...,
        trafotype: str = ...,
        in_service: bool = ...,
        check_tap_bounds: bool = ...,
        level: int = ...,
        order: int = ...,
        drop_same_existing_ctrl: bool = ...,
        matching_params: Incomplete | None = ...,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    tap_pos: Incomplete
    def control_step(self, net) -> None: ...
    def is_converged(self, net): ...
