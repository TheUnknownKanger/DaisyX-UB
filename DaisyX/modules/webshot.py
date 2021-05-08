# (c) Copyright 2021-2022 DaisyX
# Made By Sipak_Op, Devil and InukaAsith
# CREDIS = PROBOYX
import requests
from DaisyX import bot, DAISYX
from telethon import events
from DaisyX.utils import admin_cmd

@bot.on(admin_cmd(pattern="webss"))
async def events(event):
  BASE = 'https://render-tron.appspot.com/screenshot/'
  url = DAISYX(event)
  path = 'target.jpg'
  response = requests.get(BASE + url, stream=True)
  if response.status_code == 200:
      with open(path, 'wb') as file:
          for chunk in response:
              file.write(chunk)

  await borg.send_file(event.chat_id, path)
