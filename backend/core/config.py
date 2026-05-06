from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./restopulse.db"
    GROQ_API_KEY: str = ""
    LLM_MODEL_NAME: str = "llama-3.3-70b-versatile"

    model_config = {"env_file": ".env"}


settings = Settings()
