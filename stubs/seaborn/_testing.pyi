from collections.abc import Sequence

import numpy as np
from matplotlib.artist import Artist
from matplotlib.axes import Axes
from matplotlib.legend import Legend
from matplotlib.typing import ColorType

USE_PROPS: list[str]

def assert_artists_equal(list1: Sequence[Artist], list2: Sequence[Artist]) -> None: ...
def assert_legends_equal(leg1: Legend, leg2: Legend) -> None: ...
def assert_plots_equal(ax1: Axes, ax2: Axes, labels: bool = True) -> None: ...
def assert_colors_equal(a: ColorType | np.ndarray, b: ColorType | np.ndarray, check_alpha: bool = True) -> None: ...
