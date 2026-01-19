import numpy as np
import pytest

from candiamazing.utils import (
    distance_modulus_to_distance,
    distance_to_distance_modulus,
    flux_to_mag,
    mag_to_flux,
)


@pytest.mark.parametrize("zeropoint", [8.9, 25.0, 30.0])  # run test with three values for zeropoint
@pytest.mark.parametrize(
    "flux", [1.0, 10.0, 3631.0, np.array([1.0, 10.0, 3631.0])]
)  # run test with multiple values/types for flux
def test_flux_mag(zeropoint, flux):
    # check round trip conversion
    mag = flux_to_mag(flux, zeropoint)
    flux_back = mag_to_flux(mag, zeropoint)

    # These are the actual "tests"
    assert np.all(np.abs(flux - flux_back) < 1e-10), "Round trip flux -> mag -> flux failed"

    assert np.all(mag == pytest.approx(zeropoint - 2.5 * np.log10(flux))), (
        "flux_to_mag calculation incorrect"
    )

    assert np.all(flux == pytest.approx(10 ** ((zeropoint - mag) / 2.5))), (
        "mag_to_flux calculation incorrect"
    )


@pytest.mark.parametrize(
    "distmod, distance",
    [
        (0.0, 10.0),
        (5.0, 100.0),
        (10.0, 1000.0),
    ],
)  # Test with pairs of values
def test_distance_modulus_distance(distmod, distance):
    # Test distmod to distance
    distance_calculated = distance_modulus_to_distance(distmod)
    assert distance_calculated == pytest.approx(distance), (
        "Distance modulus to distance calculation incorrect"
    )

    # Test distance to distmod
    distmod_calculated = distance_to_distance_modulus(distance)
    assert distmod_calculated == pytest.approx(distmod), (
        "Distance to distance modulus calculation incorrect"
    )
