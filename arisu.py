import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


# Import bot "plugins".
from plugins import color, bot_help, img, log, mod, util, welcome

# Vars
token = os.environ.get("TOKEN")
prefix = os.environ.get("PREFIX")
bot = commands.Bot(command_prefix=f'{prefix}')

# Startup
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


# a!hello
@bot.command()
async def hi(ctx):
    """ Hi """
    await ctx.send("hi")

## Commands ##

@bot.command()
async def say(ctx, arg):
    """ Repeat after me """
    await ctx.send(arg)

@bot.command()
async def avatar(ctx):
    """ Get an avatar """
    await  img.avatar_command(ctx.message)

@bot.command()
async def pape(ctx):
    """ Get a pape. No search query gives a random wallpaper."""
    await img.pape(ctx.message)

@bot.command()
async def memcount(ctx):
    """ Counts all the members in a guild """
    await util.memcount(ctx.message)

# Welcome events
@bot.event
async def on_member_join(member):
    await welcome.mem_join(member)

@bot.event
async def on_member_remove(member):
    await welcome.mem_leave(member)

# Run it 
bot.run(token)
