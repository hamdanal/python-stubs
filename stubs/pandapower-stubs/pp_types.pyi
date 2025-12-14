from typing import Literal

import numpy as np

type Int = int | np.integer
type Float = float | np.number

type BusType = Literal["n", "b", "m"]
type CostElementType = Literal["gen", "sgen", "ext_grid", "load", "dcline", "storage"]
type GeneratorType = Literal["current_source", "async", "async_doubly_fed"]
type LineType = Literal["ol", "cs"]
type HVLVType = Literal["hv", "lv"]
type HVMVLVType = Literal["hv", "mv", "lv"]
type MeasurementType = Literal["v", "p", "q", "i", "va", "ia"]
type MeasurementElementType = Literal[
    "bus", "line", "trafo", "trafow3", "load", "gen", "sgen", "shunt", "ward", "xward", "ext_grid"
]
type PWLPowerType = Literal["p", "q"]
type SwitchElementType = Literal["b", "l", "t"]
type SwitchType = Literal["LS", "CB", "LBS", "DS"]
type TapChangerType = Literal["Ratio", "Symmetrical", "Ideal"]
type TapChangerWithTabularType = Literal["Ratio", "Symmetrical", "Ideal", "Tabular"]
type UnderOverExcitedType = Literal["underexcited", "overexcited"]
type WyeDeltaType = Literal["wye", "delta"]
