import numpy as np

import candiamazing.utils as utils


class BaseConverter:
    """A base class for conversions between flux and magnitude."""

    def __init__(self, description: str = "Base Converter"):
        self.description = description


class BrightnessConverter(BaseConverter):
    def __init__(self, zeropoint: float):
        super().__init__(description="Brightness Converter")
        self.zeropoint = zeropoint

    def flux_to_mag(self, flux: float | np.ndarray) -> float | np.ndarray:
        """Convert flux to magnitude using the stored zeropoint.

        Parameters
        ----------
        flux : float or np.ndarray
            The flux value(s) to convert.

        Returns
        -------
        float or np.ndarray
            The corresponding magnitude value(s).
        """
        return utils.flux_to_mag(flux, self.zeropoint)

    def mag_to_flux(self, mag: float | np.ndarray) -> float | np.ndarray:
        """Convert magnitude to flux using the stored zeropoint.

        Parameters
        ----------
        mag : float or np.ndarray
            The magnitude value(s) to convert.

        Returns
        -------
        float or np.ndarray
            The corresponding flux value(s).
        """
        return utils.mag_to_flux(mag, self.zeropoint)


class DistanceConverter(BaseConverter):
    """A class for converting between distance modulus and distance in parsecs."""

    def __init__(self):
        super().__init__(description="Distance Converter")

    def distmod_to_distance(self, distmod: float | np.ndarray) -> float | np.ndarray:
        """Convert distance modulus to distance in parsecs.

        Parameters
        ----------
        distmod : float or np.ndarray
            The distance modulus value(s) to convert.

        Returns
        -------
        float or np.ndarray
            The corresponding distance value(s) in parsecs.
        """
        return utils.distance_modulus_to_distance(distmod)

    def distance_to_distmod(self, distance: float | np.ndarray) -> float | np.ndarray:
        """Convert distance in parsecs to distance modulus.

        Parameters
        ----------
        distance : float or np.ndarray
            The distance value(s) in parsecs to convert.

        Returns
        -------
        float or np.ndarray
            The corresponding distance modulus value(s).
        """
        return utils.distance_to_distance_modulus(distance)
