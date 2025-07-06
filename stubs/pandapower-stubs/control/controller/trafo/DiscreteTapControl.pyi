from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.trafo_control import TrafoController

class DiscreteTapControl(TrafoController):
    vm_lower_pu: Incomplete
    vm_upper_pu: Incomplete
    vm_delta_pu: Incomplete
    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        vm_lower_pu,
        vm_upper_pu,
        side: str = "lv",
        element: str = "trafo",
        tol: float = 1e-3,
        in_service: bool = True,
        hunting_limit=None,
        level: int = 0,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    @classmethod
    def from_tap_step_percent(
        cls,
        net: pandapowerNet,
        element_index,
        vm_set_pu,
        side: str = "lv",
        element: str = "trafo",
        tol: float = 1e-3,
        in_service: bool = True,
        hunting_limit=None,
        level: int = 0,
        order: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params=None,
        **kwargs,
    ): ...
    @property
    def vm_set_pu(self): ...
    @vm_set_pu.setter
    def vm_set_pu(self, value) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    tap_pos: Incomplete
    def control_step(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet): ...
