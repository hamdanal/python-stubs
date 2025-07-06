from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller

class ShuntController(Controller):
    def __init__(
        self,
        net: pandapowerNet,
        shunt_index,
        bus_index=None,
        tol=1e-3,
        in_service=True,
        check_step_bounds=True,
        order=0,
        level=0,
        **kwargs,
    ) -> None: ...

class DiscreteShuntController(ShuntController):
    def __init__(
        self,
        net: pandapowerNet,
        shunt_index,
        vm_set_pu,
        bus_index=None,
        tol=1e-3,
        increment=1,
        reset_at_init=False,
        in_service=True,
        check_step_bounds=True,
        order=0,
        level=0,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def control_step(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool: ...
