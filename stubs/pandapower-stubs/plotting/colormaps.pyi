from collections.abc import Collection, Iterable

from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap, LogNorm, Normalize
from matplotlib.typing import ColorType

def cmap_discrete(cmap_list: Iterable[tuple[tuple[float, float], ColorType]]) -> tuple[ListedColormap, BoundaryNorm]: ...
def cmap_continuous(cmap_list: Iterable[tuple[float, ColorType]]) -> tuple[LinearSegmentedColormap, Normalize]: ...
def cmap_logarithmic(
    min_value: float, max_value: float, colors: Collection[ColorType]
) -> tuple[LinearSegmentedColormap, LogNorm]: ...
