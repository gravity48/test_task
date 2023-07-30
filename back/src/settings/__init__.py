import os

from dotenv import load_dotenv

from .db import DatabaseSettings
from .scheduler import scheduler

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))


db = DatabaseSettings()

__all__ = ['db', 'scheduler']
