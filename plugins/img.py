 # In dire need of optimization
import discord
import requests
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


async def pape(message):
    footer_url = 'https://pbs.twimg.com/profile_images/653341480640217088/t1c1aTc9.png'
    url = 'https://wallhaven.cc/api/v1/search'
    params = {'sorting': 'random'}

    # In case a query exists (a!pape query).
    if len(message.content.split()) >= 2:
        query = ' '.join(message.content.split()[1:])
        params['q'] = query

    response = requests.get(url, params)

    if len(response.json()['data']) > 0:
        wallpaper_url = response.json()['data'][0]['url']
        embed = discord.Embed(title='Wallpaper',
                              description='[Source] ' + wallpaper_url,
                              colour=0xbe132d)
        embed = (embed.set_footer(text='This command is powered by wallhaven.cc',
                                  icon_url=footer_url)
                      .set_image(url=wallpaper_url))

        await message.channel.send(embed=embed)

    else:
        await message.channel.send('No results found')

