# (c) Copyright 21-22 By lucifeermorningstar@GitHub , < https://github.com/lucifeermorningstar >
# Only For Use In DaisyX userbot Or For TeamDaisyX

import os
import asyncio
import heroku3

from telethon.tl.functions.users import GetFullUserRequest
from telethon import events

from DaisyX import bot, SUDO_USERS
from DaisyX.utils import admin_cmd


# Function From TeleBoT

async def edit_or_reply(event, text):
    Try
       if event.user_id == SUDO_USERS:
          reply_to = await event.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await event.reply(text)
    return await event.edit(text)


Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USERS", None)

@bot.on(admin_cmd(pattern="sudo")) 
async def sudo(event):
     sender = await event.get_input_sender()
     sudolelo = os.environ.get("SUDO_USERS", None) 
     await edit_or_reply(event.chat_id, f"** sᴜᴅᴏʟɪsᴛ ᴏғ ** bot.me.username\n {sudolelo}")

