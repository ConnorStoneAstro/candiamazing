# Unit Testing Guide (`tests/`)

This directory contains the automated test suite for `candiamazing`. We use **pytest**, the industry-standard framework for testing Python code.

## What is Pytest?
Pytest is a tool that finds and runs your tests. It is designed to be:
1.  **Automatic:** It crawls your directory looking for files starting with `test_` and runs them.
2.  **Simple:** You don't need to write complex classes. A test is just a function starting with `test_`.
3.  **Informative:** When a test fails, it prints a detailed breakdown of exactly *why* the values didn't match.

## How to Run Tests

From the root directory of the repository (one level up), run:

```bash
# Run all tests
pytest

# Run with verbose output (shows each individual test name)
pytest -v

# Run tests only in a specific file
pytest tests/test_core.py

# Run only tests that match a specific name pattern (e.g., only flux tests)
pytest -k "flux"

```

---

## Common Testing Patterns

If you are writing a new test, here are the standard patterns ("idioms") we use in this project.

### 1. The Basic Assertion

In older frameworks, you had to remember methods like `self.assertEqual(a, b)`. In pytest, you just use the standard Python `assert` keyword.

```python
def test_simple_math():
    x = 10
    y = 10
    assert x == y  # If this fails, pytest prints the values of x and y

```

### 2. Handling Floating Point Math (`approx`)

**Crucial for Astronomy:** Computers cannot store infinite precision. `1.0 / 3.0 * 3.0` often equals `0.999999999`, not `1.0`.
Never use `==` for floats. Use `pytest.approx()`.

```python
import pytest

def test_physics_calculation():
    result = some_complex_calculation()
    expected = 5.0
    
    # Passes if result is within 1e-6 of expected
    assert result == pytest.approx(expected)
    
    # You can also specify tolerance
    assert result == pytest.approx(expected, rel=1e-3)

```

### 3. Fixtures (Setup & Teardown)

If multiple tests need the same expensive setup (like loading a large catalog or initializing a telescope object), use a **Fixture**.

```python
@pytest.fixture
def hubble_telescope():
    """Sets up a complex object once for reuse."""
    telescope = Instrument(name="HST", zeropoint=25.0)
    return telescope

def test_observation(hubble_telescope):
    # Pytest automatically passes the return value of the fixture into the argument
    assert hubble_telescope.name == "HST"

```

### 4. Parametrization (Testing Multiple Inputs)

Instead of writing three copy-pasted tests for three different stars, use parametrization to run the same logic on a table of inputs.

```python
@pytest.mark.parametrize("input_flux, expected_mag", [
    (100.0, 20.0),
    (1000.0, 17.5),
    (10000.0, 15.0),
])
def test_flux_conversion_loop(input_flux, expected_mag):
    """Runs 3 times with different values."""
    converter = BrightnessConverter(zeropoint=25.0)
    assert converter.flux_to_mag(input_flux) == pytest.approx(expected_mag)

```

### 5. Expected Failures

Sometimes you *want* your code to crash (e.g., if a user inputs a negative flux). You should test that your code raises the correct error.

```python
def test_negative_flux_error():
    converter = BrightnessConverter(zeropoint=25.0)
    
    # The test passes ONLY if ValueError is raised inside this block
    with pytest.raises(ValueError):
        converter.flux_to_mag(-100.0)

```

### 6. Mocking (Faking Inputs)

Used primarily in `test_cli.py`. If a function relies on something external (like the command line `sys.argv` or an internet connection), we "mock" it to fake the input. This ensures our tests are isolated and don't depend on the environment.

We use the `monkeypatch` fixture (built-in to pytest) for this.

```python
def test_command_line(monkeypatch):
    # Fake the user typing "candiamazing --help"
    monkeypatch.setattr("sys.argv", ["candiamazing", "--help"])
    
    # Run the code
    main()

```

