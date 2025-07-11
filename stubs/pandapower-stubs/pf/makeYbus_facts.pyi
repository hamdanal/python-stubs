from scipy.sparse import csr_matrix  # type: ignore[import-untyped]

from pandapower._typing import Float, Int

def calc_y_svc(x_control_degree, svc_x_l_ohm, svc_x_cvar_ohm, v_base_kv, baseMVA: Float): ...
def calc_y_svc_pu(x_control, svc_x_l_pu, svc_x_cvar_pu): ...
def makeYbus_svc(Ybus, x_control_svc, svc_x_l_pu, svc_x_cvar_pu, svc_buses) -> csr_matrix: ...
def makeYbus_tcsc(Ybus, x_control_tcsc, tcsc_x_l_pu, tcsc_x_cvar_pu, tcsc_fb, tcsc_tb) -> csr_matrix: ...
def makeYft_tcsc(Ybus_tcsc, tcsc_fb, tcsc_tb, x_control_tcsc, tcsc_x_l_pu, tcsc_x_cvar_pu) -> tuple[csr_matrix, csr_matrix]: ...
def makeYbus_ssc_vsc(Ybus, internal_y_pu, fb, tb, controllable) -> tuple[csr_matrix, csr_matrix, csr_matrix]: ...
def make_Ybus_facts(from_bus, to_bus, y_pu, n: Int, ysf_pu=0, yst_pu=0, dtype=...) -> csr_matrix: ...
def make_Yft_facts(from_bus, to_bus, y_pu, n: Int, ysf_pu=0, yst_pu=0) -> tuple[csr_matrix, csr_matrix]: ...
