from telethon import events
import os, re, sys, asyncio
from DaisyX.utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd(pattern="restart"))
@bot.on(sudo_cmd(pattern="restart ?(.*)", allow_sudo=True))
async def _(event):
    k = await bot.send_message(event.chat.id, '`Wait restarting`') 
    asyncio.sleep(0.5)
    await k.edit('`Restarted successfully`')
    await event.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
    
