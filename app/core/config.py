"""
app name nerede kullanılıyor?
text analiz modellerini kullanmadan, llm ile analiz yapmaya çalış
"""

from dotenv import load_dotenv
load_dotenv()

import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    PROJECT_NAME: str = "Aspectify"
    PROJECT_VERSION: str = "1.0.0"
    LOG_LEVEL: str = "INFO"
    GOOGLE_API_KEY: SecretStr | None = None
    GEMINI_2_5_PRO_MODEL: str = "gemini-2.5-pro"

    # OPENAI_API_KEY: SecretStr | None = None
    # DATABASE_URL: SecretStr | None = None
    # PINECONE_API_KEY: SecretStr | None = None
    # PINECONE_ENVIRONMENT: SecretStr | None = None
    # PINECONE_INDEX_NAME: str = "aspectify-index"

settings = Settings()
