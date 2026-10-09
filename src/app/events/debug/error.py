from discord.ext import commands


class Error(commands.Cog):
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
    async def on_error(self):
        """
        Descripción del evento.

        :return: None
        """
        self.client.logger.error(
            f"{self.__class__.__name__}: {self.__class__.__doc__}"
        )
