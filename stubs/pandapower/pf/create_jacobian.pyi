def create_jacobian_matrix(
    Ybus, V, ref, refpvpq, pvpq, pq, createJ, pvpq_lookup, nref, npv, npq, numba, slack_weights, dist_slack
): ...
def get_fastest_jacobian_function(pvpq, pq, numba, dist_slack): ...
