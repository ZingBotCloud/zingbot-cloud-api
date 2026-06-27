import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "ZingBot Cloud API"

    APP_VERSION = "1.0.0"

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "CHANGE_ME_IN_PRODUCTION"
    )

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./zingbot.db"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24


settings = Settings()
