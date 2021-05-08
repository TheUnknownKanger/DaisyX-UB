# (c) Copyright 2021-2022 DaisyX
# Made By Sipak_Op, Devil and InukaAsith, RoseLoberX
import requests
from DaisyX import bot, DAISYX
from telethon import events
from DaisyX.utils import admin_cmd

@bot.on(admin_cmd(pattern="webss ?(.*)"))
async def events(event):
 BASE = 'https://render-tron.appspot.com/screenshot/'
 url = event.pattern_match.group(1)
 if not url.startswith('https://'):
   url = 'https://' + str(url)
 path = 'target.jpg'
 X = await event.edit("Uploading the screenshot...")
 response = requests.get(BASE + url, stream=True)
 if not response.status_code == 200:
   return await X.edit('Invalid URL Provided.')
 else:
    with open(path, 'wb') as file:
        for chunk in response:
            file.write(chunk)
 await borg.send_file(event.chat_id, path)
 await X.delete()
