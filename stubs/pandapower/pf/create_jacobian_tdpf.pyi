from pandapower.pypower.idx_brch import BR_B as BR_B, BR_R as BR_R, BR_X as BR_X, PF as PF, PT as PT, QF as QF, QT as QT
from pandapower.pypower.idx_brch_tdpf import TDPF as TDPF
from pandapower.pypower.idx_bus import BUS_I as BUS_I

SIGMA: float
ALPHA: float

def calc_r_theta_from_t_rise(net, t_rise_degree_celsius): ...
def calc_i_square_p_loss(branch, tdpf_lines, g, b, Vm, Va): ...
def calc_r_theta(t_air_pu, a0, a1, a2, i_square_pu, p_loss_pu): ...
def calc_T_frank(p_loss_pu, t_air_pu, r_theta_pu, tdpf_delay_s, T0, tau): ...
def calc_T_ngoko(i_square_pu, a0, a1, a2, tdpf_delay_s, T0, tau): ...
def calc_a0_a1_a2_tau(
    t_air_pu,
    t_max_pu,
    t_ref_pu,
    r_ref_ohm_per_m,
    conductor_outer_diameter_m,
    mc_joule_per_m_k,
    wind_speed_m_per_s,
    wind_angle_degree,
    s_w_per_square_meter,
    alpha_pu=...,
    solar_absorptivity: float = ...,
    emissivity: float = ...,
    T_base: int = ...,
    i_base_a: int = ...,
): ...
def calc_h_c(conductor_outer_diameter_m, v_m_per_s, wind_angle_degree, t_air_degree_celsius): ...
def create_J_tdpf(
    branch, tdpf_lines, alpha_pu, r_ref_pu, pvpq, pq, pvpq_lookup, pq_lookup, tau, tdpf_delay_s, Vm, Va, r_theta_pu, J, r, x, g
): ...
def calc_I(Sf, bus, f_bus, V): ...
def calc_g_b(r, x): ...
def get_S_flows(branch, Yf, Yt, baseMVA, V): ...
def create_J13(branch, tdpf_lines, in_pvpq_f, in_pvpq_t, pvpq, pvpq_lookup, Vm, Va, dg_dT, db_dT): ...
def create_J23(branch, tdpf_lines, in_pq_f, in_pq_t, pq, pq_lookup, Vm, Va, dg_dT, db_dT): ...
def create_J31(branch, tdpf_lines, in_pvpq_f, in_pvpq_t, pvpq, pvpq_lookup, Vm, Va, C, r_theta_pu, g): ...
def create_J32(branch, tdpf_lines, in_pq_f, in_pq_t, pq, pq_lookup, Vm, Va, C, r_theta_pu, g): ...
def create_J33(branch, tdpf_lines, r_theta_pu, Vm, Va, dg_dT): ...