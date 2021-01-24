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

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)