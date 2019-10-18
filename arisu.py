import discord
import os
import time
from colorthief import ColorThief
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

@bot.command()
async def avatar(ctx, member: discord.Member): # Somehow, this needs to be moved to plugin/img.py
                avatarImage = member.avatar_url
                os.system('curl -o .img.png {}'.format(avatarImage))
                color_thief = ColorThief('.img.png')
                dominant_color = color_thief.get_color(quality=1)
                os.system('rm .img.png')
                clr = '0x' + '%02X%02X%02X' % dominant_color
                clr = int(clr, base=16)
                embed = discord.Embed(title="Avatar of {}".format(member.name), color=clr)
                embed.set_image(url=avatarImage)
                await ctx.send(embed=embed)

# Welcome events
@bot.event
async def on_member_join(member):
    await welcome.mem_join(member)

@bot.event
async def on_member_remove(member):
    await welcome.mem_leave(member)

# Run it 
bot.run(token)
