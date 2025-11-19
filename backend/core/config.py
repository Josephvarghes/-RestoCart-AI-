from pydantic_settings import BaseSettings  

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./restopulse.db"
    GROQ_API_KEY: str = ""

    model_config = {  
        "env_file": ".env"
    }

settings = Settings()