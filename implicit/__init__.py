from . import als, approximate_als, nearest_neighbours
from .als import alternating_least_squares

__version__ = '0.3.4'

__all__ = [alternating_least_squares, approximate_als, als, nearest_neighbours, __version__]
