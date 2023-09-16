"""
This is an example to show how to use extensions

Extensions allow developers to organize bot's functionalities into multiple python modules and make changes to the bot
in runtime.
"""
import discord
from discord.ext import commands


class MyBot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True
        command_prefix = ">"

        super().__init__(command_prefix, intents=intents)

    async def setup_hook(self) -> None:
        await self.load_extension("extension_file")     # load the extension file using its name without the .py
        """Note: you shouldn't load an extension in `on_ready` since it is called multiple times within a lifetime of the bot"""


bot = MyBot()


@bot.command(name='reload')
async def reload_extension(ctx: commands.Context, ext_name: str):
    await bot.reload_extension(ext_name)
    """Hot reload the extension i.e. if you made any changes to an extension, you can test them without restarting the bot
    by just hot reloading that extension"""


token = "your_token"
bot.run(token)
