from _typeshed import Incomplete

from matplotlib.colors import Colormap

def get_plotly_color(color_string: str) -> str: ...
def get_plotly_color_palette(n) -> list[str]: ...
def get_plotly_cmap(
    values: Incomplete, cmap_name: Colormap | str | None = "jet", cmin: float | None = None, cmax: float | None = None
) -> list[str]: ...
