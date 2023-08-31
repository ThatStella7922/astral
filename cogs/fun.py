import discord
import requests
import dotenv
import os
import cpuinfo
import secrets
from uwuipy import uwuipy
from requests.exceptions import HTTPError
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord import Option

#load basic bot info from disk
dotenv.load_dotenv()
botVersion = "1.0.4"
botVersionDate = "Aug 30 2023"
botName = str(os.getenv("botName"))

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    funGroup = SlashCommandGroup("fun", "Various little commands of dubious utility")
    
    # astral will not! be getting a sex update

    @funGroup.command(name="kiss",description="Kiss someone (girlkissing preferred, but not required)")
    async def kiss(
        self, 
        ctx,
        member: Option(discord.Member, "Who are you going to kiss?", required=True),
        allowfruity: Option(str, description="Allow fruity responses? recipient should be comfortable being pinned against a wall if enabled..", choices=["Yes and force a fruity response", "Yes", "No"], required=False)
    ):  
        # no kissing my Eva
        if member.id == 626397784169381888 and ctx.author.id != 281503786986635265:
            await ctx.respond("Don't kiss <@281503786986635265>'s wife!!")
            return

        # special cases!
        match ctx.author.id:
            # no Eva
            case 626397784169381888:
                await ctx.respond("shut up eva i'm going to have you up against a wall soon enough just Wait")
                await ctx.send(":3")
                return
            
            # special case for loppa
            case 502595728896688128:
                await ctx.respond("you will never find love, loppa")
                return
            
        # no kissing yourself
        if ctx.author == member:
            await ctx.respond(f"{ctx.author.mention}, you can't kiss yourself!")
            return
        
        allCasesResponses = [
            f"*{ctx.author.display_name}*, you kiss *{member.display_name}*."
        ]

        fruityResponses = [
            f"*{ctx.author.display_name}*, you take *{member.display_name}* into your arms for a passionate kiss.",
            f"*{ctx.author.display_name}*, you lock eyes with *{member.display_name}*, then lean in for a kiss.",
            f"*{ctx.author.display_name}*, you pin *{member.display_name}*'s shoulders onto the wall next to you and come in for a kiss."
            ]
        
        if allowfruity == "Yes":
            kissMsg = secrets.choice([secrets.choice(fruityResponses), secrets.choice(allCasesResponses)])
        elif allowfruity == "Yes and force a fruity response":
            kissMsg = secrets.choice(fruityResponses)
        else:
            kissMsg = secrets.choice(allCasesResponses)
        
        await ctx.respond(kissMsg)

    @funGroup.command(name="uwuify",description="Uwuify text (example: The quick b-b-b-bwown (・\`ω\´・) ***screeches*** fox)")
    async def uwuify(
        self, 
        ctx,
        uwuifytext: Option(str, "Text to uwuify", required=True),
        seed: Option(int, "Uwuification seed (use an integer)", required=False),
        stutterchance: Option(float, "Word stutter probability (0-100)", min_value=0, max_value=100, default=10.0, required=False),
        facechance: Option(float, "Probability of a face like: (ᵕᴗ ᵕ⁎) (0-100)", min_value=0, max_value=100, default=5.0, required=False),
        actionchance: Option(float, "Probability of an action like: *screeches* (0-100)", min_value=0, max_value=100, default=7.5, required=False),
        exclamationchance: Option(float, "Exclamation probability (0-100)", min_value=0, max_value=100, default=100, required=False),
        nsfw_actions: Option(bool, "Allow NSFW actions? (like *notices buldge*)", default=False, required=False)
    ):
        # Parameter details above taken from https://github.com/Cuprum77/uwuipy/blob/main/README.md

        args = [stutterchance, facechance, actionchance, exclamationchance]
        argsDivided = []
        for x in args:
            argsDivided.append(x / 100)

        uwu = uwuipy(seed, argsDivided[0], argsDivided[1], argsDivided[2], argsDivided[3], nsfw_actions)
        await ctx.respond(uwu.uwuify(uwuifytext))

    @funGroup.command(name="ping",description="i sure wonder how slow the bot is today!")
    async def ping(self, ctx): 
        responses = [
            f"Latency was {round(self.bot.latency * 1000)}ms, have a stellar day",
            f"Latency was {round(self.bot.latency * 1000)}ms, have a fruity day",
            f"Latency was {round(self.bot.latency * 1000)}ms :3"
        ]

        await ctx.respond(secrets.choice(responses))

    @funGroup.command(name="about",description=f"Prints information about {botName}")
    async def about(self, ctx): 
        await ctx.defer()
        cpuinfoVar = cpuinfo.get_cpu_info()
        await ctx.respond(f"*{botName}* {botVersion} ({botVersionDate})\nHost CPU: {cpuinfoVar['brand_raw']} ({cpuinfoVar['arch_string_raw']}, {cpuinfoVar['count']} logical processors)\nHost Python: {cpuinfoVar['python_version']}\n\nSource code: <https://github.com/ThatStella7922/astral>")

def setup(bot):
    bot.add_cog(fun(bot))