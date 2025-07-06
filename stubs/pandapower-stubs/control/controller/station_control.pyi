import numpy as np

from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller

class BinarySearchControl(Controller):
    def __init__(
        self,
        net: pandapowerNet,
        ctrl_in_service,
        output_element,
        output_variable,
        output_element_index,
        output_element_in_service,
        output_values_distribution,
        input_element,
        input_variable,
        input_element_index,
        set_point,
        voltage_ctrl,
        bus_idx=None,
        tol=0.001,
        in_service=True,
        order=0,
        level=0,
        drop_same_existing_ctrl=False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
    def initialize_control(self, net: pandapowerNet) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool | np.bool: ...
    def control_step(self, net: pandapowerNet) -> None: ...

class DroopControl(Controller):
    def __init__(
        self,
        net: pandapowerNet,
        q_droop_mvar,
        bus_idx,
        vm_set_pu,
        controller_idx,
        voltage_ctrl,
        tol=1e-6,
        in_service=True,
        order=-1,
        level=0,
        drop_same_existing_ctrl=False,
        matching_params=None,
        vm_set_lb=None,
        vm_set_ub=None,
        **kwargs,
    ) -> None: ...
    def is_converged(self, net: pandapowerNet) -> bool | np.bool: ...
    def control_step(self, net: pandapowerNet) -> None: ...
