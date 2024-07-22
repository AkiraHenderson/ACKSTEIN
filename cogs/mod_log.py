import discord
from discord.ext import commands
from datetime import datetime
import pytz

class ModLog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author.bot:
            return

        log_channel = message.guild.get_channel(1262710697037533235)  # 로그 채널 ID로 변경
        if log_channel:
            embed = discord.Embed(
                title="메시지 삭제 기록",
                description=f"**사용자:** {message.author.name}\n**채널:** {message.channel.name}",
                timestamp=datetime.now(pytz.timezone('UTC')),
                color=0xff0000
            )
            embed.set_author(name=message.author.display_name, icon_url=message.author.avatar.url if message.author.avatar else message.author.default_avatar.url)
            embed.add_field(name="삭제된 메시지", value=message.content, inline=False)
            embed.set_footer(text=f"User ID: {message.author.id} | Message ID: {message.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        log_channel = member.guild.get_channel(1263467806687625326)  # 로그 채널 ID로 변경
        if log_channel:
            embed = discord.Embed(
                title="유저 탈퇴 기록",
                description=f"**사용자:** {member.name}",
                timestamp=datetime.now(pytz.timezone('UTC')),
                color=0xff0000
            )
            embed.set_footer(text=f"User ID: {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        log_channel = guild.get_channel(1262715566632734750)  # 로그 채널 ID로 변경
        if log_channel:
            embed = discord.Embed(
                title="유저 밴 기록",
                description=f"**사용자:** {user.name}",
                timestamp=datetime.now(pytz.timezone('UTC')),
                color=0xff0000
            )
            embed.set_footer(text=f"User ID: {user.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_kick(self, member):
        log_channel = member.guild.get_channel(1263470175315951627)  # 로그 채널 ID로 변경
        if log_channel:
            embed = discord.Embed(
                title="유저 킥 기록",
                description=f"**사용자:** {member.name}",
                timestamp=datetime.now(pytz.timezone('UTC')),
                color=0xff0000
            )
            embed.set_footer(text=f"User ID: {member.id}")
            await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # 로그 채널에 가입 기록 남기기 (원하는 채널 ID로 변경)
        log_channel_id = 1263467586511835159
        log_channel = member.guild.get_channel(log_channel_id)
        if log_channel:
            embed = discord.Embed(
                title="유저 가입 기록",
                description=f"**사용자:** {member.name}#{member.discriminator}",
                timestamp=datetime.now(pytz.timezone('UTC')),
                color=0x00ff00
            )
            embed.set_author(name=member.display_name, icon_url=member.avatar.url if member.avatar else member.default_avatar.url)
            embed.set_footer(text=f"User ID: {member.id}")
            await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(ModLog(bot))
