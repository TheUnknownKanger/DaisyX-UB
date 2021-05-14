import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from DaisyX.utils import admin_cmd, sudo_cmd
from DaisyX import ALIVE_NAME, StartTime as Lastupdate
from DaisyX.helpers import functions as dcdef
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else bot.me.first_name

from DaisyX import VERSION
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b174bd3efbe9590a8e2e4.jpg"
file2 = "https://telegra.ph/file/70bf9fd1f0571ebf29be3.jpg"
file3 = "https://telegra.ph/file/62928bf1b39acce656417.jpg"
file4 = "https://telegra.ph/file/22ab2fe44d05ed825c422.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"awake"))
@borg.on(sudo_cmd(pattern=r"awake", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** Hᴇʏᴀ ᴍᴀsᴛᴇʀ, I'ᴍ ᴏɴʟɪɴᴇ**\n\n"
    pm_caption += "**Wʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴɴᴀ ᴅᴏ ᴛᴏᴅᴀʏ? Bᴜᴛ ʙᴇғᴏʀᴇ ᴅᴏɪɴɢ sᴏᴍᴇᴛɪɴɢ ᴋɴᴏᴡ ᴀʙᴏᴜᴛ ᴍᴏɪ sʏsᴛᴇᴍ...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"👉 **Tᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{version.__version__}`\n"
    pm_caption += f"👉 **Pʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `3.8.7`\n"
    pm_caption += f"👉 **Lɪᴄᴇɴsᴇ:** **[Team Daisy](https://github.com/TeamDaisyX)**\n"
    pm_caption += f"👉 **Dᴀɪsʏ ᴠᴇʀsɪᴏɴ:** `{VERSION}`\n"
    pm_caption += f"👉 **Uᴘᴛɪᴍᴇ:** `{uptime}`"
    pm_caption += f"👉 **Bʀᴀɴᴄʜ:** `Main`"
    pm_caption += f"👉 **Mᴀsᴛᴇʀ:** `{bot.me.first_name}`\n"
   ''' on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)'''

    

