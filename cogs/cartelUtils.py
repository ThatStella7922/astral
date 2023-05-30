import discord
import requests
import dataset
import sys
from requests.exceptions import HTTPError
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord import Option

# console markers
success = '[√]'
error = '[x]'

# Initialize the DEETABASE
try:
    mydb = dataset.connect('sqlite:///db/astral.db')
except Exception as e:
    print(f"{error} Database connection: failed with {e}")
    sys.exit(1)
cartelMetadatatable = mydb["cartelmetadata"]
cartelMemberstable = mydb["cartelmembers"]
print(f"{success} Database connection: probably worked fine")

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
        member: Option(discord.Member, "The user that will be set as cartel owner")
    ):
        ownerMemberId = member.id
        ownerFriendlyName = member.name + "#" + member.discriminator
        setOwnerStager = dict(id="1", cartelOwnerFriendlyName=f"{ownerFriendlyName}", cartelOwnerId=ownerMemberId)
        try:
            cartelMetadatatable.upsert(setOwnerStager, ['id'])
        except Exception as e:
            print(e)
            await ctx.respond(f"Setting the cartel owner failed with the following error:\n{e}")
            return
        await ctx.respond(f"New cartel owner was succesfully set to <@{ownerMemberId}>! (user ID {ownerMemberId})")
            

    @ownerUtilsGroup.command(name="show",description="Shows the current owner of the cartel")
    async def show(self, ctx): 
        try:
            cartelOwnerObject = cartelMetadatatable.find_one(id='1') # returns an OD
            ownerFriendlyName = cartelOwnerObject["cartelOwnerFriendlyName"]
            ownerMemberID = cartelOwnerObject["cartelOwnerId"]
        except Exception as e:
            print(e)
            await ctx.respond(f"Getting the current cartel owner failed with the following error:\n{e}")
            return
        await ctx.respond(f"The current cartel owner is <@{ownerMemberID}> ({ownerFriendlyName})")
    ## End group

def setup(bot):
    bot.add_cog(cartelUtils(bot))