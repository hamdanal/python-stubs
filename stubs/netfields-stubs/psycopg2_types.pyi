from psycopg2._psycopg import _type
from psycopg2.extras import Inet

class Macaddr(Inet):
    def getquoted(self) -> bytes: ...

class Macaddr8(Inet):
    def getquoted(self) -> bytes: ...

CIDRARRAY_OID: int
CIDRARRAY: _type
MACADDRARRAY_OID: int
MACADDRARRAY: _type
MACADDRARRAY8_OID: int
MACADDRARRAY8: _type
