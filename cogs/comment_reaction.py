import discord
from discord.ext import commands

class CommentReaction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        await self.bot.process_commands(message)  # Ensure commands are processed

        if message.content == "챗봇 바보":
            await message.channel.send("...뭐이?")
            return

async def setup(bot):
    await bot.add_cog(CommentReaction(bot))
