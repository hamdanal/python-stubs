from _typeshed import Incomplete

import pandas as pd

class CimParser:
    cim: Incomplete
    def __init__(self, cim: dict[str, dict[str, pd.DataFrame]] = None) -> None: ...
    def parse_files(
        self,
        eq_file: str = ...,
        ssh_file: str = ...,
        tp_file: str = ...,
        sv_file: str = ...,
        eq_bd_file: str = ...,
        tp_bd_file: str = ...,
        file_list: None = None,
        encoding: str = "utf-8",
        prepare_cim_net: bool = False,
        set_data_types: bool = False,
    ) -> CimParser: ...
    def set_cim_data_types(self) -> CimParser: ...
    def prepare_cim_net(self) -> CimParser: ...
    def get_cim_data_structure(self) -> dict[str, dict[str, pd.DataFrame]]: ...
    def get_cim_dict(self) -> dict[str, dict[str, pd.DataFrame]]: ...
    def set_cim_dict(self, cim: dict[str, dict[str, pd.DataFrame]]): ...
