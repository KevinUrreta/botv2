# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio

import discord
from discord.ext import commands

from src.core.config import settings
from src.core.loader import Loader


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        loader = Loader(self)
        await loader.load_cogs()

async def main( ) -> None:
    # Use a breakpoint in the code line below to debug your script.
    client = Client()
    async with client:
        await client.start(token=settings.discord_token) # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
