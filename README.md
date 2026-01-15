# candiamazing: A Python Packaging Template

This repository demonstrates the canonical structure of a modern Python package. It is designed as a teaching tool to bridge the gap between writing one-off analysis scripts and building formally distributed packages.

The package implements simple astronomical conversions (flux/magnitudes and distance moduli) to illustrate where different types of logic should live in a production-grade library.

## Project Structure

For a user cloning this template, the directory structure looks like this:

```text
candiamazing/
├── src/candiamazing/      #  The Actual Source Code
│   ├── __init__.py        #   - Exposes the API
│   ├── cli.py             #   - Command Line Interface entry point
│   ├── core.py            #   - Classes & State (The "OO" layer)
│   └── utils.py           #   - Math & Physics (The functional layer)
│
├── tests/                 #  Unit Tests
│   ├── test_cli.py
│   └── test_core.py
|
├── docs/                  #  Documentation website
│
├── pyproject.toml         #  Build Configuration & Metadata
└── README.md              #  Brief Documentation

```

---

## Installation & Setup

To develop or use this package locally, you should install it in "editable" mode. This allows you to modify the code and see the changes immediately without reinstalling.

1. **Clone the repository:**
```bash
git clone [https://github.com/yourname/candiamazing.git](https://github.com/yourname/candiamazing.git)
cd candiamazing

```


2. **Create a Virtual Environment (Optional but highly Recommended):**
```bash
python -m venv candiamazing_venv
source candiamazing_venv/bin/activate

```


3. **Install in Editable Mode:**
The `-e` flag stands for "editable". The `.` means "look in the current directory". The "[dev]" means "install extra dependencies meant for working on the package" (think stuff like `pytest`)
```bash
pip install -e .[dev]

```


4. **Verify Installation:**
You should now be able to run the CLI tool from anywhere in your terminal:
```bash
candiamazing --help

```

---

## Running Tests

This template uses `pytest` for unit testing. The tests are located in the `tests/` directory and mirror the structure of the package.

1. **Install Test Dependencies:**
```bash
pip install pytest

```

2. **Run the Test Suite:**
```bash
cd tests
pytest

```

3. **Understanding the Output:**
Green dots (`.`) mean tests passed. Red `F`s mean failures.
* `test_core.py` validates the object oriented interface.
* `test_cli.py` mocks the command line to ensure the interface works.
* `test_utils.py` check core math/physics logic

---

## Configuration (`pyproject.toml`)

The `pyproject.toml` file is the heart of modern Python packaging. It replaces
the old `setup.py`. It defines the package name, version, dependencies, and CLI
entry points.

---

## Development Tools & Best Practices

To ensure code quality and reproducibility (essential for scientific software),
this template integrates several modern development tools.

### 1. Code Quality (`ruff` & `mypy`)
We use automated tools to catch bugs and enforce style before the code is even run.

* **Ruff:** A Python linter and formatter. It replaces tools like `flake8`, `isort`, and `black`. It ensures your imports are sorted and your code style is consistent.
* **Mypy:** A static type checker. It uses the type hints (like `flux: float`) in `core.py` to ensure you aren't accidentally passing bad arguments like strings into math functions.

**How to run them locally:**
```bash
# check for style errors
ruff check . 
# format code automatically
ruff format . 
# check for type errors
mypy .
```
But you won't need to do that because of `pre-commit`!

### 2. Automation (`pre-commit`)

It is easy to forget to run the linters before pushing to GitHub. **Pre-commit** solves this by installing a "git hook" that automatically runs `ruff` and `mypy` every time you try to make a commit.

**Setup (do this once):**

```bash
pip install pre-commit
cd candiamazing
pre-commit install
```

Now, if you try to commit messy code, git will stop you and fix the formatting
automatically! If it can't fix the formatting, you will get helpful messages
telling you what parts of the code need fixing. Note that these linters are very
"safe" in that they will not make any changes that break your code.

### 3. Documentation (`jupyter-book` & `ReadTheDocs`)

Scientific code needs examples. We use **Jupyter Book** to compile standard
Jupyter Notebooks (tutorials) and markdown files into a searchable website.
**ReadTheDocs** automatically builds and hosts the website so everyone can see
it.

* **Jupyter Book:** Builds the HTML site locally.
* **ReadTheDocs (RTD):** A hosting service that watches your GitHub repo. Whenever you push changes, RTD automatically builds the Jupyter Book and publishes it to the web.

**Building docs locally:**

```bash
jupyter-book build docs/
```

### 4. Coverage (`codecov`)

**Codecov** works with GitHub Actions to visualize what percentage of your code
is covered by unit tests. If you write a new function in `utils.py` but forget
to write a test for it, Codecov will flag a drop in coverage percentage in your
Pull Request. This will let you know about any untested code in your package
that needs more attention. It will give you a line by line view of what parts
you missed.