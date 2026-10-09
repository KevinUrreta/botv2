from discord.ext import commands


class Volume(commands.Cog):
    """
    Descripción del módulo.
    """
    def __init__(self, client: commands.Bot):
        """
        Inicializa el comando.
        :param client: Instancia principal del cliente
        :type client: commands.Bot
        """
        self.client: commands.Bot = client

    @commands.command(name='volume', help='Does something')
    async def volume(self, ctx: commands.Context):
        """
        Descripción del comando.
        :param ctx: Contexto del comando
        :return: None
        """
        pass