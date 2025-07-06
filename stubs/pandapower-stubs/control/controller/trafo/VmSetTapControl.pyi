from pandapower.auxiliary import pandapowerNet
from pandapower.control.controller.characteristic_control import CharacteristicControl

class VmSetTapControl(CharacteristicControl):
    def __init__(
        self,
        net: pandapowerNet,
        controller_index,
        characteristic_index,
        variable: str = "p_hv_mw",
        tol: float = 0.001,
        in_service: bool = True,
        order: int = 0,
        level: int = 0,
        drop_same_existing_ctrl: bool = False,
        matching_params=None,
        **kwargs,
    ) -> None: ...
