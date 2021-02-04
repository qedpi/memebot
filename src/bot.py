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
from expertai_test import compute_message_list_sentiment

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "memebot's hideout"  # todo: place with .env for prod
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'BOT {bot.user.name} has connected to Discord!')

@bot.command(name='meme', help='Generates shitty meme')
async def meme(ctx, top_text: str, bottom_text: str=''):
    if not bottom_text:
        res = f"https://api.memegen.link/images/buzz/memes/{top_text}.png"
    else:
        res = f"https://api.memegen.link/images/buzz/{top_text}/{bottom_text}.png"
    await ctx.send(res)



def fetchTemplates():
    req = Request('https://api.memegen.link/templates', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode()
    data = json.loads(webpage)
    return data

templates = fetchTemplates()
two_line_templates = list(filter(lambda x: not x["lines"] == 2, templates))
two_line_templates = list(map(lambda x: x["key"], two_line_templates))

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
        filtered_templates = list(filter(lambda x: not x["lines"] == 2, templates))
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

message_history = []
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    global message_history
    message_history.append(message.content)
    if len(message_history) == 2:
        top_text: str = message_history[0]
        bottom_text: str = message_history[1]

        sentiment = compute_message_list_sentiment([ top_text, bottom_text ])
        sentiment_score = sentiment[0] + sentiment[1]
        # print(sentiment[0])
        # print(sentiment[1])
        # print(sentiment_score)

        top_text = top_text.replace(' ', '_')
        bottom_text = bottom_text.replace(' ', '_')

        meme_templates = two_line_templates # neutral
        if sentiment_score > 10:
            meme_templates = ["ggg", "feelsgood", "icanhas"] # happy
        elif sentiment_score < -10:
            meme_templates = ["sad-biden", "harold", "fr", "grumpycat", "sadfrog"] # sad

        rand_int = random.randint(0, len(meme_templates) - 1)
        template = meme_templates[rand_int]
        res = f"https://api.memegen.link/images/{template}/{top_text}/{bottom_text}.png"

        message_history = []
        meme_message = await message.channel.send(res)

        # emoji reaction
        emojis = ['\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']
        for emoji in emojis:
            await meme_message.add_reaction(emoji)

bot.run(TOKEN)
