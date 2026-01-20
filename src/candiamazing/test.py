"""
test.py
=======

**Author:** Connor Stone

**Description:**
This module contains a built-in "sanity check" or "smoke test" for the package.
It is designed to be run by the end-user after installation to ensure that
the package was installed correctly and basic functions are working.

**Development Notes (Instructional):**
1. **Unit Tests vs. Smoke Tests:**
   You might wonder: "Why do we have tests here *and* in the `tests/` directory?"
   * The **`tests/` directory** (using `pytest`) is for YOU (the developer). It is thorough,
       covers edge cases, and requires extra tools to run.
   * **This file** is for the USER. It allows them to run a quick check
       (e.g., `candiamazing.test()`) without needing to clone the repository
       or install developer tools like `pytest`.

2. **Zero Dependencies:**
   Notice that this file uses standard Python `assert` statements and `print()`
   instead of a framework. This is intentional. We want this script to run
   in any environment where the package is installed, even if the user
   doesn't know what `pytest` is.

3. **Exposing the Function:**
   To make this accessible, you would typically import this function in your
   `__init__.py` so a user can simply run:
   >>> import candiamazing
   >>> candiamazing.test()
"""

import numpy as np

from .core import DistanceConverter
from .utils import flux_to_mag, mag_to_flux


def test():
    """Quick basic tests to make sure the candiamazing package was installed correctly"""

    # Test flux utils
    for flux in [1, 10, 100]:
        for zeropoint in [0, 10, 21.4]:
            mag = flux_to_mag(flux, zeropoint)
            flux_back = mag_to_flux(mag, zeropoint)

            # These are the actual "tests"
            assert abs(flux - flux_back) < 1e-10, "Round trip flux -> mag -> flux failed"

            assert np.allclose(
                mag, (zeropoint - 2.5 * np.log10(flux))
            ), "flux_to_mag calculation incorrect"

            assert np.allclose(
                flux, (10 ** ((zeropoint - mag) / 2.5))
            ), "mag_to_flux calculation incorrect"

    dist_tool = DistanceConverter()
    for D, mu in [
        (10.0, 0.0),  # By definition, at 10pc, m-M = 0
        (100.0, 5.0),  # 10x distance adds 5 magnitudes
        (1e6, 25.0),  # 1 Mpc -> DM=25
    ]:
        calculated_dm = dist_tool.distance_to_distmod(D)

        assert np.allclose(calculated_dm, mu)

    print("All tests passed!")
