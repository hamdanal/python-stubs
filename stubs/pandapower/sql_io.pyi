from _typeshed import Incomplete

PSYCOPG2_INSTALLED: bool
SQLITE_INSTALLED: bool

def match_sql_type(dtype): ...
def check_if_sql_table_exists(cursor, table_name): ...
def get_sql_table_columns(cursor, table_name): ...
def download_sql_table(cursor, table_name, **id_columns): ...
def upload_sql_table(
    conn, cursor, table_name, table, index_name: Incomplete | None = ..., timestamp: bool = ..., **id_columns
) -> None: ...
def check_postgresql_catalogue_table(cursor, table_name, grid_id, grid_id_column, download: bool = ...) -> None: ...
def create_postgresql_catalogue_entry(conn, cursor, grid_id, grid_id_column, catalogue_table_name): ...
def add_timestamp_column(conn, cursor, table_name) -> None: ...
def create_sql_table_if_not_exists(conn, cursor, table_name, grid_id_column, catalogue_table_name) -> None: ...
def delete_postgresql_net(
    grid_id, host, user, password, database, schema, grid_id_column: str = ..., grid_catalogue_name: str = ...
) -> None: ...
def from_sql(
    conn,
    schema,
    grid_id,
    grid_id_column: str = ...,
    grid_catalogue_name: str = ...,
    empty_dict_like_object: Incomplete | None = ...,
): ...
def to_sql(
    net,
    conn,
    schema,
    include_results: bool = ...,
    grid_id: Incomplete | None = ...,
    grid_id_column: str = ...,
    grid_catalogue_name: str = ...,
    index_name: Incomplete | None = ...,
): ...
def to_sqlite(net, filename, include_results: bool = ...) -> None: ...
def from_sqlite(filename): ...
def to_postgresql(
    net,
    host,
    user,
    password,
    database,
    schema,
    include_results: bool = ...,
    grid_id: Incomplete | None = ...,
    grid_id_column: str = ...,
    grid_catalogue_name: str = ...,
    index_name: Incomplete | None = ...,
): ...
def from_postgresql(
    grid_id,
    host,
    user,
    password,
    database,
    schema,
    grid_id_column: str = ...,
    grid_catalogue_name: str = ...,
    empty_dict_like_object: Incomplete | None = ...,
): ...
