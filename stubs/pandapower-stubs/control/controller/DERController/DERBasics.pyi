import numpy as np

from pandapower._typing import Array1D, FloatVectorLike

class BaseModel:
    @classmethod
    def name(cls) -> str: ...

class QVCurve:
    vm_points_pu: FloatVectorLike
    q_points_pu: FloatVectorLike
    def __init__(self, vm_points_pu: FloatVectorLike, q_points_pu: FloatVectorLike) -> None: ...
    def step(self, vm_pu) -> Array1D[np.float64]: ...

class CosphiVCurve:
    vm_points_pu: FloatVectorLike
    cosphi_points: FloatVectorLike
    cosphi_pos: Array1D[np.float64]
    def __init__(self, vm_points_pu: FloatVectorLike, cosphi_points: FloatVectorLike) -> None: ...
    def step(self, vm_pu, p_pu) -> Array1D[np.float64]: ...

class CosphiPCurve:
    p_points_pu: FloatVectorLike
    cosphi_points: FloatVectorLike
    cosphi_pos: Array1D[np.float64]
    def __init__(self, p_points_pu: FloatVectorLike, cosphi_points: FloatVectorLike) -> None: ...
    def step(self, p_pu) -> Array1D[np.float64]: ...
