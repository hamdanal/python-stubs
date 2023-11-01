import numpy
import pandas

import geopandas

from . import datasets as datasets
from ._config import options as options
from .array import points_from_xy as points_from_xy
from .geodataframe import GeoDataFrame as GeoDataFrame
from .geoseries import GeoSeries as GeoSeries
from .io.arrow import _read_feather, _read_parquet
from .io.file import _read_file
from .io.sql import _read_postgis
from .tools import clip as clip, overlay as overlay, sjoin as sjoin, sjoin_nearest as sjoin_nearest
from .tools._show_versions import show_versions as show_versions

read_file = _read_file
read_feather = _read_feather
read_parquet = _read_parquet
read_postgis = _read_postgis

gpd = geopandas
np = numpy
pd = pandas
__version__: str
