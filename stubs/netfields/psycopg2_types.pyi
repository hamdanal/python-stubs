from _typeshed import Incomplete

from psycopg2.extras import Inet

class Macaddr(Inet):
    def getquoted(self) -> bytes: ...

class Macaddr8(Inet):
    def getquoted(self) -> bytes: ...

# ***ARRAY are psycopg type-casting objects (`psycopg2._psycopg.type`) with:
# - name: str
# - values: tuple[int, ...]
# - __call__: Callable[[?, ?], ?]
# - __eq__, __ge__, __gt__, __le__, __lt__, __ne__: Callable[[?], bool]
CIDRARRAY_OID: int
CIDRARRAY: Incomplete
MACADDRARRAY_OID: int
MACADDRARRAY: Incomplete
MACADDRARRAY8_OID: int
MACADDRARRAY8: Incomplete
