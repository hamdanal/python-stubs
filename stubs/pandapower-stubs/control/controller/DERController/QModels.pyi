from _typeshed import Incomplete

import numpy as np

from pandapower._typing import Float
from pandapower.control.controller.DERController.DERBasics import BaseModel, CosphiPCurve, CosphiVCurve, QVCurve

class QModel(BaseModel):
    def __init__(self, **kwargs) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelConstQ(QModel):
    q_pu: Incomplete
    def __init__(self, q_pu) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelCosphiVCurve(QModel):
    cosphi_v_curve: CosphiVCurve
    def __init__(self, cosphi_v_curve: dict[str, Incomplete] | CosphiVCurve) -> None: ...
    def step(self, vm_pu, p_pu=None): ...  # type: ignore[override]

class QModelCosphiP(QModel):
    cosphi: Float
    q_setpoint_pu: np.float64
    def __init__(self, cosphi: Float) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelCosphiSn(QModel):
    cosphi: Float
    def __init__(self, cosphi: Float = 0.2) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelCosphiPQ(QModel):
    cosphi: Float
    q_setpoint_pu: np.float64
    def __init__(self, cosphi: Float) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelCosphiPCurve(QModel):
    cosphi_p_curve: CosphiPCurve
    def __init__(self, cosphi_p_curve) -> None: ...
    def step(self, vm_pu=None, p_pu=None): ...

class QModelQVCurve(QModel):
    qv_curve: QVCurve
    def __init__(self, qv_curve: dict[str, Incomplete] | QVCurve) -> None: ...
    def step(self, vm_pu, p_pu=None): ...  # type: ignore[override]
