import os


async def code_command(message):
    url = 'https://github.com/TheSorton/arisu.py'
    await message.channel.send(url)


async def find_member(message, nickname):
    for member in message.guild.members:
        if nickname in member.nick:
            await member

    await None
