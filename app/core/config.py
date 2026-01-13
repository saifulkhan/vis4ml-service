from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    application settings loaded from environment variables.

    configuration is loaded from:
    1. environment variables
    2. .env file (if present)
    3. default values
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # application environment
    ENVIRONMENT: Literal["development", "staging", "production"] = Field(
        default="development", description="application environment"
    )

    # server configuration
    PORT: int = Field(default=8000, description="server port")
    HOST: str = Field(default="0.0.0.0", description="server host")

    # logging
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="logging level"
    )

    # cors configuration
    CORS_ORIGINS: str = Field(default="*", description="allowed cors origins")

    # api configuration
    API_VERSION: str = Field(default="v1", description="api version")
    API_PREFIX: str = Field(default="/api", description="api prefix")

    @property
    def cors_origins_list(self) -> list[str]:
        """parse cors origins from comma-separated string"""

        if self.CORS_ORIGINS == "*":
            return ["*"]
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",")]

    @property
    def is_production(self) -> bool:
        """check if running in production"""

        return self.ENVIRONMENT == "production"

    @property
    def api_base_path(self) -> str:
        """get the full api base path including version"""

        return f"{self.API_PREFIX}/{self.API_VERSION}"


config = Settings()
