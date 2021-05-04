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
from . import legdf as dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀɪsʏ χ"


global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/b174bd3efbe9590a8e2e4.jpg"
file2 = "https://telegra.ph/file/70bf9fd1f0571ebf29be3.jpg"
file3 = "https://telegra.ph/file/62928bf1b39acce656417.jpg"
file4 = "https://telegra.ph/file/22ab2fe44d05ed825c422.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** 𝙳𝙰𝙸𝚂𝚈 𝚇 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n\n"
    pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/DaisySupport_Official)\n"
    pm_caption += "➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [𝚃𝙴𝙰𝙼 𝙳𝙰𝙸𝚂𝚈𝚇](https://github.com/TeamDaisyX)\n"
    pm_caption += "➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [𝙳𝙰𝙸𝚂𝚈-𝚇](https://github.com/TeamDaisyX/Daisy-X-UB)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ghanti})\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

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
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    

