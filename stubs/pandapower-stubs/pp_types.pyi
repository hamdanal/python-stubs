from typing import Literal
from typing_extensions import TypeAlias

import numpy as np

Int: TypeAlias = int | np.integer
Float: TypeAlias = float | np.number

BusType: TypeAlias = Literal["n", "b", "m"]
CostElementType: TypeAlias = Literal["gen", "sgen", "ext_grid", "load", "dcline", "storage"]
GeneratorType: TypeAlias = Literal["current_source", "async", "async_doubly_fed"]
LineType: TypeAlias = Literal["ol", "cs"]
HVLVType: TypeAlias = Literal["hv", "lv"]
HVMVLVType: TypeAlias = Literal["hv", "mv", "lv"]
MeasurementType: TypeAlias = Literal["v", "p", "q", "i", "va", "ia"]
MeasurementElementType: TypeAlias = Literal[
    "bus", "line", "trafo", "trafow3", "load", "gen", "sgen", "shunt", "ward", "xward", "ext_grid"
]
PWLPowerType: TypeAlias = Literal["p", "q"]
SwitchElementType: TypeAlias = Literal["b", "l", "t"]
SwitchType: TypeAlias = Literal["LS", "CB", "LBS", "DS"]
TapChangerType: TypeAlias = Literal["Ratio", "Symmetrical", "Ideal"]
TapChangerWithTabularType: TypeAlias = Literal["Ratio", "Symmetrical", "Ideal", "Tabular"]
UnderOverExcitedType: TypeAlias = Literal["underexcited", "overexcited"]
WyeDeltaType: TypeAlias = Literal["wye", "delta"]
