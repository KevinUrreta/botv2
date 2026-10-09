# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio

import discord
from discord.ext import commands

from src.core.config import settings
from src.core.loader import Loader
from src.core.logger import logger
from src.infrastructure.database.connection import Database
from src.infrastructure.lavalink.connection import Lavalink


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())
        self.postgres = Database(url=settings.postgres_url, logger=logger)


    async def setup_hook(self) -> None:
        await Loader(self, logger).load_cogs()
        await Lavalink.connect(
            bot=self,
            uri=settings.lavalink_uri,
            password=settings.lavalink_password,
            logger=logger
        )

    async def close(self) -> None:
        if hasattr(self, "postgres"):
            await self.postgres.close()
        await super().close()

async def main( ) -> None:
    # Use a breakpoint in the code line below to debug your script.
    client = Bot()
    async with client:
        await client.start(token=settings.discord_token) # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
