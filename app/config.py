import os
from dataclasses import dataclass

from dotenv import load_dotenv
from loguru import logger

load_dotenv()


@dataclass
class Config:
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME")  # Логин для авторизации

    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD")  # Пароль для авторизации

    SERVER_IP: str = os.getenv("SERVER_IP")  # Айпи сервера

    SERVER_PORT: str = os.getenv("SERVER_IP")  # Порт для открытия API приложения

    CYPHER_KEY: str = os.getenv("CYPHER_KEY")  # Ключ шифрования для авторизации администратора

    DATABASE_URL: str = "sqlite:///database.db"  # URL базы данных для sqlalchemy

    LOGS_PATH: str = "logs/app.log"  # Путь до файла с логами


# Set up logging
logger.remove()
logger.add(Config.LOGS_PATH,
           format="<white>{time: %d.%m %H:%M:%S.%f}</white> | "
                  "<level>{level}</level>| "
                  "|{name} {function} line:{line}| "
                  "<bold>{message}</bold>",
           rotation="5 MB",
           compression='zip')
