from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET : str
    JWT_ALGORITHM : str
    ACCESS_TOKEN_EXPIRY : int = 3600
    REFRESH_TOKEN_EXPIRY : int = 2

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()
