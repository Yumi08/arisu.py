import discord
import os
from dotenv import load_dotenv
load_dotenv()

# Import bot plugins.
from plugins import (color, help, img, log, mod, util, welcome)

token = os.environ.get("TOKEN")
prefix = os.environ.get("PREFIX")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('Hello! The prefix is ' + prefix)

# Util
@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'code'):
        url = 'https://github.com/TheSorton/arisu.py'
        await message.channel.send(url)
    if message.content.startswith(prefix + 'embed'):
        from discord import Webhook, AsyncWebhookAdapter
        requestor = message.author
        name = message.author.name
        avatarImage = Webhook.avatar_url_as(message.author, format=None, size=1024)
        embed = discord.Embed(title="Avatar of {}".format(name), value=requestor, color=0x00ff00)
        embed.set_image(url=avatarImage)
        await message.channel.send(embed=embed))
    
# Welcome
#@client.event
#async def on_member_join(member):
    #await client.send_message("Yeet")
#async def on_member_remove(member):
    #await client.send_message("Yote")

client.run(token)
