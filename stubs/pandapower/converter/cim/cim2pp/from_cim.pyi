import pandapower.auxiliary

from .. import cim_classes

def from_cim_dict(
    cim_parser: cim_classes.CimParser,
    log_debug: bool = ...,
    convert_line_to_switch: bool = ...,
    line_r_limit: float = ...,
    line_x_limit: float = ...,
    **kwargs,
) -> pandapower.auxiliary.pandapowerNet: ...
def from_cim(
    eq_file: str = ...,
    ssh_file: str = ...,
    tp_file: str = ...,
    sv_file: str = ...,
    encoding: str = ...,
    convert_line_to_switch: bool = ...,
    line_r_limit: float = ...,
    line_x_limit: float = ...,
    repair_cim: str = ...,
    repair_pp: str = ...,
    **kwargs,
) -> pandapower.auxiliary.pandapowerNet: ...
