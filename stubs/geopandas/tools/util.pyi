from collections.abc import Iterable

import pandas as pd
from shapely.geometry.base import BaseGeometry

from ..geoseries import GeoSeries

def collect(
    x: Iterable[BaseGeometry] | GeoSeries | pd.Series[BaseGeometry] | BaseGeometry, multi: bool = False
) -> BaseGeometry: ...
