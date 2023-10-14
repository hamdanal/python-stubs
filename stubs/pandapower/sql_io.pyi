from _typeshed import StrOrBytesPath
from _typeshed.dbapi import DBAPIConnection, DBAPICursor
from collections.abc import Mapping

import pandas as pd
from pandapower.auxiliary import pandapowerNet

PSYCOPG2_INSTALLED: bool
SQLITE_INSTALLED: bool

def match_sql_type(dtype: str) -> str: ...
def check_if_sql_table_exists(cursor: DBAPICursor, table_name: str) -> bool: ...
def get_sql_table_columns(cursor: DBAPICursor, table_name: str) -> list[str]: ...
def download_sql_table(cursor: DBAPICursor, table_name: str, **id_columns: int) -> pd.DataFrame: ...
def upload_sql_table(
    conn: DBAPIConnection,
    cursor: DBAPICursor,
    table_name: str,
    table: pd.DataFrame,
    index_name: str | None = None,
    timestamp: bool = False,
    **id_columns: int,
) -> None: ...
def check_postgresql_catalogue_table(
    cursor: DBAPICursor, table_name: str, grid_id: int | None, grid_id_column: str, download: bool = False
) -> None: ...
def create_postgresql_catalogue_entry(
    conn: DBAPIConnection, cursor: DBAPICursor, grid_id: int | None, grid_id_column: str, catalogue_table_name: str
) -> int: ...
def add_timestamp_column(conn: DBAPIConnection, cursor: DBAPICursor, table_name: str) -> None: ...
def create_sql_table_if_not_exists(
    conn: DBAPIConnection, cursor: DBAPICursor, table_name: str, grid_id_column: str, catalogue_table_name: str
) -> None: ...
def delete_postgresql_net(
    grid_id: int,
    host: str,
    user: str,
    password: str,
    database: str,
    schema: str,
    grid_id_column: str = "grid_id",
    grid_catalogue_name: str = "grid_catalogue",
) -> None: ...
def from_sql(
    conn: DBAPIConnection,
    schema: str,
    grid_id: int,
    grid_id_column: str = "grid_id",
    grid_catalogue_name: str = "grid_catalogue",
    empty_dict_like_object: Mapping[str, pd.DataFrame] | None = None,
) -> pandapowerNet: ...
def to_sql(
    net: pandapowerNet,
    conn: DBAPIConnection,
    schema: str,
    include_results: bool = False,
    grid_id: int | None = None,
    grid_id_column: str = "grid_id",
    grid_catalogue_name: str = "grid_catalogue",
    index_name: str | None = None,
) -> int: ...
def to_sqlite(net: pandapowerNet, filename: StrOrBytesPath, include_results: bool = False) -> None: ...
def from_sqlite(filename: StrOrBytesPath) -> pandapowerNet: ...
def to_postgresql(
    net: pandapowerNet,
    host: str,
    user: str,
    password: str,
    database: str,
    schema: str,
    include_results: bool = False,
    grid_id: int | None = None,
    grid_id_column: str = "grid_id",
    grid_catalogue_name: str = "grid_catalogue",
    index_name: str | None = None,
) -> int: ...
def from_postgresql(
    grid_id: int,
    host: str,
    user: str,
    password: str,
    database: str,
    schema: str,
    grid_id_column: str = "grid_id",
    grid_catalogue_name: str = "grid_catalogue",
    empty_dict_like_object: Mapping[str, pd.DataFrame] | None = None,
) -> pandapowerNet: ...
