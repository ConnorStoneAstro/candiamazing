# Main package directory

This repository demonstrates the canonical structure of a modern Python package. It is designed as a teaching tool to bridge the gap between writing one-off analysis scripts and building formally distributed packages.

The package implements simple astronomical conversions (flux/magnitudes and distance moduli) to illustrate where different types of logic should live in a production-grade library.

## Package Layout & Philosophy

When structuring a package, the goal is **Separation of Concerns**. We separate the "heavy lifting" (classes/logic), the low-level utilities (stateless math), and the user interface (CLI).

### 1. `core.py`: The Object-Oriented Interface
This module contains the primary high-level interface that users will interact with in their Python scripts. It typically houses classes that manage **state** (like configurations, instrument parameters, or constants) and provide methods for the user.

* **Role:** Defines the user-facing API.
* **Example content:** The `BrightnessConverter` class, which stores a `zeropoint` state so the user doesn't have to pass it repeatedly during an analysis pipeline.

#### Usage Example
Users import from the package (typically exposed via `__init__.py`) to use in their scripts:

```python
import numpy as np
from candiamazing.core import BrightnessConverter, DistanceConverter

# 1. Using the Class-based interface for Magnitude conversions
# We initialize the converter once with our instrument's zeropoint
# This is "stateful" usage—the object remembers the ZP.
converter = BrightnessConverter(zeropoint=25.0)

# Convert an array of source fluxes
fluxes = np.array([100.0, 500.0, 1000.0])
mags = converter.flux_to_mag(fluxes)
print(f"Magnitudes: {mags}")

# 2. Using the Distance Converter
dist_tool = DistanceConverter()
d_mod = 34.5  # Approx distance modulus for the Virgo Cluster
distance_pc = dist_tool.distmod_to_distance(d_mod)

print(f"Distance to source: {distance_pc / 1e6:.2f} Mpc")

```

### 2. `utils.py`: The Functional Backend

This module contains **pure functions** (stateless logic). These functions take inputs and return outputs without storing data or requiring class instantiation. This is where the raw physics and math live.

* **Role:** Reusable, modular logic.
* **Relationship:** It is imported by `core.py` to power the high-level classes, and by `cli.py` for quick one-off calculations.
* **Why split it?** If you later decide to build a GUI or a web app, you can reuse `utils` without dragging in the command-line parsing logic or specific class structures.


### 3. `cli.py`: The Command Line Interface (CLI)

This file serves as the entry point for the terminal. It uses the standard library `argparse` to map shell commands to Python functions.

* **Role:** Translates text inputs (strings from the terminal) into Python types (floats, ints) and passes them to the logic functions in `utils.py`.
* **Key concept:** The CLI is just a **wrapper**. Notice that `cli.py` contains almost no math; it simply parses arguments and delegates the work to `utils`.

#### Terminal Usage

Once installed, users can access the `candiamazing` entry point directly from their shell (e.g., bash or zsh).

**Convert Flux to Magnitude:**

```bash
# Syntax: candiamazing flux_to_mag <flux> <zeropoint>
candiamazing flux_to_mag 3631 8.9
# Output: -1.5 (approx)

```

**Convert Magnitude to Flux:**

```bash
# Syntax: candiamazing mag_to_flux <mag> <zeropoint>
candiamazing mag_to_flux 20.0 25.0
# Output: 100.0

```

#### How to link CLI

To turn these files into a command line tool, you add some lines to the `pyproject.toml` file at the root directory. This configuration file handles build dependencies and defines the executable script entry point.

Example `pyproject.toml` snippet for the CLI:

```toml
[project.scripts]
candiamazing = "candiamazing.cli:main"

```

This tells pip during installation: *When the user types `candiamazing` in their terminal, run the `main()` function inside `cli.py`.*

### 4. `__init__.py`: The Package Gateway

This file turns a simple directory of scripts into a formal Python package. It executes automatically when the package is imported.

* **Role:** Exposes the API and manages namespace.
* **Why it matters:** Without this file, a user would have to type `from candiamazing.core import BrightnessConverter`. With the imports configured in `__init__.py`, the user can simply type `from candiamazing import BrightnessConverter`.

#### Flattening the Namespace

In our example, we import key classes from `core.py` directly into the package root. This hides the internal file structure from the user, making the API cleaner and easier to remember.

**Resulting Import Structure:**

```python
# Clean, flat import (Thanks to __init__.py)
import candiamazing
converter = candiamazing.BrightnessConverter(zeropoint=25.0)

# Accessing submodule utilities
flux = candiamazing.utils.mag_to_flux(20, 25.0)

```

