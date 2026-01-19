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
