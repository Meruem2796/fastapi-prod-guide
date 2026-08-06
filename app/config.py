from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path


class Settings(BaseSettings):
    mongo_uri: str
    github_oauth_client_id: str
    github_oauth_client_secret: str
    root_path: str = ""
    logging_level: str = "INFO"
    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env",
        extra="ignore",
    )


settings = Settings()
