from matplotlib.axes import Axes

from pandapower._typing import Float, Int

def plot_pq_area(
    pq_area,
    *,
    title: str | None = None,
    ax: Axes | None = None,
    saturate_sn_pu: Float = ...,
    circle_segment: Int = 90,
    p_samples=None,
    tex: bool = False,
) -> None: ...
def plot_qv_area(qv_area, title=None, ax: Axes | None = None, prune_to_flexibility=False, vm_samples=None, tex: bool = False): ...
def generate_circle_segment(center_x, center_y, radius, start, stop, step): ...
