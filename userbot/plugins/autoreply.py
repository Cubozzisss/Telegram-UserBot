import asyncio
from telethon.sync import TelegramClient
from telethon import functions, types
from userbot.events import register

message = "**⛔️ Al momento sono OFFLINE non disturbare Ryze\n⚠️ Risponderò il prima possibile.\n\nNON spammatemi troppi messaggi e non rompere i coglioni**"
exempt = []
mutedList = []
autoNiceText = True
exempted = []
e = [] 

@register(outgoing=True, pattern="^[.]gmex ")
async def BroadCast(e):
  global exempted
  mex = e.text.split(" ", 1)[1]
  Uauzs = await e.client(functions.messages.GetAllChatsRequest([0]))
  chattezzs = []
  for i in Uauzs.chats:
    if not i.id in chattezzs:
      chattezzs.append(i.id)
  chats = []
  for i in chattezzs:
    if not str(i) in exempted:
      chats.append(i)
  await asyncio.wait([e.client.send_message(chat, mex) for chat in chats])
  await e.edit("Mex mandato in tutti i gruppi in cui sei presente!")

@register(outgoing=True, pattern="^.pula$")
async def CARABINIERIIIIIIIIIII(e):
  for i in range(10):
    await asyncio.wait([e.edit("🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵\n🔴🔴🔴🔴   🔵🔵🔵🔵")])
    await asyncio.sleep(0.1)
    await asyncio.wait([e.edit("🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴\n🔵🔵🔵🔵   🔴🔴🔴🔴")])
    await asyncio.sleep(0.1)
  await asyncio.wait([e.edit("**💦💦💦Arriva assunta la troia sborrata💦💦💦**")])

@register(outgoing=True, pattern="^.pp$")
async def dev(e):
  await asyncio.wait([e.edit("** https://www.paypal.me/vogliadisoldi puoi pagare pure da qua grazie 👈🏻 ) **")])

@register(outgoing=True, pattern="^.rep$")
async def dev(e):
  await asyncio.wait([e.edit("** @UshyRep ecco il mio gruppo vendite  **")])

@register(outgoing=True, pattern="^.btc$")
async def dev(e):
  await asyncio.wait([e.edit("** non ho un addi fisso :( **")])

@register(outgoing=True)
async def niceText(e):
  if e.text[0].isalpha() and not e.text == "Canali":
    global autoNiceText
    if autoNiceText:
      mex = ""
      for i in range(len(e.text)):
        if e.text[i] == " ":
          mex = mex + ' '
        else:
          mex = mex + e.text[i]
        await asyncio.wait([e.edit("`" + mex + " |`")])
        await asyncio.sleep(0.1)
        await asyncio.wait([e.edit("`" + mex + "  ‏‏‎ `")])
        await asyncio.sleep(0.1)
        if i == len(e.text) - 1:
          await asyncio.wait([e.edit("`" + e.text + "`")])

@register(outgoing=True, pattern="^.niceText$")
async def setNiceText(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global autoNiceText
    if autoNiceText:
      autoNiceText = False
      await e.edit("`Animazione Testo Disattivata!`")
    else:
      autoNiceText = True
      await e.edit("`Animazione Testo Attivata!`")

@register(outgoing=True, pattern="^.mex")
async def setMessage(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    global message
    message = str(e.text[5:])
    await e.edit("`Messaggio impostato correttamente!`")

@register(outgoing=True, pattern="^.mute$")
async def setMute(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    if e.is_private and not (await e.get_sender()).bot:
      global mutedList
      if e.chat_id in mutedList:
        mutedList.remove(e.chat_id)
        await e.edit("`Utente Smutato!`")
      else:
        mutedList.append(e.chat_id)
        await e.edit("`Utente Mutato!`")

@register(incoming=True)
async def autoReply(e):
  if e.is_private and not (await e.get_sender()).bot:
    global mutedList
    if e.chat_id in mutedList:
      await e.delete()
    else:
      if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
        global exempt
        if not e.sender.id in exempt:
          exempt.append(e.sender.id)
          x = 0
          while True:
            if type((await e.client.get_me()).status).__name__ ==  "UserStatusOffline":
              await asyncio.sleep(1)
              x += 1
              if x >= 3:
                global message
                await e.respond(message)
                result = client(functions.account.UpdateProfileRequest(
                    last_name='- OFFLINE',
                ))
                exempt.remove(e.sender.id)
                break
            else:
              exempt.remove(e.sender.id)
              break
