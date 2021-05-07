"""Take screenshot of any website
Syntax: .screencapture <Website URL>"""


import os
import io
import requests
from telethon import events
from DaisyX.utils import admin_cmd
     
        
@borg.on(admin_cmd("webss (.*)"))
async def take_ss(event):
    if event.fwd_from:
        return
    url = event.pattern_match.group(1)
    m = await event.edit("Processing ...")
    await m.edit("**Uploading**")
    try:
        await borg.send_photo(
            event.chat_id,
            photo=f"https://webshot.amanoteam.com/print?q={url}",
        )
    except TypeError:
        await m.edit("No Such Website.")
        return
    await m.delete()
