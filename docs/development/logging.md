# Logging Guide for Developers

## Using the Logger

The application's main logger can be imported from the `app.core.logging_config` module. However, the best practice is for each module to create its own logger instance.

```python
import logging

# Create a module-specific logger
logger = logging.getLogger(__name__)

# Use the logger
logger.info("This module has been initialized.")
```

## Log Levels and Their Use Cases

Choosing the correct log level ensures that logs are meaningful and effective.

| Level | Description | When to Use |
| :--- | :--- | :--- |
| `DEBUG` | Detailed information, typically of interest only when diagnosing problems. | When tracking the value of a variable or the flow of a function. |
| `INFO` | Informational messages that highlight the normal progress of the application. | To indicate that an operation has started, finished, or reached a significant milestone. |
| `WARNING` | An indication that something unexpected happened, but the application is still working as expected. | For potential issues like a slow response from an API or a temporary connection problem. |
| `ERROR` | A serious error that prevented the application from performing a specific operation. | For situations like a database connection failure, a file not being found, or invalid input. |
| `CRITICAL` | A very serious error, indicating that the program itself may be unable to continue running. | For systemic crises like running out of disk space or memory. |

## Error Handling and Logging

When logging errors, it is important to provide as much context as possible. Logging within `try...except` blocks is standard practice.

```python
try:
    # An operation that might fail
    result = risky_operation()
    logger.info("Risky operation completed successfully.")
except Exception as e:
    # The exc_info=True parameter adds the exception's stack trace to the log.
    # This is vital for debugging.
    logger.error(f"An unexpected error occurred: {e}", exc_info=True)
    raise  # Re-raise the exception to halt the program's flow
```

## Security: Avoid Logging Sensitive Information

**Never** log sensitive information such as user passwords, API keys, tokens, or personal data.

```python
# ❌ WRONG APPROACH
logger.debug(f"User login attempt: {username}, password: {password}")

# ✅ CORRECT APPROACH
logger.info(f"User login attempt: {username}")
```

If necessary, use helper functions to mask data before logging it.
