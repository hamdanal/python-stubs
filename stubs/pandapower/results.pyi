from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet

suffix_mode: Incomplete

def verify_results(net: pandapowerNet, mode: str = "pf") -> None: ...
def get_result_tables(element: str, suffix: str | None = None) -> tuple[str, str]: ...
def empty_res_element(net: pandapowerNet, element: str, suffix: str | None = None) -> None: ...
def init_element(net: pandapowerNet, element: str, suffix: str | None = None) -> None: ...
def get_relevant_elements(mode: str = "pf") -> list[str] | Incomplete: ...
def init_results(net: pandapowerNet, mode: str = "pf") -> None: ...
def reset_results(net: pandapowerNet, mode: str = "pf") -> None: ...
