import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


# Import bot "plugins".
from plugins import color, bot_help, img, mod, util, welcome

# Vars
token = os.environ.get("TOKEN")
prefix = os.environ.get("PREFIX")
logchan = os.environ.get("LOGCHAN")
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

class Utils(commands.Cog):

    @commands.command()
    async def say(self, ctx, arg):
        """ Repeat after me """
        await ctx.send(arg)

    @commands.command()
    async def avatar(self, ctx):
        """ Get an avatar """
        await  img.avatar_command(ctx.message)

    @commands.command()
    async def memcount(self, ctx):
            """ Counts all the members in a guild """
            await util.memcount(ctx.message)

bot.add_cog(Utils())


class Image(commands.Cog):

    @commands.command()
    async def pape(self, ctx):
        """ Get a pape. No search query gives a random wallpaper."""
        await img.pape(ctx.message)

bot.add_cog(Image())

class Admin(commands.Cog):

    @commands.command()
    async def kick(self, ctx):
        """ Kicks a member """
        await mod.kick(ctx.message)

    @commands.command()
    async def ban(self, ctx):
        """ Bans a member """
        await mod.ban(ctx.message)

    @commands.command()
    async def mute(self, ctx):
        """ Mutes a member """
        await mod.mute(ctx.message)

    @commands.command()
    async def unmute(self, ctx):
        """ Unmutes a member """
        await mod.unmute(ctx.message)

    @commands.command()
    async def purge(self, ctx):
        """Purges 'n' messages"""
        args = ctx.message.content.split()

        if len(args) >= 2:
            n_purge = int(args[1])
            await mod.purge(ctx.message, n_purge)

bot.add_cog(Admin())

# Welcome events
@bot.event
async def on_member_join(member):
    await welcome.mem_join(member)
    await log_member_join(member) # Bad solution please fix

@bot.event
async def on_member_remove(member):
    await welcome.mem_leave(member)
    await log_member_leave(member) # Also this

# Logging events
@bot.event
async def on_message_delete(message):
    embed = discord.Embed(title="Message Deleted")
    embed.add_field(name="Content", value=message.content)
    channel = bot.get_channel(int(logchan))
    await channel.send(embed = embed)

@bot.event
async def on_message_edit(message1, message2):
    embed = discord.Embed(title="Message Edited")
    embed.add_field(name="From", value=message1.content)
    embed.add_field(name="To", value=message2.content)
    channel = bot.get_channel(int(logchan))
    await channel.send(embed = embed)

async def log_member_join(member):
    embed = discord.Embed(title="Member Joined")
    embed.add_field(name="Name", value=member)
    embed.set_footer(text=f'ID: {member.id}')
    channel = bot.get_channel(int(logchan))
    await channel.send(embed = embed)

async def log_member_leave(member):
    embed = discord.Embed(title="Member Left")
    embed.add_field(name="Name", value=member)
    embed.set_footer(text=f'ID: {member.id}')
    channel = bot.get_channel(int(logchan))
    await channel.send(embed = embed)


# Run it 
bot.run(token)
