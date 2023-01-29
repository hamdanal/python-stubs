from _typeshed import Incomplete

from psycopg2.extras import Inet

class Macaddr(Inet):
    def getquoted(self) -> Incomplete: ...

class Macaddr8(Inet):
    def getquoted(self) -> Incomplete: ...

CIDRARRAY_OID: int
CIDRARRAY: Incomplete
MACADDRARRAY_OID: int
MACADDRARRAY: Incomplete
MACADDRARRAY8_OID: int
MACADDRARRAY8: Incomplete
