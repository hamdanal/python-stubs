import numpy as np

from pandapower._typing import Int
from pandapower.auxiliary import pandapowerNet
from pandapower.io_utils import JSONSerializableClass

class ProtectionDevice(JSONSerializableClass):
    index: np.int64
    def __init__(
        self, net: pandapowerNet, index: Int | None = None, in_service: bool = True, overwrite: bool = False, **kwargs
    ) -> None: ...
    def reset_device(self): ...
    def has_tripped(self) -> bool: ...
    def protection_function(self, net: pandapowerNet, scenario): ...
