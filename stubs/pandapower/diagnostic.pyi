from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet

log_message_sep: str

def diagnostic(
    net: pandapowerNet,
    report_style: str = ...,
    warnings_only: bool = ...,
    return_result_dict: bool = ...,
    overload_scaling_factor: float = ...,
    min_r_ohm: float = ...,
    min_x_ohm: float = ...,
    min_r_pu: float = ...,
    min_x_pu: float = ...,
    nom_voltage_tolerance: float = ...,
    numba_tolerance: float = ...,
) -> dict[str, Incomplete]: ...
def check_greater_zero(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_greater_equal_zero(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_less_zero(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_less_equal_zero(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_boolean(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_pos_int(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_number(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_greater_zero_less_equal_one(element: Incomplete, element_index: int, column: str) -> int | None: ...
def check_switch_type(element: Incomplete, element_index: int, column: str) -> int | None: ...
def invalid_values(net: pandapowerNet) -> dict[str, list[tuple[int, str, str, Incomplete]]]: ...
def no_ext_grid(net: pandapowerNet) -> bool | None: ...
def multiple_voltage_controlling_elements_per_bus(net: pandapowerNet) -> dict[str, list[int]] | None: ...
def overload(net: pandapowerNet, overload_scaling_factor: float) -> dict[str, bool] | None: ...
def wrong_switch_configuration(net: pandapowerNet) -> bool | None: ...
def missing_bus_indices(net: pandapowerNet) -> dict[str, list[tuple[int, str, int]]] | None: ...
def different_voltage_levels_connected(net: pandapowerNet) -> dict[str, list[int]] | None: ...
def impedance_values_close_to_zero(
    net: pandapowerNet, min_r_ohm: float, min_x_ohm: float, min_r_pu: float, min_x_pu: float
) -> list[dict[str, Incomplete]] | None: ...
def nominal_voltages_dont_match(net: pandapowerNet, nom_voltage_tolerance: float) -> dict[str, dict[str, list[int]]] | None: ...
def disconnected_elements(net: pandapowerNet) -> list[dict[str, list[int]]] | None: ...
def wrong_reference_system(net: pandapowerNet) -> dict[str, list[int]] | None: ...
def numba_comparison(net: pandapowerNet, numba_tolerance: float) -> dict[str, dict[str, float]] | None: ...
def deviation_from_std_type(net: pandapowerNet) -> dict[str, dict[int, dict[str, Incomplete]]] | None: ...
def parallel_switches(net: pandapowerNet) -> list[list[int]] | None: ...
