### Formation
Now I will show a short script to show the formation of the desired script.
```python3
@command(pattern="^.alive", outgoing=True)
async def hello_world(event):
    if event.fwd_from:
        return
    await event.edit("**HELLO WORLD**\n\nThe following is controlling me too!\n" + Var.SUDO_USERS)
```

## CREDITS TO:

***Official Bot Dveloper: [anubis](https://github.com/Dark-Princ3/)***
***Official Bot Developer: [SnapDragon7410](https://github.com/SnapDragon7410)***
