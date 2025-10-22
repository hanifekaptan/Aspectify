# Testing Guide

## Test Philosophy and Future Vision

-   **Unit Tests:** These are tests that verify the correct functionality of each function or class in isolation from other components. They ensure the robustness of the code's fundamental building blocks.
-   **Integration Tests:** These tests check that multiple modules work together in harmony (for example, an API endpoint calling a service). They provide information about the overall health of the system.

**Current Status:** At this stage of the project, the testing infrastructure has been planned, and test coverage is actively under development. The goal is for all future features and bug fixes to be submitted with corresponding tests.

## Tools to be Used

We will use **Pytest**, the standard tool in the Python ecosystem, for writing and running tests in our project.

-   **Installation:** Pytest will be included among the project's development dependencies by being added to the `requirements.txt` (or `requirements-dev.txt`) file.

## Running Tests

Once the test suite is established, the following command will be used to run all tests from the project's root directory:

```bash
pytest
```

## How to Write New Tests

The following structure and standards will be followed for tests to be written in the future.

### 1. File Structure and Naming

-   All test files will be located in the `tests/` folder in the project's root directory.
-   The internal structure of the `tests/` folder will mirror the structure of the `app/` folder, which contains the source code.
-   The names of test files and functions must start with the `test_` prefix.

**Example Structure:**

```
├── app/
│   └── logic/
│       └── language_detector.py
└── tests/
    └── logic/
        └── test_language_detector.py
```

### 2. Example of Writing a Test

Below is an example of how to write a test for a simple helper function.

**Function to be Tested (`app/utils/formatters.py`):**

```python
def normalize_text(text: str) -> str:
    """Converts text to lowercase and strips leading/trailing whitespace."""
    if not isinstance(text, str):
        return ""
    return text.strip().lower()
```

**Test Code (`tests/utils/test_formatters.py`):**

```python
from app.utils.formatters import normalize_text

def test_normalize_text_with_mixed_case_and_whitespace():
    """Should correctly normalize text with mixed case and whitespace."""
    assert normalize_text("  Hello World  ") == "hello world"

def test_normalize_text_with_empty_string():
    """Should return an empty string when given an empty string."""
    assert normalize_text("") == ""

def test_normalize_text_with_already_normalized_string():
    """Should not change an already normalized string."""
    assert normalize_text("already normal") == "already normal"
```

This guide serves as a starting point for establishing a consistent and effective testing culture in the Aspectify project.