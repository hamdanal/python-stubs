from pandapower._typing import Float, Int
from pandapower.auxiliary import pandapowerNet

def kb_extrem_landnetz_freileitung(
    n_lines: Int = 26,
    l_lines_in_km: Float = 0.012,
    std_type: str = "NFA2X 4x70",
    trafotype: str = "0.25 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0,
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_landnetz_kabel(
    n_branch_1: Int = 26,
    l_lines_1_in_km: Float = 0.026,
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.25 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.018,
    length_branchout_line_2: Float = 0.033,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_landnetz_freileitung_trafo(
    n_branch_1: Int = 26,
    n_branch_2: Int = 1,
    l_lines_1_in_km: Float = 0.012,
    l_lines_2_in_km: Float = 0.036,
    std_type: str = "NFA2X 4x70",
    trafotype: str = "0.1 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0,
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_landnetz_kabel_trafo(
    n_branch_1: Int = 26,
    n_branch_2: Int = 1,
    l_lines_1_in_km: Float = 0.026,
    l_lines_2_in_km: Float = 0.078,
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.1 MVA 10/0.4 kV",
    p_load_mw: Float = 0.008,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.018,
    length_branchout_line_2: Float = 0.033,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_dorfnetz(
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.4 MVA 10/0.4 kV",
    p_load_mw: Float = 0.006,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.015,
    length_branchout_line_2: Float = 0.031,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_dorfnetz_trafo(
    std_type: str = "NAYY 4x150",
    trafotype: str = "0.25 MVA 10/0.4 kV",
    p_load_mw: Float = 0.006,
    q_load_mvar: Float = 0.0,
    length_branchout_line_1: Float = 0.015,
    length_branchout_line_2: Float = 0.031,
    std_type_branchout_line: str = "NAYY 4x50",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_vorstadtnetz_1(
    std_type: str = "NAYY 4x150",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.63 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_vorstadtnetz_2(
    std_type: str = "NAYY 4x185",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.63 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_vorstadtnetz_trafo_1(
    std_type: str = "NAYY 4x150",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.25 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
def kb_extrem_vorstadtnetz_trafo_2(
    std_type: str = "NAYY 4x185",
    p_load_mw: Float = 0.002,
    q_load_mvar: Float = 0.0,
    trafotype: str = "0.25 MVA 10/0.4 kV",
    v_os: Float = 10.0,
) -> pandapowerNet: ...
