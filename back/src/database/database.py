from asyncio import current_task
from contextlib import asynccontextmanager

from settings import db
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=MetaSingleton):
    def __init__(self):
        self._engine = create_async_engine(
            f"postgresql+asyncpg://{db.USER}:{db.PASSWORD}@{db.HOST}:{db.PORT}/{db.DB}",
        )
        self._session_factory = async_scoped_session(
            async_sessionmaker(
                self._engine,
                class_=AsyncSession,
                expire_on_commit=False,
            ),
            scopefunc=current_task,
        )

    @asynccontextmanager
    async def session(self):
        session: AsyncSession = self._session_factory()
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
