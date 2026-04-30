import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    openai_api_key: str = Field(
        default="",
        description="OpenAI API key (env: OPENAI_API_KEY).",
    )

    def resolved_openai_api_key(self) -> str:
        return (self.openai_api_key or os.environ.get("OPENAI_API_KEY", "")).strip()


settings = Settings()
