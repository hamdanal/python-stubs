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
        profile_name: Incomplete | None = ...,
        data_source: Incomplete | None = ...,
        scale_factor: float = ...,
        in_service: bool = ...,
        recycle: bool = ...,
        order: int = ...,
        level: int = ...,
        drop_same_existing_ctrl: bool = ...,
        matching_params: Incomplete | None = ...,
        initial_run: bool = ...,
        **kwargs,
    ) -> None: ...
    def set_recycle(self, net) -> None: ...
    def time_step(self, net, time) -> None: ...
    def is_converged(self, net): ...
    def control_step(self, net) -> None: ...
