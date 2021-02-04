# library
import os
import random
import json

# networks
from urllib.request import Request, urlopen
from urllib.parse import quote

# APIs
from discord.ext import commands
from dotenv import load_dotenv

from expertai_test import compute_message_list_sentiment

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = "memebot's hideout"  # todo: place with .env for prod
bot = commands.Bot(command_prefix='!')

message_history = []


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


def fetch_templates():
    # todo: header???
    req = Request('https://api.memegen.link/templates', headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode()
    data = json.loads(webpage)
    return data


templates = fetch_templates()
two_line_templates = [x['key'] for x in templates if x['lines'] == 2]


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    global message_history
    message_history.append(message.content)

    if len(message_history) % 2 == 0:
        top_text: str = message_history[0]
        bottom_text: str = message_history[1]

        # todo: model will learn sentiment patterns (eg top line negative, bottom positive for twist)
        sentiment = compute_message_list_sentiment([ top_text, bottom_text ])
        sentiment_score = sentiment[0] + sentiment[1]
        # print(sentiment[0])
        # print(sentiment[1])
        # print(sentiment_score)

        top_text = quote(top_text)
        bottom_text = quote(bottom_text)

        meme_templates = two_line_templates  # neutral
        if sentiment_score > 10:
            meme_templates = ["ggg", "feelsgood", "icanhas"]  # happy
        elif sentiment_score < -10:
            meme_templates = ["sad-biden", "harold", "fr", "grumpycat", "sadfrog"]  # sad

        rand_int = random.randint(0, len(meme_templates) - 1)
        template = meme_templates[rand_int]
        res = f"https://api.memegen.link/images/{template}/{top_text}/{bottom_text}.png"

        meme_message = await message.channel.send(res)

        # emoji reaction
        emojis = ['\N{THUMBS UP SIGN}', '\N{THUMBS DOWN SIGN}']
        for emoji in emojis:
            await meme_message.add_reaction(emoji)

bot.run(TOKEN)
