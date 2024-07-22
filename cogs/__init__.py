from .bot_status import setup as setup_bot_status
from .auto_roles import setup as setup_auto_roles
from .comment_reaction import setup as setup_comment_reaction
from .embed_commands import setup as setup_embed_commands
from .mod_log import setup as setup_mod_log
from .welcome_message import setup as setup_welcome_message

async def setup_cogs(bot):
    await setup_bot_status(bot)
    await setup_auto_roles(bot)
    await setup_comment_reaction(bot)
    await setup_embed_commands(bot)
    await setup_mod_log(bot)
    await setup_welcome_message(bot)