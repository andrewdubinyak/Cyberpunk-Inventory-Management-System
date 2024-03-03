import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


class AppConfig(BaseModel):
    """Settings for application"""

    app_name: str = Field(default="Inventory Management System")
    app_port: int = Field(default=8000)
    debug: bool = Field(default=False)


class PostgresConfig(BaseModel):
    """Settings for PSQL database"""

    postgres_port: int
    postgres_host: str
    postgres_db: str
    postgres_user: str
    postgres_password: str


class Config(BaseModel):
    """Application configuration"""

    app_config: AppConfig
    postgres_config: PostgresConfig


def load_config() -> Config:
    """GET service config"""
    return Config(
        app_config=AppConfig(
            app_name=os.environ.get(
                "INVENTORY_MANAGEMENT_APP_NAME", "Inventory Management System"
            ),
            app_port=os.environ.get("INVENTORY_MANAGEMENT_PORT"),
            debug=os.environ.get("DEBUG"),
        ),
        postgres_config=PostgresConfig(
            postgres_host=os.environ.get("POSTGRES_HOST"),
            postgres_port=os.environ.get("POSTGRES_PORT"),
            postgres_db=os.environ.get("POSTGRES_DB"),
            postgres_user=os.environ.get("POSTGRES_USER"),
            postgres_password=os.environ.get("POSTGRES_PASSWORD"),
        ),
    )
