import sqlite3
import discord
import requests
import pymongo
from requests.exceptions import HTTPError
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord import Option

# console markers
success = '[√]'
error = '[x]'

# Initialize the DEETABASE
myclient = pymongo.MongoClient("mongodb://192.168.69.3:27017/")
mydb = myclient["astral"]
cartelMetadata = mydb["cartelmetadata"]
cartelMembers = mydb["cartelmembers"]
print(f"{success} Database init: probably")

class cartelUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    cartelUtilsGroup = SlashCommandGroup("cartel", "Utilities for the Fruitycord cartel, part of ThatStella7922's server")
    ownerUtilsGroup = cartelUtilsGroup.create_subgroup("owner", "Cartel owner utilities")
    voteGroup = cartelUtilsGroup.create_subgroup("vote", "Cartel voting")
    channelManagementGroup = cartelUtilsGroup.create_subgroup("channel", "Cartel channel management")

    ## Main Cartel Utils Commands
    @cartelUtilsGroup.command(name="info",description="Info about the cartel")
    async def set(self, ctx): 
        await ctx.respond(f"this is supposed to pull from the db but im lazy")

    @cartelUtilsGroup.command(name="setname",description="Set the name of the cartel")
    async def setname(self, ctx): 
        await ctx.respond(f"success message or something idek")
    ## End group

    ## Owner Utils Commands
    @ownerUtilsGroup.command(name="set",description="Set a new cartel owner immediately")
    async def set(
        self,
        ctx,
        member: Option(float, "The user that will be set as cartel owner")
    ):
        #cartelMetaTable.upsert(dict(ownerID=281503786986635265)) 
        await ctx.respond(f"idk")

    @ownerUtilsGroup.command(name="show",description="Shows the current owner of the cartel")
    async def show(self, ctx): 
        await ctx.respond(f"Owner is ")
    ## End group

def setup(bot):
    bot.add_cog(cartelUtils(bot))