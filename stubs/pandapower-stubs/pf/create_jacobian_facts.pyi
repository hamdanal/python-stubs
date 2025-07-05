from typing import Final

from scipy.sparse import csr_array, csr_matrix  # type: ignore[import-untyped]

SMALL_NUMBER: Final = 1e-9

def create_J_modification_svc(
    J, svc_buses, pvpq, pq, pq_lookup, Vm, x_control, svc_x_l_pu, svc_x_cvar_pu, nsvc_controllable, svc_controllable
) -> csr_matrix: ...
def create_J_modification_tcsc(
    J, V, y_tcsc_pu, x_control, tcsc_controllable, tcsc_x_l_pu, f, t, pvpq, pq, pvpq_lookup, pq_lookup, nsvc
) -> csr_matrix: ...
def create_J_modification_ssc_vsc(
    J, V, Vm, y_pu, f, t, pvpq, pq, pvpq_lookup, pq_lookup, control_v, control_delta
) -> csr_matrix: ...
def create_J_modification_hvdc(
    J, V_dc, Ybus_hvdc, Ybus_vsc_dc, vsc_g_pu, vsc_gl_pu, dc_p, dc_p_lookup, vsc_dc_fb, vsc_dc_tb, vsc_dc_slack, vsc_dc_mode_p
) -> csr_array: ...
