from logging import Logger

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)


class Database:
    """
    Gestiona conexiones asíncronas para PostgreSQL usando SQLAlchemy
    """

    def __init__(self, url: str, logger: Logger) -> None:
        """
        Inicializa la conexión de la base de datos
        :param url: URL de la base de datos
        :type url: str
        """
        self.url: str = url
        self.logger: Logger = logger

        try:
            self.engine: AsyncEngine = create_async_engine(
                url,
                echo=False,
            )

            self.session: async_sessionmaker[AsyncSession] = async_sessionmaker[AsyncSession](
                self.engine,
                expire_on_commit=False,
            )
            self.logger.info(f"Database connection established from {self.url}.")


        except (SQLAlchemyError, Exception) as exc:
            error_msg = f"Unable to connect to PostgreSQL in {self.url}: {exc}"
            self.logger.error(error_msg)
            raise RuntimeError(error_msg) from exc

    async def close(self) -> None:
        """
        Cierra la conexión con PostgreSQL
        :return: None
        """
        if hasattr(self, "engine"):
            await self.engine.dispose()
            self.logger.info(f"Database connection closed from {self.url}.")
