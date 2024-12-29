from typing import Any, SupportsIndex as Int

from pandapower.auxiliary import pandapowerNet
from pandapower.io_utils import JSONSerializableClass

class BasicCtrl(JSONSerializableClass):
    index: int
    def __init__(self, container: pandapowerNet, index: Int | None = None, **kwargs) -> None: ...
    def time_step(self, container: pandapowerNet, time: Any) -> None: ...
    def initialize_control(self, container: pandapowerNet) -> None: ...
    def is_converged(self, container: pandapowerNet): ...
    def control_step(self, container: pandapowerNet) -> None: ...
    def repair_control(self, container: pandapowerNet) -> None: ...
    def restore_init_state(self, container: pandapowerNet) -> None: ...
    def finalize_control(self, container: pandapowerNet) -> None: ...
    def finalize_step(self, container: pandapowerNet, time: Any) -> None: ...
    def set_active(self, container: pandapowerNet, in_service: bool) -> None: ...
    def level_reset(self, prosumer) -> None: ...

class Controller(BasicCtrl):
    matching_params: dict[str, Any]
    index: int
    def __init__(
        self,
        net: pandapowerNet,
        in_service: bool = True,
        order: Int = 0,
        level: Int = 0,
        index: Int | None = None,
        recycle: bool = False,
        drop_same_existing_ctrl: bool = False,
        initial_run: bool = True,
        overwrite: bool = False,
        matching_params: dict[str, Any] | None = None,
        **kwargs,
    ) -> None: ...
    def add_controller_to_net(
        self,
        net: pandapowerNet,
        in_service: bool,
        initial_run: bool,
        order: Int,
        level: Int,
        index: Int,
        recycle: bool,
        drop_same_existing_ctrl: bool,
        overwrite: bool,
        **kwargs,
    ) -> int: ...
    def time_step(self, net: pandapowerNet, time: Any) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet): ...
    def control_step(self, net: pandapowerNet) -> None: ...
    def repair_control(self, net: pandapowerNet) -> None: ...
    def restore_init_state(self, net: pandapowerNet) -> None: ...
    def finalize_control(self, net: pandapowerNet) -> None: ...
    def finalize_step(self, net: pandapowerNet, time: Any) -> None: ...
    def set_active(self, net: pandapowerNet, in_service: bool) -> None: ...
    def set_recycle(self, net: pandapowerNet) -> None: ...
