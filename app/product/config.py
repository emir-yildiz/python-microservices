from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    database_url: str
    log_level: str = "INFO"
    app_port: int = 8001
    api_key: str

    model_config = {"env_file": ".env"}