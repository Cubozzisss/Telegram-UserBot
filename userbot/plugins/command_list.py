from telethon import events
import subprocess
import asyncio
import time


@command(pattern="^.cmds", outgoing=True)
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls userbot/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**ℹ️ LISTA PLUG-IN 🔍:**\n{o}\n\n**ℹ️ SUGGERIMENTO:** __Per vedere i comandi di un plug-in, fai:-__ \n `.help <plugin name>` **senza le parentesi < > .**\n__Tutti i plug-in potrebbero non funzionare. Visita__ ~ @AnonHexoUserBot ~ __per assistenza.__"
    await event.edit(OUTPUT)
