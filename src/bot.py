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
import json
from urllib.request import Request, urlopen
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "memebot's hideout"  # todo: place with .env for prod
bot = commands.Bot(command_prefix='!')

# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     guild = discord.utils.get(client.guilds, name=GUILD)
#
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

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


@bot.event
async def on_ready():
    print(f'BOT {bot.user.name} has connected to Discord!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='meme', help='Generates shitty meme')
async def meme(ctx, top_text: str, bottom_text: str=''):
    if not bottom_text:
        res = f"https://api.memegen.link/images/buzz/memes/{top_text}.png"
    else:
        res = f"https://api.memegen.link/images/buzz/{top_text}/{bottom_text}.png"
    await ctx.send(res)

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

def fetchTemplates():
    req = Request('https://api.memegen.link/templates', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode()
    data = json.loads(webpage)
    return data

templates = fetchTemplates()

@bot.command(name='test')
async def test(ctx):
    this_channel = ctx.channel.id
    channel = bot.get_channel(int(this_channel))

    messages = await channel.history(limit=3).flatten()
    messages = list(filter(lambda x: not x.author.bot, messages))
    messages.reverse()
    # for message in messages:
    #     print(message.author)
    #     print(message.author.bot)
    #     print(message.content)

    top_text: str = messages[0].content.replace(' ', '_')
    bottom_text: str = messages[1].content.replace(' ', '_') if len(messages) > 1 else ""
    # print(top_text)
    # print(bottom_text)
    # print(templates)

    if not bottom_text:
        filtered_templates = list(filter(lambda x: not x["lines"] == 1, templates))
        rand_int = random.randint(0, len(filtered_templates) - 1)
        template = filtered_templates[rand_int]["key"]
        res = f"https://api.memegen.link/images/{template}/memes/{top_text}.png"
    else:
        filtered_templates = list(filter(lambda x: not x["lines"] == 1, templates))
        rand_int = random.randint(0, len(filtered_templates) - 1)
        template = filtered_templates[rand_int]["key"]
        res = f"https://api.memegen.link/images/{template}/{top_text}/{bottom_text}.png"
    # print(res)
    await ctx.send(res)

    # response = []
    # for message in messages:
    #     response.append(message.content)
    # response = "\n".join(response)
    # await ctx.send(response)

bot.run(TOKEN)
