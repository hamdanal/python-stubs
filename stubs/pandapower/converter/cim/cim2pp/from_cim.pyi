import pandapower.auxiliary

from .. import cim_classes

def from_cim_dict(
    cim_parser: cim_classes.CimParser,
    log_debug: bool = False,
    convert_line_to_switch: bool = False,
    line_r_limit: float = 0.1,
    line_x_limit: float = 0.1,
    **kwargs,
) -> pandapower.auxiliary.pandapowerNet: ...
def from_cim(
    eq_file: str = ...,
    ssh_file: str = ...,
    tp_file: str = ...,
    sv_file: str = ...,
    encoding: str = "utf-8",
    convert_line_to_switch: bool = False,
    line_r_limit: float = 0.1,
    line_x_limit: float = 0.1,
    repair_cim: str = None,
    repair_pp: str = None,
    **kwargs,
) -> pandapower.auxiliary.pandapowerNet: ...
