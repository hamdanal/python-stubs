from pandapower.auxiliary import pandapowerNet
from pandapower.converter.cim.cim_classes import CimParser
from pandapower.converter.cim.interfaces import CIMRepair, PandapowerRepair

def from_cim_dict(
    cim_parser: CimParser,
    log_debug: bool = False,
    convert_line_to_switch: bool = False,
    line_r_limit: float = 0.1,
    line_x_limit: float = 0.1,
    repair_cim: str | CIMRepair | None = None,
    repair_cim_class: type[CIMRepair] | None = None,
    repair_pp: str | PandapowerRepair | None = None,
    repair_pp_class: type[PandapowerRepair] | None = None,
    **kwargs,
) -> pandapowerNet: ...
def from_cim(
    file_list: list[str] | None = None,
    encoding: str = "utf-8",
    convert_line_to_switch: bool = False,
    line_r_limit: float = 0.1,
    line_x_limit: float = 0.1,
    repair_cim: str | CIMRepair | None = None,
    repair_cim_class: type[CIMRepair] | None = None,
    repair_pp: str | PandapowerRepair | None = None,
    repair_pp_class: type[PandapowerRepair] | None = None,
    **kwargs,
) -> pandapowerNet: ...
