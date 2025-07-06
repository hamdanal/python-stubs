import numpy as np
from scipy.sparse import csr_matrix  # type: ignore[import-untyped]

from pandapower._typing import Array1D, Array2D, Float, Int

def makeAang(
    baseMVA: Float, branch, nb: Int, ppopt
) -> tuple[
    Array2D[np.float64] | csr_matrix, Array1D[np.float64], Array1D[np.float64], Array1D[np.float64] | Array1D[np.bool]
]: ...
