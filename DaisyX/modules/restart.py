# (c) Copyright 2021-2022 DaisyX

from telethon import events
import os, re, sys, asyncio
from DaisyX.utils import admin_cmd, sudo_cmd

@bot.on(admin_cmd(pattern="restart"))
@bot.on(sudo_cmd(pattern="restart ?(.*)", allow_sudo=True))
async def _(event):
    k = await bot.send_message(event.chat_id, '`Wait restarting`') 
    asyncio.sleep(0.5)
    await k.edit('`Restarted successfully`')
    await event.delete()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit ()
    
# Made by Devil ( @lucifeermorningstar) 

@bot.on(admin_cmd(pattern="update")) 
@bot.on(sudo_cmd(pattern="update ? (.*)", allow_sudo=True)) 
async def update(event):
     await event.edit("•• **ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ᴅᴀɪsʏx ᴜsᴇʀʙᴏᴛ ᴛʜᴇɴ ᴊᴜsᴛ `.restart` ᴏɴʟʏ **••") 
