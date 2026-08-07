from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from langchain_groq import ChatGroq
from config.serverConfig import server_config
from functools import lru_cache


@lru_cache
def llm_client() -> ChatGroq:
    settings = server_config()
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=settings.GROQ_MODEL,
        temperature=settings.TEMPERATURE,
        max_tokens=settings.GROQ_MAX_TOKENS,
    )