
from telethon import events

import asyncio

from userbot.utils import admin_cmd
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@borg.on(admin_cmd(pattern=r"police"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 12)

    await event.edit("Police")

    animation_chars = [
        
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",    
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            "🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴\n🔵🔵🔵🔴🔴🔴",
            "🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵\n🔴🔴🔴🔵🔵🔵",
            f"{DEFAULTUSER} **Ecco la Polizia**"

 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 12])
