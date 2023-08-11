import discord
import requests
import dotenv
import sqlite3
import os
from requests.exceptions import HTTPError
from discord.ext import commands

print(f"astral")

# console markers
success = '[√]'
error = '[x]'

#load token and owner from disk
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
ownerid = str(os.getenv("OWNERID"))

# bot setup
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

#load cogs
cogs_list = ['osuUtils', 'fun', 'lookupUtils']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"{success} Bot sucessfully initialized as {bot.user}")

bot.run(token)
