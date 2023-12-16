from typing_extensions import deprecated

__all__ = ["available", "get_path"]

available: list[str]

@deprecated("Module `geopandas.dataset` is deprecated and will be removed in GeoPandas 1.0.")
def get_path(dataset: str) -> str: ...
