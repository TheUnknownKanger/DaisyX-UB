# (c) Copyright 21-22 By lucifeermorningstar@GitHub , < https://github.com/lucifeermorningstar >
# Only For Use In DaisyX userbot Or For TeamDaisyX

import os
import asyncio
import heroku3

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events

from DaisyX import bot
from DaisyX.utils import admin_cmd

Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS", None)

@bot.on(admin_cmd(pattern="sudo")) 
async def sudo(events):
     sudolelo = os.environ.get("SUDO_USERS", None) 
     await event.reply(event, f"** sᴜᴅᴏʟɪsᴛ ᴏғ ** bot.me.username\n {sudolelo}")
