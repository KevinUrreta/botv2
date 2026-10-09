import discord
from discord.ext import commands


class UserUpdate(commands.Cog):
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
    async def on_user_update(self, before: discord.Member, after: discord.Member):
        """
        Descripción del evento.

        :return: None
        """
        if before.name != after.name:
            self.client.logger.info(f"Usuario: {before.name} -> {after.name}")
        if before.global_name != after.global_name:
            self.client.logger.info(f"Nombre global: {before.name} -> {after.name}")
        if before.avatar != after.avatar:
            self.client.logger.info(f"Avatar: {before.avatar} -> {after.avatar}")
