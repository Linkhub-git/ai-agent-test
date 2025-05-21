from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    OPENAI_API_KEY: str = "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"

settings = Settings()