import numpy as np
import shapely

from pandapower._typing import Array1D, Array2D, Float, FloatVectorLike
from pandapower.control.controller.DERController.DERBasics import BaseModel

class BaseArea(BaseModel):
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array2D[np.float64]: ...

class BasePQVArea(BaseArea):
    raise_merge_overlap: bool
    def __init__(self, raise_merge_overlap: bool = True) -> None: ...
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array2D[np.float64]: ...

class PQAreaPOLYGON(BaseArea):
    p_points_pu: FloatVectorLike
    q_points_pu: FloatVectorLike
    polygon: shapely.Polygon
    def __init__(self, p_points_pu: FloatVectorLike, q_points_pu: FloatVectorLike) -> None: ...
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array2D[np.float64]: ...

class QVAreaPOLYGON(BaseArea):
    q_points_pu: FloatVectorLike
    vm_points_pu: FloatVectorLike
    polygon: shapely.Polygon
    def __init__(self, q_points_pu: FloatVectorLike, vm_points_pu: FloatVectorLike) -> None: ...
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array2D[np.float64]: ...

class PQVAreaPOLYGON(BasePQVArea):
    pq_area: PQAreaPOLYGON
    qv_area: QVAreaPOLYGON
    def __init__(
        self,
        p_points_pu: FloatVectorLike,
        q_pq_points_pu: FloatVectorLike,
        q_qv_points_pu: FloatVectorLike,
        vm_points_pu: FloatVectorLike,
        raise_merge_overlap: bool = True,
    ) -> None: ...

class PQAreaSTATCOM(BaseArea):
    min_q_pu: FloatVectorLike
    max_q_pu: FloatVectorLike
    def __init__(self, min_q_pu: FloatVectorLike, max_q_pu: FloatVectorLike) -> None: ...
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array2D[np.float64]: ...

class PQArea4120(BaseArea):
    version: int
    p_points_pu: list[float]
    min_q_pu: FloatVectorLike
    max_q_pu: FloatVectorLike
    q_max_under_p_point: float
    linear_factor_ind: FloatVectorLike
    linear_factor_cap: FloatVectorLike
    def __init__(self, min_q_pu: FloatVectorLike, max_q_pu: FloatVectorLike, version: int = 2018, **kwargs) -> None: ...
    def in_area(self, p_pu: FloatVectorLike, q_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array1D[np.bool]: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike | None = None) -> Array2D[np.float64]: ...

class QVArea4120(BaseArea):
    min_q_pu: FloatVectorLike
    max_q_pu: FloatVectorLike
    max_vm_pu: float
    min_vm_pu: float
    delta_vm_pu: float
    linear_factor: FloatVectorLike
    def __init__(self, min_q_pu: FloatVectorLike, max_q_pu: FloatVectorLike) -> None: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array2D[np.float64]: ...

class PQVArea4120Base(BasePQVArea):
    pq_area: PQArea4120
    qv_area: QVArea4120
    def __init__(
        self, min_q_pu: FloatVectorLike, max_q_pu: FloatVectorLike, version: int = 2018, raise_merge_overlap: bool = True
    ) -> None: ...

class PQVArea4120V1(PQVArea4120Base):
    def __init__(self, version: int = 2018, raise_merge_overlap: bool = True) -> None: ...

class PQVArea4120V2(PQVArea4120Base):
    def __init__(self, version: int = 2018, raise_merge_overlap: bool = True) -> None: ...

class PQVArea4120V3(PQVArea4120Base):
    def __init__(self, version: int = 2018, raise_merge_overlap: bool = True) -> None: ...

class PQArea4130(PQArea4120):
    def __init__(self, min_q_pu, max_q_pu) -> None: ...

class QVArea4130(QVArea4120):
    min_q_pu: FloatVectorLike
    max_q_pu: FloatVectorLike
    vn_kv: Float
    variant: int
    min_vm_points_pu: Array1D[np.float64]
    max_vm_points_pu: Array1D[np.float64]
    min_q_points_pu: Array1D[np.float64]
    max_q_points_pu: Array1D[np.float64]
    def __init__(self, min_q_pu: FloatVectorLike, max_q_pu: FloatVectorLike, vn_kv: Float, variant: int) -> None: ...
    def q_flexibility(self, p_pu: FloatVectorLike, vm_pu: FloatVectorLike) -> Array2D[np.float64]: ...

class PQVArea4130Base(BasePQVArea):
    pq_area: PQArea4130
    qv_area: QVArea4130
    def __init__(
        self,
        min_q_pu: FloatVectorLike,
        max_q_pu: FloatVectorLike,
        variant: int,
        vn_kv: Float = 380,
        raise_merge_overlap: bool = True,
    ) -> None: ...

class PQVArea4130V1(PQVArea4130Base):
    def __init__(self, vn_kv: Float = 380, raise_merge_overlap: bool = True) -> None: ...

class PQVArea4130V2(PQVArea4130Base):
    def __init__(self, vn_kv: Float = 380, raise_merge_overlap: bool = True) -> None: ...

class PQVArea4130V3(PQVArea4130Base):
    def __init__(self, vn_kv: Float = 380, raise_merge_overlap: bool = True) -> None: ...

class PQArea4110(PQAreaPOLYGON):
    def __init__(self) -> None: ...

class QVArea4110(QVAreaPOLYGON):
    def __init__(self) -> None: ...

class PQVArea4110(BasePQVArea):
    pq_area: PQArea4110
    qv_area: QVArea4110
    def __init__(self, raise_merge_overlap: bool = True) -> None: ...

class PQArea4105(PQAreaPOLYGON):
    def __init__(self, variant: int) -> None: ...

class QVArea4105(QVAreaPOLYGON):
    def __init__(self, variant: int) -> None: ...

class PQVArea4105(BasePQVArea):
    pq_area: PQArea4105
    qv_area: QVArea4105
    def __init__(self, variant: int, raise_merge_overlap: bool = True) -> None: ...
