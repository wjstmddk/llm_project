import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", "1000"))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))
    SYSTEM_PROMPT: str = (
        "You are a helpful AI assistant. Answer questions clearly and concisely."
    )
