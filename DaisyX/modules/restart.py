from telethon import events
import os, re, sys, asyncio
from DaisyX.utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd(pattern="restart"))
async def _(event):
    await bot.send_message(event.chat.id, '`Wait restarting`')
    await event.delete() 
    asyncio.sleep(0.5)
    await event.edit('`Restarted successfully`')
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
    
