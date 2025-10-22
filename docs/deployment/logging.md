# Logging System Configuration and Management

## Overview

-   **Log File:** All logs are written to the `logs/app.log` file in the application's root directory.
-   **Configuration:** The log level and other settings are controlled via environment variables.
-   **Log Rotation:** To prevent the log file from growing excessively, it is automatically rotated when its size reaches 10MB, and the last 5 files are kept.

## Configuration

To control the log level, set the following variable in your `.env` file or in the server's environment variables.

```env
# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
# The recommended level for production environments is INFO or WARNING.
LOG_LEVEL=INFO
```

## Log Format

All log entries are written in a standard format to facilitate analysis:

-   **Format:** `Timestamp - Logger Name - Level - Message`
-   **Example:** `2024-01-15 10:30:45,123 - app.agents.absa_agent - INFO - ABSA analysis initiated`

## Log File Management

### Log Rotation

The logging system automatically manages log files using `RotatingFileHandler`.

-   **Maximum File Size:** `10 MB`
-   **Backup Count:** `5` (app.log, app.log.1, ..., app.log.4)

These settings are defined in the `app/core/logging_config.py` file and should be updated there if changes are needed.

### Log Cleanup

The application does not include a built-in mechanism for automatically cleaning up old log files. To prevent disk space issues on the server, it is recommended to periodically archive or delete old files in the `logs/` directory using standard system tools like `logrotate` (on Linux) or scheduled tasks (cron jobs).

## Security Notes

-   **Access Control:** Access to the `logs/` directory and its log files should be restricted to authorized users and system services only.
-   **Sensitive Information:** As per development standards, sensitive information should not be present in the logs. However, to protect against potential leaks, log files should not be considered secure.
