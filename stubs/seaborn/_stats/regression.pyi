from seaborn._stats.base import Stat as Stat

class PolyFit(Stat):
    order: int
    gridsize: int
    def __call__(self, data, groupby, orient, scales): ...
    def __init__(self, order, gridsize) -> None: ...

class OLSFit(Stat): ...
