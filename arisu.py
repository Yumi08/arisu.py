import discord
import os
import time
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

# Import bot plugins.
from plugins import (color, help, img, log, mod, util, welcome)

token = os.environ.get("TOKEN")
prefix = os.environ.get("PREFIX")

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

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

## Avatar
    if message.content.startswith(prefix + 'avatar'):
        await img.avatar_command(message)

# Welome events
@client.event
async def on_member_join(member):
    await welcome.mem_join(member)

@client.event
async def on_member_remove(member):
    await welcome.mem_leave(member)

client.run(token)
