"""
This is an example to show how to use discord.Permissions()
"""
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">", intents=intents)


# define objects with your desired permissions set to True
server_managers = discord.Permissions(manage_channels=True, manage_guild=True, manage_roles=True)
"""You can either manually set each permission's value"""
event_managers = discord.Permissions.events()
"""or You can use predefined methods of `discord.Permissions` class that suit your needs"""


# create roles using the defined permission objects
@bot.command(name="sm")
async def create_server_manager_role(ctx: commands.Context):
    await ctx.guild.create_role(name='Server Manager', permissions=server_managers)


@bot.command(name="em")
async def create_event_manager_role(ctx: commands.Context):
    await ctx.guild.create_role(name='Event Manager', permissions=event_managers)


# check if a role has `create_events` permission or not
@bot.command(name='ce')
async def show_event_manager_permissions(ctx: commands.Context, role: discord.Role):
    if role.permissions.create_events:
        await ctx.reply(f"{role.mention} has create_events permission")
    else:
        await ctx.reply(f"{role.mention} does not have create_events permission")


token = "your_token"
bot.run(token)
