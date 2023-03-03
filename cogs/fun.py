import discord
import requests
import dotenv
import os
from requests.exceptions import HTTPError
from discord.ext import commands

#load basic bot info from disk
dotenv.load_dotenv()
botVersion = str(os.getenv("botVersion"))
botVersionDate = str(os.getenv("botVersionDate"))
botName = str(os.getenv("botName"))

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping",description="i sure wonder how slow the bot is today!")
    async def ping(self, ctx): 
        await ctx.respond(f"latency was {round(self.bot.latency * 1000)}ms have a stellar day")

    @discord.slash_command(name="about",description=f"Prints information about {botName}")
    async def about(self, ctx): 
        await ctx.respond(f"*{botName}*\n{botVersion} ({botVersionDate})")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(fun(bot)) # add the cog to the bot