# Contributing to candiamazing

Thank you for your interest in contributing to `candiamazing`! We welcome contributions from everyone, whether you are fixing a typo, adding a new astronomical conversion, or improving the documentation.

This guide will walk you through the standard "GitHub Flow" used in open source projects.

## The Quick Version

1.  **Issue:** Find an open issue or open a new one to discuss your idea.
2.  **Fork:** Create a copy of this repository to your own GitHub account.
3.  **Branch:** Create a new branch for your specific change.
4.  **Code:** Write your code, tests, and documentation.
5.  **PR:** Submit a Pull Request to merge your changes back into the main project.

---

## Step-by-Step Guide

### 1. Find or Create an Issue
Before you start coding, it is best to check the [Issues tab](https://github.com/ConnorStoneAstro/candiamazing) to see if someone else is already working on the same thing.
* **Found a bug?** Open an issue describing the bug and how to reproduce it.
* **Want a new feature?** Open an issue to propose your idea (e.g., "Add redshift converter").

### 2. Fork the Repository
Click the **Fork** button in the top-right corner of this page. This creates a copy of the repository under your own GitHub username (e.g., `your-username/candiamazing`).

### 3. Clone and Set Up
Clone your fork to your local machine:

```bash
# Replace 'your-username' with your actual GitHub username
git clone https://github.com/your-username/candiamazing.git
cd candiamazing

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install the package in editable mode with dev dependencies
pip install -e ".[dev]"

```

### 4. Create a New Branch

Always create a new branch for your work. Do not work directly on the `main` branch. Name your branch something descriptive.

```bash
# Standard naming convention: type/description
git checkout -b feature/add-redshift-calc

```

### 5. Make Your Changes

Now, write your code!

* **Logic:** Add your math to `utils.py` or classes to `core.py`.
* **Tests:** If you add code, you **must** add a test in `tests/` to prove it works.
* **Docs:** If you change how a function works, update the docstring.

### 6. Check Your Code (Quality Control)

Before committing, run the project's quality tools to ensure your code is clean.

```bash
# Run the test suite
pytest

# Check code style
ruff check .

```

*Tip: If you set up `pre-commit` (see README), the ruff check happens automatically!*

### 7. Commit and Push

Once your tests pass, commit your changes.

```bash
git add .
git commit -m "Add redshift to velocity conversion function"
git push origin feature/add-redshift-calc

```

### 8. Open a Pull Request (PR)

1. Go to the original repository on GitHub.
2. You should see a banner asking if you want to **Compare & pull request**. Click it.
3. Fill in the template describing what you changed.
4. Click **Create pull request**.

### What Happens Next?

A maintainer will review your code. They might ask for changes (e.g., "Please add a comment explaining this formula"). Once everything looks good, your code will be merged!
