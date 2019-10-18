 # In dire need of optimization
import discord
import os
import json
from colorthief import ColorThief
from discord import Webhook, AsyncWebhookAdapter

# Avatar command
async def avatar_command(message):
        if (len(message.mentions) > 0):
            for user in message.mentions:
                print(user.avatar_url)
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
                await message.channel.send(embed=embed)
        else:
                requestor = message.author
                name = message.author.name
                avatarImage = Webhook.avatar_url_as(message.author, format=None, size=1024)
                os.system('curl -o .img.png {}'.format(avatarImage))
                color_thief = ColorThief('.img.png')
                dominant_color = color_thief.get_color(quality=1)
                os.system('rm .img.png')
                clr = '0x' + '%02X%02X%02X' % dominant_color
                clr = int(clr, base=16)
                embed = discord.Embed(title="Avatar of {}".format(name), value=requestor, color=clr)
                embed.set_image(url=avatarImage)
                await message.channel.send(embed=embed)


