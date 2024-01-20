from numpy.typing import ArrayLike

from shapely.geometry.base import BaseGeometry
from shapely.lib import Geometry
from shapely.prepared import PreparedGeometry

def contains(geometry: Geometry | PreparedGeometry[BaseGeometry], x: ArrayLike, y: ArrayLike): ...
def touches(geometry: Geometry | PreparedGeometry[BaseGeometry], x: ArrayLike, y: ArrayLike): ...
