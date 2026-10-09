import discord
from discord.ext import commands


class GuildUpdate(commands.Cog):
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
    async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
        """
        Descripción del evento.

        :return: None
        """
        self.client.logger.info(
            f"El servidor '{before.name}' (ID: {after.id}) ha sido actualizado."
        )
