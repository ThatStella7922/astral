import discord
import requests
import os
import cpuinfo
from http import HTTPStatus
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord import Option


class lookupUtils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    lookupUtilsGroup = SlashCommandGroup("lookup", "Helpful time-saving lookups")

    @lookupUtilsGroup.command(name="http",description="Prints what an HTTP status code is")
    async def http(
        self,
        ctx,
        httpcode: Option(int, "Specify an HTTP code (eg. 200)")
    ): 
        try:
            await ctx.respond(f"HTTP status code {httpcode}: {HTTPStatus(httpcode).phrase} ({HTTPStatus(httpcode).description})")
        except ValueError:
            await ctx.respond(f"HTTP status code `{httpcode}` doesn't correspond to any standard HTTP response. It may be a non-standard response.")
            return
        
    @lookupUtilsGroup.command(name="httpcat",description="Shows your HTTP status code but as a cat!")
    async def httpcat(
        self,
        ctx,
        httpcode: Option(int, "Specify an HTTP code (eg. 200)")
    ): 
        try:
            await ctx.respond(f"CAT!!1!11!! HTTP status code {httpcode}: {HTTPStatus(httpcode).phrase} ({HTTPStatus(httpcode).description})")
            await ctx.send(f"https://http.cat/{httpcode}")
        except ValueError:
            await ctx.respond(f"HTTP status code `{httpcode}` doesn't correspond to any standard HTTP response. It may be a non-standard response.")
            return

def setup(bot):
    bot.add_cog(lookupUtils(bot))   