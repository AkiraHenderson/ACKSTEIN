import discord
from discord.ext import commands

class BotStatus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}!')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("기능하고있어용"))

async def setup(bot):
    await bot.add_cog(BotStatus(bot))
