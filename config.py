from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    COHERE_API_KEY: str = "zWAVUdlyYIlHYB8Kw1MxhdBUDV6nMTy1OQ8gvvDw"
    QDRANT_URL: str = "https://863916fc-6774-44b8-98dd-1feb6478294f.us-east4-0.gcp.cloud.qdrant.io:6333"
    QDRANT_API_KEY: str = "2kvNbZSxikGMMMIBVMs8jw6kGaAcoREXtLyEGV8Amubg2lyF097QPQ"


settings = Settings()