from _typeshed import Incomplete

from django.db.models import lookups
from django.db.models.fields import Field, related_lookups
from django.db.models.fields.related import ForeignObject

class InValuesLookupMixin:
    def as_sql(self, compiler: Incomplete, connection: Incomplete) -> str: ...

@Field.register_lookup
class InValuesLookup(InValuesLookupMixin, lookups.In): ...

@ForeignObject.register_lookup
class InValuesRelatedLookup(InValuesLookupMixin, related_lookups.RelatedIn): ...
