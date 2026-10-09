import discord
from discord.ext import commands


class MemberUpdate(commands.Cog):
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
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        """
        Descripción del evento.

        :return: None
        """
        changes = {}
        if before.name != after.name:
            changes["name"] = after.name

        if before.display_name != after.display_name:
            changes["display_name"] = after.display_name

        if not changes:
            return
        self.client.logger.info(
            f"{after.id} -> {before.name} -> {after.name}"
        )
