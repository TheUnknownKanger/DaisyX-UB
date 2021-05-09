# (c) Copyright 2021-2022 DaisyX
# Made By @lucifeermorningstar (Devil) 
# 🤣 sed I am laughing on me thinking adding credit at this a small normal plugin which anyone can easily made 🥺


from DaisyX import bot
from DaisyX.utils import admin_cmd
@bot.on(admin_cmd(pattern=r"alive"))
async def amialivedad(event): 
   chat = event.chat_id 
   message = " Master ! I am alive :)" 
   await event.edit(message)
