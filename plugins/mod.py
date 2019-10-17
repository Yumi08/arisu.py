import discord
client = discord.Client()
server = discord.Guild
member = discord.Member

# Kick
async def kick(message):
    if (len(message.mentions) > 0):
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                target = server.get_member(user.id)
                await server.kick(target)
                await message.channel.send('**{}** has been kicked'.format(target))
# Ban
async def ban(message):
    if (len(message.mentions) > 0):
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                target = server.get_member(user.id)
                await server.ban(target)
                await message.channel.send('**{}** has been banned'.format(target))

# Mute
async def mute(message):
    if (len(message.mentions) > 0):
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                target = server.get_member(user.id)
                role = discord.utils.get(server.roles, name="silenced")
                await member.add_roles(target, role)

async def unmute(message):
    if (len(message.mentions) > 0):
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                target = server.get_member(user.id)
                role = discord.utils.get(server.roles, name="silenced")
                await member.remove_roles(target, role)

