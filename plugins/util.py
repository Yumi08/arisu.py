import os
import discord
from colorthief import ColorThief


async def code_command(message):
    url = 'https://github.com/TheSorton/arisu.py'
    await message.channel.send(url)


def find_member(message, nickname):
    """
    Finds the first memeber that matches the nickname
    on the guild where the message was sent.

    Parameters
    ----------
    message : discord.Message
        Message that triggered the event.
    nickname : str
        nickname of the user that might be
        on the same guild where the message
        was delivared.

    Returns
    -------
    member : discord.Member
        First discord member that matches the nickname.
        If no member was found that matches the nickname
        None will be returned.
    """
    for member in message.guild.members:
        if nickname in member.nick:
            await member

    None

def create_avatar_embed(message, user):
    """
    Creates an embed object that will contain the avatar
    of the user and will 'mention' the author of the original
    message.

    Paramters
    ---------
    message : discord.Message
        Message that triggered the event.
    user : discord.Member
        User from which it's avatar is going to be retrieved.

    Returns
    -------
    embed : discord.Embed
        embed containing the avatar of the user.
    """

    requestor = message.author
    name = user.name
    avatarImage = user.avatar_url
    os.system('curl -o .img.png {}'.format(avatarImage))
    color_thief = ColorThief('.img.png')
    dominant_color = color_thief.get_color(quality=1)
    os.system('rm .img.png')
    clr = '0x' + '%02X%02X%02X' % dominant_color
    clr = int(clr, base=16)
    embed = discord.Embed(title="Avatar of {}".format(name), value=requestor, color=clr)
    embed.set_image(url=avatarImage)

    embed
