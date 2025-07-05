import numpy as np
from scipy.sparse import csr_array, csr_matrix  # type: ignore[import-untyped]

from pandapower._typing import Array1D, Float, Int

def gen_Ybus(
    Yf_x, Yt_x, Ysh, col_Y, f, t, f_sort, t_sort, nb: Int, nl: Int, r_nl
) -> tuple[Array1D[np.complex128], Array1D[np.int64], Array1D[np.int64], int]: ...
def makeYbus(baseMVA: Float, bus, branch) -> tuple[csr_matrix, csr_array, csr_array]: ...
