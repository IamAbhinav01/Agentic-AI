from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import ClassVar

REPO_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = REPO_ROOT / '.env'
load_dotenv(ENV_PATH)

class Settings(BaseSettings):
    APP_NAME : str = "AGENTIC_AI_WORKFLOWS"
    GROQ_API_KEY : str
    GROQ_MODEL : str = "llama-3.1-8b-instant"
    GROQ_MAX_TOKENS : int = 4096
    TEMPERATURE : float = 0.7

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding='utf-8',
        extra='allow',
    )

@lru_cache
def server_config() -> Settings:
    return Settings()