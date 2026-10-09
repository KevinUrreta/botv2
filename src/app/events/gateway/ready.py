import discord
from discord.ext import commands


class Ready(commands.Cog):
    """
    Descripción del módulo de eventos.
    """

    def __init__(self, client: commands.Bot):
        """
        Inicializa el listener de eventos.

        :param client: Instancia principal del cliente.
        :type client: commands.Bot
        """
        self.client: commands.Bot = client

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        Descripción del evento.

        :return: None
        """
        self.client.logger.info(f"{self.client.user} ya está completamente cargado.")
