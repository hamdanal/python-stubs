from collections.abc import Collection, Iterable
from typing import Literal, overload

import numpy as np
from numpy.typing import NDArray

type _PMode = Literal["load", "gen"]
type _QMode = Literal["underexcited", "overexcited"]

def signing_system_value(element_type: str) -> Literal[-1, 1]: ...
@overload
def pq_from_cosphi(s: float, cosphi: float, qmode: _QMode, pmode: _PMode) -> tuple[float, np.float64]: ...  # type: ignore[overload-overlap]
@overload
def pq_from_cosphi(
    s: Iterable[float], cosphi: float | Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: float | Iterable[float], qmode: Iterable[_QMode], pmode: _PMode | Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float], cosphi: float | Iterable[float], qmode: _QMode | Iterable[_QMode], pmode: Iterable[_PMode]
) -> tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def pq_from_cosphi(
    s: float | Iterable[float],
    cosphi: float | Iterable[float],
    qmode: _QMode | Iterable[_QMode],
    pmode: _PMode | Iterable[_PMode],
) -> tuple[float, np.float64] | tuple[NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def cosphi_from_pq(p: float, q: float) -> tuple[float, float, _PMode, _QMode]: ...
@overload
def cosphi_from_pq(
    p: Iterable[float], q: float | Iterable[float]
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]: ...
@overload
def cosphi_from_pq(
    p: float | Iterable[float], q: Iterable[float]
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]: ...
@overload
def cosphi_from_pq(
    p: float | Iterable[float], q: float | Iterable[float]
) -> (
    tuple[float, float, _PMode, _QMode] | tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.str_], NDArray[np.str_]]
): ...
@overload
def cosphi_pos_neg_from_pq(p: float, q: float) -> np.float64: ...
@overload
def cosphi_pos_neg_from_pq(p: Iterable[float], q: float | Iterable[float]) -> NDArray[np.float64]: ...
@overload
def cosphi_pos_neg_from_pq(p: float | Iterable[float], q: Iterable[float]) -> NDArray[np.float64]: ...
@overload
def cosphi_pos_neg_from_pq(p: float | Iterable[float], q: float | Iterable[float]) -> np.float64 | NDArray[np.float64]: ...
@overload
def cosphi_to_pos(cosphi: float) -> np.float64: ...
@overload
def cosphi_to_pos(cosphi: Collection[float]) -> NDArray[np.float64]: ...
@overload
def cosphi_from_pos(cosphi: float) -> np.float64: ...
@overload
def cosphi_from_pos(cosphi: Collection[float]) -> NDArray[np.float64]: ...
