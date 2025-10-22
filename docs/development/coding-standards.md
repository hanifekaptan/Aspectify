# Coding Standards and Git Workflow

This document serves as a guide to ensure the quality, readability, and long-term maintainability of the code in the Aspectify project. Our core philosophy is based on the principles of "Clean Code," which means our goal is not just for the code to work, but also for it to be easily understood by another developer (including our future selves).

To achieve this goal, we adhere to **[PEP 8](https://peps.python.org/pep-0008/)**, Python's official style guide.

## Coding Standards

Adherence to the following rules and best practices is expected to ensure code quality and consistency.

### 1. Naming Conventions

The following naming conventions have been adopted to ensure consistency throughout the project:

-   **Variables, Functions, and Modules:** Should be named using lowercase letters with underscores between words (`snake_case`).
    -   *Examples:* `process_data`, `user_name`
-   **Classes:** Should be named using the `PascalCase` convention (each word starts with a capital letter).
    -   *Examples:* `AnalysisService`, `MultiModalRequest`
-   **Constants:** Should be named using all capital letters with underscores between words (`SCREAMING_SNAKE_CASE`).
    -   *Examples:* `MAX_RETRIES`, `DEFAULT_TIMEOUT`

### 2. Comments and Docstrings

Clear code is self-documenting code. However, when necessary, it is crucial to explain *why* the code is written a certain way.

-   Use inline comments (starting with `#`) to explain code blocks that are complex or difficult to understand.
-   All public modules, classes, and functions should include a docstring (`"""Docstring here."""`) that explains what they do, the parameters they take, and the value they return. This helps with code comprehension and facilitates automatic documentation generation in the future.

### 3. Readability and Simplicity

-   **Single Responsibility Principle:** Avoid making a function do too many things. Whenever possible, each function should have a single, well-defined responsibility.
-   **Don't Repeat Yourself (DRY):** Prevent code duplication by moving repetitive logic into helper functions or classes.
-   **Line Length:** To make code easier to read on different screens, it is a widely accepted practice to keep the line length ideally around 80-100 characters.

## Git Workflow

A clean Git history is one of our most valuable tools for understanding the project's evolution and tracking down potential bugs.

### 1. Branch Management

For each new task, create a new branch from the `main` branch. This ensures that the main branch remains stable at all times. Branch names should use the following prefixes to summarize the work being done:

-   **`feature/`**: When adding a new feature (e.g., `feature/add-caching`)
-   **`fix/`**: When fixing a bug (e.g., `fix/login-bug`)
-   **`docs/`**: For documentation-related changes (e.g., `docs/update-readme`)

### 2. Commit Messages

A clear project history is at least as valuable as the code itself. Therefore, we follow the "Conventional Commits" standard.

-   **Format:** `<type>: <short description>`
-   **Example Types:**
    -   **`feat`**: For a new feature.
    -   **`fix`**: For a bug fix.
    -   **`docs`**: For documentation-only changes.
    -   **`style`**: For formatting changes that do not affect the meaning of the code.
    -   **`refactor`**: For a code change that neither fixes a bug nor adds a feature.
    -   **`test`**: For adding missing tests or correcting existing tests.
    -   **`chore`**: For changes to the build process or auxiliary tools.

-   **Good Commit Message Examples:**
    ```
    feat: Add multi-modal request support for audio files
    fix: Correctly handle Unicode characters in text analysis
    docs: Update local setup guide with Docker instructions
    ```