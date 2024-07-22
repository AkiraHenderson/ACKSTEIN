import discord
from discord.ext import commands
from datetime import datetime
import pytz

class WelcomeMessage(commands.Cog):
  def __init__(self, bot):
      self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    # 환영 메시지 전송 (원하는 채널 ID로 변경)
    welcome_channel_id = 1262710410369568800
    welcome_channel = member.guild.get_channel(welcome_channel_id)
    if welcome_channel:
        await welcome_channel.send(f"환영합니다, {member.mention}! 서버에 오신 것을 환영합니다!")

async def setup(bot):
  await bot.add_cog(WelcomeMessage(bot))