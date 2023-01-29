from _typeshed import Incomplete

import pandapower.auxiliary

from .. import cim_classes as cim_classes

sc: Incomplete

class CimConverter:

    cim_parser: Incomplete
    kwargs: Incomplete
    cim: Incomplete
    net: Incomplete
    bus_merge: Incomplete
    power_trafo2w: Incomplete
    power_trafo3w: Incomplete
    def __init__(self, cim_parser: cim_classes.CimParser, **kwargs) -> None: ...
    def convert_to_pp(
        self,
        convert_line_to_switch: bool = ...,
        line_r_limit: float = ...,
        line_x_limit: float = ...,
        log_debug: bool = ...,
        **kwargs,
    ) -> pandapower.auxiliary.pandapowerNet: ...
