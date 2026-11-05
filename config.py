from functools import lru_cache
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """App settings, read from environment variables, then `.env` in the project folder."""

    model_config = SettingsConfigDict(env_file=PROJECT_DIR / ".env", extra="ignore")

    fireworks_api_key: SecretStr
    llm_model: str = "accounts/fireworks/models/qwen3p8-max"
    llm_base_url: str = "https://api.fireworks.ai/inference/v1"


@lru_cache
def get_settings() -> Settings:
    """Load settings once, on first use (so importing modules never needs an API key)."""
    return Settings()  # pyright: ignore[reportCallIssue]  # values come from env / .env
