from _typeshed import Incomplete

class _LinearPlotter:
    data: Incomplete
    def establish_variables(self, data, **kws) -> None: ...
    def dropna(self, *vars) -> None: ...
    def plot(self, ax) -> None: ...

class _RegressionPlotter(_LinearPlotter):
    x_estimator: Incomplete
    ci: Incomplete
    x_ci: Incomplete
    n_boot: Incomplete
    seed: Incomplete
    scatter: Incomplete
    fit_reg: Incomplete
    order: Incomplete
    logistic: Incomplete
    lowess: Incomplete
    robust: Incomplete
    logx: Incomplete
    truncate: Incomplete
    x_jitter: Incomplete
    y_jitter: Incomplete
    color: Incomplete
    label: Incomplete
    x: Incomplete
    y: Incomplete
    x_discrete: Incomplete
    x_range: Incomplete
    def __init__(
        self,
        x,
        y,
        data: Incomplete | None = ...,
        x_estimator: Incomplete | None = ...,
        x_bins: Incomplete | None = ...,
        x_ci: str = ...,
        scatter: bool = ...,
        fit_reg: bool = ...,
        ci: int = ...,
        n_boot: int = ...,
        units: Incomplete | None = ...,
        seed: Incomplete | None = ...,
        order: int = ...,
        logistic: bool = ...,
        lowess: bool = ...,
        robust: bool = ...,
        logx: bool = ...,
        x_partial: Incomplete | None = ...,
        y_partial: Incomplete | None = ...,
        truncate: bool = ...,
        dropna: bool = ...,
        x_jitter: Incomplete | None = ...,
        y_jitter: Incomplete | None = ...,
        color: Incomplete | None = ...,
        label: Incomplete | None = ...,
    ) -> None: ...
    @property
    def scatter_data(self): ...
    @property
    def estimate_data(self): ...
    def fit_regression(self, ax: Incomplete | None = ..., x_range: Incomplete | None = ..., grid: Incomplete | None = ...): ...
    def fit_fast(self, grid): ...
    def fit_poly(self, grid, order): ...
    def fit_statsmodels(self, grid, model, **kwargs): ...
    def fit_lowess(self): ...
    def fit_logx(self, grid): ...
    def bin_predictor(self, bins): ...
    def regress_out(self, a, b): ...
    def plot(self, ax, scatter_kws, line_kws) -> None: ...
    def scatterplot(self, ax, kws) -> None: ...
    def lineplot(self, ax, kws) -> None: ...

def lmplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    hue: Incomplete | None = ...,
    col: Incomplete | None = ...,
    row: Incomplete | None = ...,
    palette: Incomplete | None = ...,
    col_wrap: Incomplete | None = ...,
    height: int = ...,
    aspect: int = ...,
    markers: str = ...,
    sharex: Incomplete | None = ...,
    sharey: Incomplete | None = ...,
    hue_order: Incomplete | None = ...,
    col_order: Incomplete | None = ...,
    row_order: Incomplete | None = ...,
    legend: bool = ...,
    legend_out: Incomplete | None = ...,
    x_estimator: Incomplete | None = ...,
    x_bins: Incomplete | None = ...,
    x_ci: str = ...,
    scatter: bool = ...,
    fit_reg: bool = ...,
    ci: int = ...,
    n_boot: int = ...,
    units: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    order: int = ...,
    logistic: bool = ...,
    lowess: bool = ...,
    robust: bool = ...,
    logx: bool = ...,
    x_partial: Incomplete | None = ...,
    y_partial: Incomplete | None = ...,
    truncate: bool = ...,
    x_jitter: Incomplete | None = ...,
    y_jitter: Incomplete | None = ...,
    scatter_kws: Incomplete | None = ...,
    line_kws: Incomplete | None = ...,
    facet_kws: Incomplete | None = ...,
): ...
def regplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    x_estimator: Incomplete | None = ...,
    x_bins: Incomplete | None = ...,
    x_ci: str = ...,
    scatter: bool = ...,
    fit_reg: bool = ...,
    ci: int = ...,
    n_boot: int = ...,
    units: Incomplete | None = ...,
    seed: Incomplete | None = ...,
    order: int = ...,
    logistic: bool = ...,
    lowess: bool = ...,
    robust: bool = ...,
    logx: bool = ...,
    x_partial: Incomplete | None = ...,
    y_partial: Incomplete | None = ...,
    truncate: bool = ...,
    dropna: bool = ...,
    x_jitter: Incomplete | None = ...,
    y_jitter: Incomplete | None = ...,
    label: Incomplete | None = ...,
    color: Incomplete | None = ...,
    marker: str = ...,
    scatter_kws: Incomplete | None = ...,
    line_kws: Incomplete | None = ...,
    ax: Incomplete | None = ...,
): ...
def residplot(
    data: Incomplete | None = ...,
    *,
    x: Incomplete | None = ...,
    y: Incomplete | None = ...,
    x_partial: Incomplete | None = ...,
    y_partial: Incomplete | None = ...,
    lowess: bool = ...,
    order: int = ...,
    robust: bool = ...,
    dropna: bool = ...,
    label: Incomplete | None = ...,
    color: Incomplete | None = ...,
    scatter_kws: Incomplete | None = ...,
    line_kws: Incomplete | None = ...,
    ax: Incomplete | None = ...,
): ...
