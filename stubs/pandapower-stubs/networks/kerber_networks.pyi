from pandapower._typing import Float, Int
from pandapower.auxiliary import pandapowerNet

def create_kerber_landnetz_freileitung_1(
    n_lines: Int = 13,
    l_lines_in_km: Float = 0.021,
    std_type: str = "NFA2X 4x70",
    trafotype: str = "0.16 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0,
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_landnetz_freileitung_2(
    n_branch_1: Int = 6,
    n_branch_2: Int = 2,
    l_lines_1_in_km: Float = 0.038,
    l_lines_2_in_km: Float = 0.081,
    std_type: str = "NFA2X 4x70",
    trafotype: str = "0.1 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0,
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_landnetz_kabel_1(
    n_branch_1: Int = 6,
    n_branch_2: Int = 2,
    l_lines_1_in_km: Float = 0.082,
    l_lines_2_in_km: Float = 0.175,
    std_type: str = "NAYY 4x150",
    std_type_branchout_line: str = "NAYY 4x50",
    trafotype: str = "0.1 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.018,
    length_branchout_line_2: Float = 0.033,
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_landnetz_kabel_2(
    n_branch_1: Int = 12,
    n_branch_2: Int = 2,
    l_lines_1_in_km: Float = 0.053,
    l_lines_2_in_km: Float = 0.175,
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.16 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.018,
    length_branchout_line_2: Float = 0.033,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_dorfnetz(
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.4 MVA 10/0.4 kV",
    p_load_mw: Float = 0.006,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.015,
    length_branchout_line_2: Float = 0.031,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_vorstadtnetz_kabel_1(
    std_type: str = "NAYY 4x150",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.63 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def create_kerber_vorstadtnetz_kabel_2(
    std_type: str = "NAYY 4x185",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.63 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
