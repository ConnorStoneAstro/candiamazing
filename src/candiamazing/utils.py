"""
utils.py
========

**Author:** Connor Stone

**Description:**
This module provides the low-level mathematical utilities for the `candiamazing` package.
It contains the raw physics equations for astronomical conversions (flux, magnitude, distance).

**Development Notes (Instructional):**
1. **What belongs here?** In a standard package layout, the `utils` module should hold "pure functions"—functions
   that produce output based *only* on their inputs, without side effects or maintaining state
   (like `self.zeropoint`). These are the atomic building blocks of your library. By keeping
   them separate from `core.py` (classes) and `cli.py` (interface), you ensure they can be
   easily reused anywhere (e.g., in a GUI, a web app, or a script).

2. **Scaling Up:**
   Currently, this is a single file because the package is small. In a large production code,
   if this file grew to 1000+ lines, it would be standard practice to convert `utils.py` into
   a directory (`utils/`) containing multiple specific files (e.g., `utils/photometry.py`,
   `utils/cosmology.py`), while using `__init__.py` to keep the import paths clean.
"""

import numpy as np


def flux_to_mag(flux: float | np.ndarray, zeropoint: float) -> float | np.ndarray:
    """Convert flux to magnitude using the given zeropoint.

    Parameters
    ----------
    flux : float or np.ndarray
        The flux value(s) to convert.
    zeropoint : float
        The zeropoint for the magnitude system.


    Returns
    -------
    float or np.ndarray
        The corresponding magnitude value(s).

    See Also
    --------
    mag_to_flux : Convert magnitude to flux.
    """
    return -2.5 * np.log10(flux) + zeropoint


def mag_to_flux(mag: float | np.ndarray, zeropoint: float) -> float | np.ndarray:
    """Convert magnitude to flux using the given zeropoint.

    Parameters
    ----------
    mag : float or np.ndarray
        The magnitude value(s) to convert.
    zeropoint : float
        The zeropoint for the magnitude system.

    Returns
    -------
    float or np.ndarray
        The corresponding flux value(s).

    See Also
    --------
    flux_to_mag : Convert flux to magnitude.
    """
    return 10 ** ((zeropoint - mag) / 2.5)


def distance_modulus_to_distance(distmod: float | np.ndarray) -> float | np.ndarray:
    """Convert distance modulus to distance in parsecs.

    Parameters
    ----------
    distmod : float or np.ndarray
        The distance modulus value(s) to convert.

    Returns
    -------
    float or np.ndarray
        The corresponding distance value(s) in parsecs.

    See Also
    --------
    distance_to_distance_modulus : Convert distance in parsecs to distance modulus.
    """
    return 10 ** ((distmod + 5) / 5)


def distance_to_distance_modulus(distance: float | np.ndarray) -> float | np.ndarray:
    """Convert distance in parsecs to distance modulus.

    Parameters
    ----------
    distance : float or np.ndarray
        The distance value(s) in parsecs to convert.

    Returns
    -------
    float or np.ndarray
        The corresponding distance modulus value(s).

    See Also
    --------
    distance_modulus_to_distance : Convert distance modulus to distance in parsecs.
    """
    return 5 * np.log10(distance) - 5
