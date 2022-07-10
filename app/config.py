from pydantic import BaseSettings


class Settings(BaseSettings):
    d_hostname: str
    d_port: str
    d_password: str
    d_name: str
    d_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
