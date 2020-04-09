"""No Logic Pligon for @PepeBot
\nCoding by Legend @NeoMatrix90
\nType .logic to see many logical fact
"""
from telethon import events
import asyncio
import random

from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=f"logic", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.logic", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Attendi 2sec sto pensando 🤔...`")
    await asyncio.sleep(2)
    x=(random.randrange(1,7))
    if x==1:
        await event.edit("`La logica è una cosa e il buon senso un’altra.`")
    if x==2:
        await event.edit("`Ama la vita più della sua logica.`")
    if x==3:
        await event.edit("`La logica vi porterà da A a B. L’immaginazione vi porterà dappertutto.`")
    if x==4:
        await event.edit("`Le relazioni tra uomini e donne non si possono spiegare mediante la logica.`")
    if x==5:
        await event.edit("`Nella realtà non avviene nulla che corrisponda rigorosamente alla logica.`")
    if x==6:
        await event.edit("`Una mente tutta logica è come un coltello tutto lama. Fa sanguinare la mano che lo usa.`")
    if x==7:
        await event.edit("`Ciò che sfugge alla logica è quanto v’è di più prezioso in noi stessi.`")
