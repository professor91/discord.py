"""
This file is part of extensions example `extension.py`

An extension is simply a python module which has a setup function as an entry point for the bot.

Note: you cannot define events in extensions directly (checkout Cogs for that)
"""
from discord.ext import commands


# you can write commands, cogs, views etc. like you used to do in `bot.py` and
# then add them to your bot in `setup` function
@commands.command()
async def hello(ctx: commands.Context):
    await ctx.reply(f'Hello {ctx.author.display_name}.')


async def setup(bot):
    bot.add_command(hello)
    """Commands, cogs, views etc. defined in this extension are added to the bot here. If they are not added here your
    bot will simply deny their existence"""
