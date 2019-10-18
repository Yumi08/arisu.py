 # In dire need of optimization
from . import util

# Avatar command
async def avatar_command(message):
        if len(message.mentions) > 0:
            for user in message.mentions:
                print(user.avatar_url)
                embed = util.create_avatar_embed(message, user)
                await message.channel.send(embed=embed)

        # If the message contains users but doesn't metion them.
        elif len(message.content.split()) == 2:
            # Getting the users and removing nicknames that didn't match (None).
            nicknames = message.content.split()[1:]
            users = [util.find_member(message, nickname) for nickname in nicknames]
            users = [user for user in users if user is not None]

            for user in users:
                print(user.avatar_url)
                embed = util.create_avatar_embed(message, user)
                await message.channel.send(embed=embed)

        else:
                embed = util.create_avatar_embed(message, message.author)
                await message.channel.send(embed=embed)

