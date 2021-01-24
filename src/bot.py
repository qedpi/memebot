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
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "memebot's hideout"  # todo: place with .env for prod
bot = commands.Bot(command_prefix='!')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# @client.event
# async def on_message(message):
#     # if message.author == client.user:
#     #     return
#     print(message.author)
#
#
#     brooklyn_99_quotes = [
#         'I\'m the human form of the 💯 emoji.',
#         'Bingpot!',
#         (
#             'Cool. Cool cool cool cool cool cool cool, '
#             'no doubt no doubt no doubt no doubt.'
#         ),
#     ]
#
#     if message.content == '99!':
#         response = random.choice(brooklyn_99_quotes)
#         await message.channel.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice, number_of_sides):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

client.run(TOKEN)
