import discord
import requests
import dotenv
import os
from requests.exceptions import HTTPError
from discord.ext import commands

#load token from disk
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = commands.Bot()

#load cogs
cogs_list = ['osuUtils', 'fun']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"{bot.user} started succesfully")

bot.run(token)
