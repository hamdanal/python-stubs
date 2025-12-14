from typing import Literal

from django.db import models

class NetManager[M: models.Model](models.Manager[M]):
    use_for_related_fields: Literal[True]
