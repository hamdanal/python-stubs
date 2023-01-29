from _typeshed import Incomplete

import pandapower.auxiliary

class PandapowerDiagnostic:

    net: Incomplete
    diagnostic: Incomplete
    def __init__(self, net: pandapower.auxiliary.pandapowerNet, diagnostic: dict = ...) -> None: ...
    def replace_pp_diagnostic_with_cim_ids(self) -> dict: ...
    def serialize(self, diagnostic: dict, path_to_store: str): ...
