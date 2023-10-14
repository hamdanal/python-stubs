from _typeshed import Incomplete

from pandapower.control.basic_controller import Controller

class ConstControl(Controller):
    data_source: Incomplete
    element_index: Incomplete
    element: Incomplete
    values: Incomplete
    profile_name: Incomplete
    scale_factor: Incomplete
    applied: bool
    def __init__(
        self,
        net,
        element,
        variable,
        element_index,
        profile_name: Incomplete | None = None,
        data_source: Incomplete | None = None,
        scale_factor: float = 1.0,
        in_service: bool = True,
        recycle: bool = True,
        order: int = -1,
        level: int = -1,
        drop_same_existing_ctrl: bool = False,
        matching_params: Incomplete | None = None,
        initial_run: bool = False,
        **kwargs,
    ) -> None: ...
    def set_recycle(self, net) -> None: ...
    def time_step(self, net, time) -> None: ...
    def is_converged(self, net): ...
    def control_step(self, net) -> None: ...
