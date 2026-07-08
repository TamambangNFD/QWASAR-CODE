"""
Centralized application configuration.
All values are overridable via environment variables (see .env.example).
This is the single source of truth for config across every future service —
do not hardcode connection strings or secrets anywhere else in the codebase.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- App ---
    APP_NAME: str = "IDAP"
    ENVIRONMENT: str = "development"  # development | staging | production
    DEBUG: bool = True

    # --- Database ---
    DATABASE_URL: str = "postgresql://idap:idap@db:5432/idap"

    # --- Cache / Queue ---
    REDIS_URL: str = "redis://redis:6379/0"

    # --- Auth (wired up fully in Take 2) ---
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # --- CORS ---
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
