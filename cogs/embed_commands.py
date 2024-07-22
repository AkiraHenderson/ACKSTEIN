import discord
from discord.ext import commands
from datetime import datetime
import pytz

class EmbedCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
            if message.content.startswith("!embed"):
                parts = message.content.split(" ", 3)
                if len(parts) != 4:
                    await message.channel.send("명령어 형식: !embed 제목 설명 색상(HTML 코드)")
                    return

                title = parts[1].strip("{}")
                description = parts[2].strip("{}")
                color_hex = parts[3]

                if color_hex.startswith("#") and len(color_hex) == 7:
                    try:
                        color = int(color_hex[1:], 16)
                    except ValueError:
                        await message.channel.send("유효한 HTML 색상 코드를 입력해주세요. 예: #FF5733")
                        return
                else:
                    await message.channel.send("유효한 HTML 색상 코드를 입력해주세요. 예: #FF5733")
                    return

                embed = discord.Embed(title=title, description=description, color=color)
                await message.channel.send(embed=embed)

            if message.content == "/임베드":
                embed = discord.Embed(
                    title="제목",
                    description="부제목",
                    timestamp=datetime.now(pytz.timezone('UTC')),
                    color=0x00ff00
                )
                embed.add_field(name="임베드 라인 1 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
                embed.add_field(name="임베드 라인 2 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
                embed.add_field(name="임베드 라인 3 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
                embed.add_field(name="임베드 라인 4 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
                embed.set_footer(text="Bot Made by.???", icon_url="https://example.com/icon.png")
                embed.set_thumbnail(url="https://example.com/thumbnail.png")
                await message.channel.send(embed=embed)

            if message.content == "/규칙실행" and message.channel.id == 1257218964728053763:  # 채널 ID를 실제 채널의 ID로 교체해야 합니다
                embed = discord.Embed(
                    title="제목",
                    description="부제목",
                    timestamp=datetime.now(pytz.timezone('UTC')),
                    color=0x00ff00
                )
                embed.add_field(name="임베드 라인 1 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
                embed.add_field(name="임베드 라인 2 - inline = false로 책정", value="라인 이름에 해당하는 값", inline=False)
                embed.add_field(name="임베드 라인 3 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
                embed.add_field(name="임베드 라인 4 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
                embed.set_footer(text="Bot Made by. Henderson / ChatGPT")
                embed.set_thumbnail(url="https://example.com/thumbnail.png")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1257218964728053763/1263387960661901403/AS_-_.png?ex=669a0d3a&is=6698bbba&hm=2a168412d308dd6064c78453e245de1b6b8f0807b467e1b38916e43353b998fe&")  # 크게 로딩할 이미지 URL 설정
                await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(EmbedCommands(bot))

