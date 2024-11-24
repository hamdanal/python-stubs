from _typeshed import Incomplete

from pandapower.control.basic_controller import Controller

class TrafoController(Controller):
    trafotype: Incomplete
    tid: Incomplete
    tol: Incomplete
    def __init__(
        self, net, tid, side, tol, in_service, trafotype, level: int = 0, order: int = 0, recycle: bool = True, **kwargs
    ) -> None: ...
    def initialize_control(self, net) -> None: ...
    def nothing_to_do(self, net): ...
    def set_recycle(self, net) -> None: ...
