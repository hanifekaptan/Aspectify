# Configuration

Aspectify uses a centralized configuration system through the `app.core.config` module.

## Configuration File

The main configuration is defined in the `app/core/config.py` file:

```python
from dotenv import load_dotenv
load_dotenv()

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "Aspectify"
    PROJECT_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    GOOGLE_API_KEY: SecretStr | None = None
    GEMINI_2_5_PRO_MODEL: str = "gemini-2.5-pro"
```

## Environment Variables

Follow the instructions in the installation guide to create the `.env` file.

## Configuration Options

### Log Levels

Available log levels:

<!-- - `DEBUG`: Detailed information for debugging -->
- `INFO`: General information about program execution
<!-- - `WARNING`: Something unexpected happened
- `ERROR`: A serious problem occurred
- `CRITICAL`: A very serious error occurred -->

### AI Models

Currently supported Gemini models:

- `gemini-2.5-pro`: Latest Gemini model

## Using the Configuration

Access the configuration settings in your code:

```python
from app.core.config import settings

print(f"Project: {settings.PROJECT_NAME}")
print(f"Version: {settings.PROJECT_VERSION}")
print(f"Log Level: {settings.LOG_LEVEL}")

if settings.GOOGLE_API_KEY:
    api_key = settings.GOOGLE_API_KEY.get_secret_value()
```

## Validation

The configuration system uses Pydantic for validation:

-   It ensures correct data types through type checking.
-   It assigns reasonable default values.

## Troubleshooting

### Configuration Not Loading

1.  Check that the `.env` file is in the project's root directory.
2.  Verify the file permissions.
3.  Ensure there are no syntax errors in the `.env` file.

### API Key Issues

1.  Verify that the key was copied correctly (no extra spaces).
2.  Check that the key has the appropriate permissions.
3.  Make sure the key has not expired.

### Model Configuration

1.  Verify that the model name is correct.
2.  Check that the model is available in your region.
3.  Ensure the API key has access to the model.
