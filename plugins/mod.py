import discord


async def kick(message):
    if len(message.mentions) > 0:
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                await server.kick(user)
                await message.channel.send(f'**{user}** has been kicked)')


async def ban(message):
    if len(message.mentions) > 0:
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                await server.ban(user)
                await message.channel.send(f'**{user}** has been banned')


async def mute(message):
    if len(message.mentions) > 0:
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                role = discord.utils.get(server.roles, name="silenced")
                await user.add_roles(role)


async def unmute(message):
    if len(message.mentions) > 0:
        for user in message.mentions:
            if message.author.guild_permissions.administrator:
                server = user.guild
                role = discord.utils.get(server.roles, name="silenced")
                await user.remove_roles(role)

