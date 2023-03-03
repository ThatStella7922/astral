import discord
import requests
from requests.exceptions import HTTPError
from discord.commands import SlashCommandGroup
from discord.ext import commands

class osuUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    osuUtilsGroup = SlashCommandGroup("osu", "Utilities related to osu!")

    @osuUtilsGroup.command(name="getlatest",description="Gets info about the latest version of osu!lazer")
    async def getlatest(self, ctx): 
        try:
            apiReq = requests.get('https://api.github.com/repos/ppy/osu/releases/latest')
            jsonResponse = apiReq.json()
            osuVersion = jsonResponse["tag_name"]
            await ctx.respond("The latest version of osu!lazer is " + osuVersion + ", you can download it at <" + jsonResponse["html_url"] + ">." + "\nChangelog: <https://osu.ppy.sh/home/changelog/lazer/" + osuVersion + ">")
        except HTTPError as http_err:
            await ctx.respond(f"http error: {http_err}")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(osuUtils(bot)) # add the cog to the bot