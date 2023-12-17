from numpy.typing import ArrayLike

from shapely.geometry.base import BaseGeometry
from shapely.prepared import PreparedGeometry

def contains(geometry: BaseGeometry | PreparedGeometry[BaseGeometry], x: ArrayLike, y: ArrayLike): ...
def touches(geometry: BaseGeometry | PreparedGeometry[BaseGeometry], x: ArrayLike, y: ArrayLike): ...
