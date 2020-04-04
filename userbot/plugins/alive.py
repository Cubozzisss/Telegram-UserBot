"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "senza nome"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`∇ STATUS USERBOT ∇`**\n\n"
                     "`Versione Telethon: 7.0.1\nVersione Python: 3.8.0\nRAMO:` @IOIIOIIIOIIOI\n"
                     "`CREATORE BOT:` [SnapDragon7410](tg://user?id=719877937)\n"
                     "`STATUS DATABASE: In esecuzione...\n\nIl mio master\n`"
                     f"`PROPIETARIO`: {DEFAULTUSER}\n"
                     "[DISTRIBUISCI QUESTO USERBOT](https://github.com/IIOOIIOIIOOII/USERBOT-ITA.git)")