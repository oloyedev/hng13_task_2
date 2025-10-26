from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DB_HOST_NAME: str
    DB_PORT: int
    DB_PASSWORD: str
    DB_USERNAME: str
    DB_NAME: str
    COUNTRY_API_URL: str
    EXCHANGE_RATE_API_URL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
