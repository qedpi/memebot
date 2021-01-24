# # core
# import discord
# from discord.ext import commands
# from discord.ext.commands import bot
#
# # project imports
# from constants import MEDIA_PATH, COMMAND_PREFIX, HR
#
# # library
#
# @bot.event
# async def on_ready():
#     print(f"Logged in as {bot.user} "
#           f"with access to: \n {' & '.join(str(g) for g in bot.guilds)}{HR}")

import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "memebot's hideout"  # todo: place with .env for prod
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    print(message.author)


    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

client.run(TOKEN)
