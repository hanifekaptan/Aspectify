# Production Deployment Guide

This guide explains how to deploy the Aspectify application to a production environment **as a persistent and stable service**.

**Prerequisite:** Before starting this guide, it is assumed that you are familiar with the project's basic setup steps. If necessary, please review the **[Main Installation Guide](../getting-started/installation.md)** first.

## 1. Configuration for Production

Unlike the development environment, some values in the `.env` file need to be set carefully for a production environment.

1.  Navigate to the project's root directory on your server.
2.  Create your `.env` file using the command: `cp .env.example .env`.
3.  Open the `.env` file and ensure you **specifically set the following values** for production:

    ```dotenv
    # .env (Critical Fields for Production)

    # APPLICATION SETTINGS
    # This disables the application's debug mode and improves performance.
    ENVIRONMENT=production

    # SECURITY
    # Enter a long, complex, and unpredictable key.
    # You can generate one with a command like `openssl rand -hex 32`.
    SECRET_KEY=your_very_strong_and_random_secret_key_goes_here

    # LOGGING
    # Use INFO or WARNING in production to avoid unnecessary logs.
    LOG_LEVEL=INFO

    # EXTERNAL SERVICE API KEYS
    # Ensure that all API keys are the ones intended for production.
    GEMINI_API_KEY=[YOUR_PRODUCTION_GEMINI_API_KEY]
    ```

**Important Note:** The project is currently in active development. Docker support, database integration, and an API layer are not yet available. This guide describes how to run the project in its current command-line-based state.