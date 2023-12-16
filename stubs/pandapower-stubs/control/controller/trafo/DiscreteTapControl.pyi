from _typeshed import Incomplete

from pandapower.control.controller.trafo_control import TrafoController

class DiscreteTapControl(TrafoController):
    vm_lower_pu: Incomplete
    vm_upper_pu: Incomplete
    vm_delta_pu: Incomplete
    def __init__(
        self,
        net,
        tid,
        vm_lower_pu,
        vm_upper_pu,
        side: str = "lv",
        trafotype: str = "2W",
        tol: float = 0.001,
        in_service: bool = True,
        level: int = 0,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    @classmethod
    def from_tap_step_percent(
        cls,
        net,
        tid,
        vm_set_pu,
        side: str = "lv",
        trafotype: str = "2W",
        tol: float = 0.001,
        in_service: bool = True,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ): ...
    @property
    def vm_set_pu(self): ...
    @vm_set_pu.setter
    def vm_set_pu(self, value) -> None: ...
    def initialize_control(self, net) -> None: ...
    tap_pos: Incomplete
    def control_step(self, net) -> None: ...
    def is_converged(self, net): ...
