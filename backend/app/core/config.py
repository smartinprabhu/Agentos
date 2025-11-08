from pydantic_settings import BaseSettings
from pathlib import Path

env_path = Path(__file__).parent.parent.parent / '.env'


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    NVIDIA_API_KEY: str
    NVIDIA_API_BASE_URL: str = "https://integrate.api.nvidia.com/v1"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = env_path


settings = Settings()
