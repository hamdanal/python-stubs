from collections.abc import Sequence
from pathlib import Path
from typing import Any, Literal

import plotly.graph_objs as go  # type: ignore[import-not-found] # pyright: ignore[reportMissingImports]  # ty:ignore[unresolved-import]

def version_check() -> None: ...
def draw_layers(
    traces: Sequence[dict[str, Any]],
    num_layers: int = 0,
    on_map: bool = False,
    map_style: str = "basic",
    showlegend: bool = True,
    figsize: float = 1,
    aspectratio: tuple[float, float] | Literal["auto"] = "auto",
    filename: str | Path | None = None,
    auto_open: bool = True,
    **kwargs,
) -> go.Figure: ...
