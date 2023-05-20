from typing import overload
from typing_extensions import Literal

from matplotlib.axes import Axes
from matplotlib.colors import Colormap, Normalize
from matplotlib.figure import Figure
from matplotlib.layout_engine import LayoutEngine
from matplotlib.markers import MarkerStyle as mpl_MarkerStyle
from matplotlib.path import Path
from matplotlib.scale import ScaleBase, scale_factory as scale_factory
from matplotlib.typing import FillStyleType
from numpy.typing import ArrayLike
from seaborn.external.version import Version as Version

def MarkerStyle(
    marker: str | ArrayLike | Path | mpl_MarkerStyle | None = None, fillstyle: FillStyleType | None = None
) -> mpl_MarkerStyle: ...
@overload
def norm_from_scale(scale: ScaleBase | None, norm: Normalize) -> Normalize: ...
@overload
def norm_from_scale(scale: None, norm: float | None) -> None: ...
@overload
def norm_from_scale(scale: ScaleBase, norm: float | None) -> Normalize: ...
def set_scale_obj(ax: Axes, axis: Literal["x", "y"], scale: ScaleBase) -> None: ...
def get_colormap(name: str | Colormap | None) -> Colormap: ...
def register_colormap(name: str | None, cmap: Colormap) -> None: ...
def set_layout_engine(
    fig: Figure, engine: Literal["constrained", "compressed", "tight", "none"] | LayoutEngine | None
) -> None: ...
def share_axis(ax0: Axes, ax1: Axes, which: Literal["x", "y"]) -> None: ...
