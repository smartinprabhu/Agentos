from pydantic import BaseSettings, Field
import os

class Settings(BaseSettings):
    """
    Application settings are managed by this class.
    It loads environment variables and provides them to the application.
    """
    # NVIDIA API Configuration
    NVIDIA_API_KEY: str = Field(..., env="NVIDIA_API_KEY")
    NVIDIA_API_BASE: str = Field("https://integrate.api.nvidia.com/v1", env="NVIDIA_API_BASE")

    # Database Configuration
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    # Redis Configuration
    REDIS_HOST: str = Field("localhost", env="REDIS_HOST")
    REDIS_PORT: int = Field(6379, env="REDIS_PORT")

    # API Server Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AGNO Marketplace"

    # CORS Origins - comma-separated string
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost:3000", "http://localhost:8000"]

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

