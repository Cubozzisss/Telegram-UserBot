"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio







@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "avast":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nRicerca: 01 of 01 Files Scansione...\n\nSTATUS: Nessun Virus Rilevato...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "avast1":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Avast Security Checkup\n\n\nAccount: User Pro\nScadenza: 31/12/2099\n\nRicerca: 01 of 01 Scansione...\n\nSTATUS:⚠️Virus Rilevato⚠️\nINFO: Torzan, Spyware, Adware`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
