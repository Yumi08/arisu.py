import discord
import os
client = discord.Client()

# Welcome 
async def mem_join(member):
     guild = member.guild 
     if guild.system_channel is not None:
        msg = 'Welcome {0.mention}!'.format(member) 
        await guild.system_channel.send(msg)

async def mem_leave(member):
     guild = member.guild 
     if guild.system_channel is not None:
        msg = 'Bye **{0.name}**!'.format(member) 
        await guild.system_channel.send(msg)