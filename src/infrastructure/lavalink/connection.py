from logging import Logger

import wavelink
from wavelink import (
    AuthorizationFailedException,
    InvalidClientException,
    NodeException,
)


class Lavalink:
    """
    Gestor de conexiones para Lavalink usando Wavelink.
    """

    @staticmethod
    async def connect(bot, uri: str, password: str, logger: Logger) -> None:
        """
        Establece conexión con el servidor si no existe una activa.
        :param bot: Instancia principal del cliente.
        :param uri: Dirección del servidor
        :type uri: str
        :param password: Autenticación al servidor
        :type password: str
        :param logger:
        :type logger: Logger
        :return: None
        """
        if wavelink.Pool.nodes:
            return
        logger.info(f"Connecting to Lavalink node {uri}")

        try:
            await wavelink.Pool.connect(
                nodes=[
                    wavelink.Node(
                        identifier="main",
                        uri=uri,
                        password=password,
                    )
                ],
                client=bot,
            )
        except (
            AuthorizationFailedException,
            InvalidClientException,
            NodeException,
        ) as exc:
            raise RuntimeError(
                f"Failed to connect to Lavalink node {uri}: {exc}"
            ) from exc