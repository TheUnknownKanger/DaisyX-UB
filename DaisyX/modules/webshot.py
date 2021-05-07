"""Take screenshot of any website
Syntax: .screencapture <Website URL>"""


import os
import io
import requests, asyncio
from telethon import events
from AlainX import bot
from telethon import events
     
        
@bot.on(events.NewMessage(pattern="/webss (.*)"))
async def take_ss(event):
    if event.fwd_from:
        return
    url = event.pattern_match.group(1)
    await bot.send_message(event.chat.id, "Hi")
    try:
        photo = f"https://webshot.amanoteam.com/print?q={url}"
        await bot.send_file(event.chat_id,photo )
    except TypeError:
        await event.reply("No Such Website.")
        return
await take_ss(event)
