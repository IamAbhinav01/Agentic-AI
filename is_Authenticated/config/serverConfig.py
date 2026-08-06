import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import lru_cache

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class Settings(BaseSettings):
    APP_NAME : str = "AGENTIC_AI_WORKFLOWS"
    GROQ_API_KEY:str
    GROQ_MODEL:str = "llama-3.1-8b-instant"
    GROQ_MAX_TOKENS:int = 4096
    TEMPERATURE:float = 0.7

    llm_config = SettingsConfigDict(env_file='.env',env_file_encoding='utf-8',extra=True)

@lru_cache
def server_config()->Settings:
    return Settings()