from dotenv import dotenv_values

config_values = dotenv_values()

database_name = config_values.get("DATABASE_NAME")
database_username = config_values.get("DATABASE_USERNAME")
database_password = config_values.get("DATABASE_PASSWORD")

database_uri = f"mysql://{database_username}:{database_password}@localhost/{database_name}"


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = database_uri
