import discord
from discord.ext import commands


class MemberJoin(commands.Cog):
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
    async def on_member_join(self, member: discord.Member):
        """
        Descripción del evento.

        :return: None
        """
        self.client.logger.info(
            f"Miembro nuevo: {member.name} | ID: {member.id} en {member.guild.name}"
        )
