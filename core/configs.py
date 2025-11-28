from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    DATABASE_URL: str = (
        f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )  

    OPENAI_API_KEY: str

    MIN_SCRIPT_NAME_LENGTH: int = 3
    MAX_SCRIPT_NAME_LENGTH: int = 5
    REPEAT_SCRIPT_NAME_GENERATE = 3
    IF_SCRIPT_NAME_EXISTS: int = 10
    NAME_CHOICES: str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0987654321"

    ANSWER_PATH: str = "./answers"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()