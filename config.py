from dataclasses import dataclass
from environs import Env


@dataclass
class Config:
    WTF_CSRF_ENABLED: bool
    WTF_CSRF_SECRET_KEY: str
    SECRET_KEY: str


def load_config(path: str = '.env'):
    env = Env()
    env.read_env(path)

    return Config(
        WTF_CSRF_ENABLED=env.bool("WTF_CSRF_ENABLED"),
        WTF_CSRF_SECRET_KEY=env.str("WTF_CSRF_SECRET_KEY"),
        SECRET_KEY=env.str("SECRET_KEY"),
        )
    
def load_port(path: str = '.env'):
    env = Env()
    env.read_env(path)
    return env.str("PORT")
