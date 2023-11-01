from _typeshed import Incomplete

from pandapower.auxiliary import pandapowerNet

class PandapowerDiagnostic:
    net: pandapowerNet
    diagnostic: dict[Incomplete, Incomplete]
    def __init__(self, net: pandapowerNet, diagnostic: dict[Incomplete, Incomplete] | None = None) -> None: ...
    def replace_pp_diagnostic_with_cim_ids(self) -> dict[Incomplete, Incomplete]: ...
    def serialize(self, diagnostic: dict[Incomplete, Incomplete], path_to_store: str): ...
