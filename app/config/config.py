import os
from dotenv import load_dotenv


def get_env():
    return os.getenv("APP_ENV", "local")


def get_image_host_url():
    return os.getenv("IMAGE_HOST")


def create_database_uri() -> str:
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    return f"mysql+aiomysql://{username}:{password}@{host}:{port}/{dbname}"


def get_database_uri() -> str:
    app_env = get_env()
    env_file_name = f"envs/.env.{app_env}"
    load_dotenv(dotenv_path=env_file_name)
    return create_database_uri()


SQLALCHEMY_DATABASE_URI: str = get_database_uri()
