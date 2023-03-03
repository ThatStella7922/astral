import discord
import requests
import dotenv
import os
from requests.exceptions import HTTPError
from discord.ext import commands

#load token from disk
dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

#basic info
botVersion = "1.0"
botVersionDate = "March 2 2023"
botName = "astral"

bot = commands.Bot()

#load cogs
cogs_list = ['osuUtils', 'fun']
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

@bot.event
async def on_ready():
    print(f"{bot.user} started succesfully")

#base command - about
@bot.slash_command(name="about",description=f"Prints information about {botName}", guild_ids=[502661867919900673])
async def about(ctx): 
    await ctx.respond(f"{botName} {botVersion} ({botVersionDate})\nhello yes this is astral")

bot.run(token)
