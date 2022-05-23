"""
    Config environment variables reader.
"""

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    """ Base settings. """
    database_url: PostgresDsn

    proxy_url_prefix: str
    proxy_url_host: str


_settings = Settings()

def get_settings():
    return _settings
