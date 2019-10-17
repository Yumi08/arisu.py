import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


# Import bot "plugins".
from plugins import (color, help, img, log, mod, util, welcome)

# Vars
token = os.environ.get("TOKEN")
prefix = os.environ.get("PREFIX")
bot = commands.Bot(command_prefix='{}'.format(prefix))

# Startup
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))


# a!hello
@bot.command()
async def hi(ctx):
    await ctx.send("hi")

## Commands ##

@bot.command()
async def foo(ctx, arg):
    await ctx.send(arg)


# Welcome events
@bot.event
async def on_member_join(member):
    await welcome.mem_join(member)

@bot.event
async def on_member_remove(member):
    await welcome.mem_leave(member)

# Run it 
bot.run(token)
