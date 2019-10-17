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
client = discord.Client()

# Startup
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


# a!hello
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello! The prefix is ' + prefix)

# Util
## Code
@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'code'):
        await util.code_command(message)

    elif message.content.startswith(prefix + 'kick'):
        await mod.kick(message)

    elif message.content.startswith(prefix + 'ban'):
        await mod.ban(message)
## Avatar
    elif message.content.startswith(prefix + 'avatar'):
        await img.avatar_command(message)

# Welcome events
@client.event
async def on_member_join(member):
    await welcome.mem_join(member)

@client.event
async def on_member_remove(member):
    await welcome.mem_leave(member)

# Run it 
client.run(token)
