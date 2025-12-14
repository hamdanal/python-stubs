from pandapower.auxiliary import pandapowerNet
from pandapower.control.basic_controller import Controller

class DmrControl(Controller):
    def __init__(
        self,
        net: pandapowerNet,
        dmr_line: int,
        dc_plus_line: int,
        dc_minus_line: int,
        in_service=True,
        order=0,
        level=0,
        drop_same_existing_ctrl=False,
        matching_params=None,
        **kwargs,
    ): ...
    def is_converged(self, net: pandapowerNet) -> bool: ...
    def finalize_control(self, net: pandapowerNet) -> None: ...
