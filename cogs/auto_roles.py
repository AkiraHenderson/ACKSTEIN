import discord
from discord.ext import commands
from datetime import datetime
import pytz

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # 역할 추가
        roles_to_assign = [
            1263396237600620616,  # 역할 ID들로 교체
            1259167116414812170
        ]
        for role_id in roles_to_assign:
            role = member.guild.get_role(role_id)
            if role:
                try:
                    await member.add_roles(role)
                    print(f'Added role {role.name} to member {member}')
                except discord.Forbidden:
                    print(f'Failed to add role {role.name} to member {member} (permission error)')
                except discord.HTTPException as e:
                    print(f'Failed to add role {role.name} to member {member} (API error: {e})')

async def setup(bot):
    await bot.add_cog(AutoRole(bot))