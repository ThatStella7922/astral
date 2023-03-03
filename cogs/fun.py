import discord
import requests
from requests.exceptions import HTTPError
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="ping",description="i sure wonder how slow the bot is today!")
    async def ping(self, ctx): 
        await ctx.respond(f"latency was {round(self.bot.latency * 1000)}ms have a stellar day")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(fun(bot)) # add the cog to the bot