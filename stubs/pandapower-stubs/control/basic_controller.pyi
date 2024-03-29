from _typeshed import Incomplete

from pandapower.io_utils import JSONSerializableClass

class BasicCtrl(JSONSerializableClass):
    index: Incomplete
    def __init__(self, container, index: Incomplete | None = None, **kwargs) -> None: ...
    def time_step(self, container, time) -> None: ...
    def initialize_control(self, container) -> None: ...
    def is_converged(self, container): ...
    def control_step(self, container) -> None: ...
    def repair_control(self, container) -> None: ...
    def restore_init_state(self, container) -> None: ...
    def finalize_control(self, container) -> None: ...
    def finalize_step(self, container, time) -> None: ...
    def set_active(self, container, in_service) -> None: ...
    def level_reset(self, prosumer) -> None: ...

class Controller(BasicCtrl):
    matching_params: Incomplete
    index: Incomplete
    def __init__(
        self,
        net,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        index: Incomplete | None = None,
        recycle: bool = False,
        drop_same_existing_ctrl: bool = False,
        initial_run: bool = True,
        overwrite: bool = False,
        matching_params: Incomplete | None = None,
        **kwargs,
    ) -> None: ...
    def add_controller_to_net(
        self, net, in_service, initial_run, order, level, index, recycle, drop_same_existing_ctrl, overwrite, **kwargs
    ): ...
    def time_step(self, net, time) -> None: ...
    def initialize_control(self, net) -> None: ...
    def is_converged(self, net): ...
    def control_step(self, net) -> None: ...
    def repair_control(self, net) -> None: ...
    def restore_init_state(self, net) -> None: ...
    def finalize_control(self, net) -> None: ...
    def finalize_step(self, net, time) -> None: ...
    def set_active(self, net, in_service) -> None: ...
    def set_recycle(self, net) -> None: ...
