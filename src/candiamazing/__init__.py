from . import utils
from .core import BaseConverter, BrightnessConverter, DistanceConverter
from .test import test

try:
    from ._version import version as __version__  # noqa
except ImportError:
    __version__ = "0.0.0dev"

__author__ = "Connor Stone, Erik Osinga"

# List packages here to explicitly define the public API. Now candiamazing.<package> works.
__all__ = (
    "BaseConverter",
    "BrightnessConverter",
    "DistanceConverter",
    "utils",
    "test",
    "__version__",
    "__author__",
)
