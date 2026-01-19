import numpy as np
import pytest

from candiamazing.core import BrightnessConverter, DistanceConverter


# Fixtures allow you to setup data or objects once and reuse them in multiple tests.
# This mimics a real workflow: "Initialize the telescope/instrument once, then use it."
@pytest.fixture
def standard_converter():
    """Returns a BrightnessConverter initialized with a standard zeropoint of 25.0."""
    return BrightnessConverter(zeropoint=25.0)


def test_flux_to_mag_simple(standard_converter):
    """Test simple flux to magnitude conversion using the fixture."""
    # Math: m = -2.5 * log10(100) + 25.0  --> -2.5 * 2 + 25 = 20.0
    flux = 100.0
    expected_mag = 20.0

    # We assert that the calculated value is approximately equal to the expected value
    assert standard_converter.flux_to_mag(flux) == pytest.approx(expected_mag)


def test_mag_to_flux_simple(standard_converter):
    """Test simple magnitude to flux conversion."""
    # Math: f = 10**((25 - 20) / 2.5) --> 10**2 = 100.0
    mag = 20.0
    expected_flux = 100.0

    assert standard_converter.mag_to_flux(mag) == pytest.approx(expected_flux)


# Instead of writing three separate tests for three different stars, we write one test
# and "feed" it different inputs. This is cleaner and easier to expand.
@pytest.mark.parametrize(
    "distance_pc, expected_distmod",
    [
        (10.0, 0.0),  # By definition, at 10pc, m-M = 0
        (100.0, 5.0),  # 10x distance adds 5 magnitudes
        (1e6, 25.0),  # 1 Mpc -> DM=25
    ],
)
def test_distance_modulus_values(distance_pc, expected_distmod):
    """Check distance modulus calculations for known standard distances."""
    dist_tool = DistanceConverter()
    calculated_dm = dist_tool.distance_to_distmod(distance_pc)

    assert calculated_dm == pytest.approx(expected_distmod)


def test_array_handling(standard_converter):
    """Ensure the converter works on numpy arrays, not just single floats."""
    fluxes = np.array([10.0, 100.0, 1000.0])
    # Expected: 10x flux steps should equal -2.5 magnitude steps
    # If 100 flux -> 20 mag, then 10 -> 22.5 mag, 1000 -> 17.5 mag
    expected_mags = np.array([22.5, 20.0, 17.5])

    calculated_mags = standard_converter.flux_to_mag(fluxes)

    # pytest.approx works on arrays too!
    assert calculated_mags == pytest.approx(expected_mags)


# It is important to verify that your code fails when it is supposed to fail.
# Here we check that passing a string (text) instead of a number raises a TypeError.
def test_invalid_input_raises_error(standard_converter):
    """Test that invalid input types raise a TypeError."""
    bad_input = "not_a_number"

    # The test passes ONLY if the code inside the 'with' block raises TypeError
    with pytest.raises(TypeError):
        standard_converter.flux_to_mag(bad_input)
