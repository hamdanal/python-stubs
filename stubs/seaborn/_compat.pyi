from _typeshed import Incomplete

from seaborn.external.version import Version as Version

def MarkerStyle(marker: Incomplete | None = ..., fillstyle: Incomplete | None = ...): ...
def norm_from_scale(scale, norm): ...
def scale_factory(scale, axis, **kwargs): ...
def set_scale_obj(ax, axis, scale) -> None: ...
def get_colormap(name): ...
def register_colormap(name, cmap) -> None: ...
def set_layout_engine(fig, engine) -> None: ...
def share_axis(ax0, ax1, which) -> None: ...
