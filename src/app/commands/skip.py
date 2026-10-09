from discord.ext import commands


class Skip(commands.Cog):
    """

    """

    def __init__(self, client: commands.Bot):
        """
        Inicializa el comando
        :param client:
        """
        self.client: commands.Bot = client

    @commands.command(name='skip', help='Does something')
    async def skip(self, ctx: commands.Context):
        """

        :param ctx: Contexto del comando
        :return:
        """
        pass