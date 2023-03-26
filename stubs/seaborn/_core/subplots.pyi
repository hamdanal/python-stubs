from collections.abc import Generator

from matplotlib.axes import Axes as Axes
from matplotlib.figure import Figure as Figure, SubFigure as SubFigure
from seaborn._core.plot import FacetSpec as FacetSpec, PairSpec as PairSpec

class Subplots:
    subplot_spec: dict
    def __init__(self, subplot_spec: dict, facet_spec: FacetSpec, pair_spec: PairSpec) -> None: ...
    def init_figure(
        self,
        pair_spec: PairSpec,
        pyplot: bool = False,
        figure_kws: dict | None = None,
        target: Axes | Figure | SubFigure | None = None,
    ) -> Figure: ...
    def __iter__(self) -> Generator[dict, None, None]: ...
    def __len__(self) -> int: ...
