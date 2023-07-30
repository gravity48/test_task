from pydantic.v1 import BaseSettings


class DatabaseSettings(BaseSettings):
    HOST: str
    PORT: str
    DB: str
    USER: str
    PASSWORD: str

    class Config:
        env_prefix = 'POSTGRES_'


__all__ = [
    'DatabaseSettings',
]
