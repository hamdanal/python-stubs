from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller

class TrafoController(Controller):
    element: Incomplete
    element_index: Incomplete
    tol: Incomplete
    trafobus: Incomplete | None
    def __init__(
        self,
        net: pandapowerNet,
        element_index,
        side,
        tol,
        in_service: bool,
        element,
        level: int = 0,
        order: int = 0,
        recycle: bool = True,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def nothing_to_do(self, net: pandapowerNet) -> bool: ...
    def set_recycle(self, net: pandapowerNet) -> None: ...
