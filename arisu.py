import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get("TOKEN")
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


client.run(TOKEN)

