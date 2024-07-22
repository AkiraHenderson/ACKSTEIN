import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
access_token = os.environ["BOT_TOKEN"]

async def main():
    async with bot:
        await setup_cogs()
        await bot.start(access_token)

async def setup_cogs():
    from cogs import setup_cogs
    await setup_cogs(bot)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

if __name__ == "__main__":
    asyncio.run(main())
