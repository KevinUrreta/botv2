from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra='ignore',
    )

    language: str | None = None
    discord_token: str | None = None
    youtube_oauth_refresh_token: str | None = None

    log_file: str | None = None

    postgres_db: str | None = None
    postgres_user: str | None = None
    postgres_password: str | None = None
    postgres_host: str | None = None
    postgres_port: str | None = None

    lavalink_uri: str | None = None
    lavalink_password: str | None = None
    lavalink_port: str | None = None
    lavalink_opus: str | None = None

    spotify_client_id: str | None = None
    spotify_secret_id: str | None = None

    @field_validator("*", mode="before")
    @classmethod
    def validate_not_empty(cls, value):
        """
        Comprueba si algún valor está vacío.
        :param value: valor secreto del entorno
        :raises: ValueError
        :return:
        """
        if value is None:
            raise ValueError("Environment variable cannot be empty")

        if isinstance(value, str) and not value.strip():
            raise ValueError("Environment variable cannot be empty")

        return value


settings = Settings()