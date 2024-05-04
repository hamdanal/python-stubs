from django import db
from psycopg import Error as _Psycopg3Error  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]
from psycopg2 import Error as _Psycopg2Error

Psycopg2Error: type[_Psycopg2Error] | None
Psycopg3Error: type[_Psycopg3Error] | None

def extract_postgres_error(error: db.Error) -> _Psycopg2Error | _Psycopg3Error | None: ...
def extract_postgres_error_code(error: db.Error) -> str | None: ...
