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


global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/9e009eefb93872370607a.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"awake"))
@borg.on(sudo_cmd(pattern=r"awake", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "`**𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙾𝙵 𝚁𝙰𝚅𝙰𝙽𝙰 𝙾𝙽𝙻𝙸𝙽𝙴**`\n\n"
    pm_caption += "**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ About My System ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ `{version.__version__}`\n"
    pm_caption += f"`➾ **ᴜᴘᴛɪᴍᴇ** ☞ `{uptime}`\n\n"
    𝚙𝚖_𝚌𝚊𝚙𝚝𝚒𝚘𝚗 += "➾ **`𝙼𝚎𝚛𝚎 𝚖𝚊𝚜𝚝𝚎𝚛 𝚜𝚎 𝚝𝚑𝚘𝚍𝚊 𝙺𝚊𝚢𝚍𝚎 𝚖𝚎 𝚑𝚒 𝚋𝚊𝚊𝚝 𝚔𝚛𝚎 𝚝𝚘 𝚊𝚊𝚙𝚔𝚎 𝚑𝚎𝚊𝚕𝚝𝚑 𝚔 𝚕𝚒𝚢𝚎 𝚜𝚊𝚑𝚒 𝚑𝚘𝚐𝚊`**\n\n"
    pm_caption += "➾ **`𝙼𝚢 𝚖𝚊𝚜𝚝𝚎𝚛 𝚍𝚘𝚎𝚜𝚗'𝚝 𝚔𝚗𝚘𝚠 𝚊𝚗𝚐𝚛𝚎𝚣𝚒. 𝚃𝚘 𝚓𝚢𝚊𝚍𝚊 2050 𝚔 𝚖𝚘𝚍𝚎𝚛𝚗 𝚒𝚝𝚎𝚖 𝚖𝚊𝚝 𝚋𝚗𝚗𝚊 𝚖𝚎𝚛𝚎 𝚖𝚊𝚜𝚝𝚎𝚛 𝚔 𝚜𝚊𝚊𝚖𝚗𝚎`**\n\n"
    pm_caption += "➾ **`𝙱𝚎 𝚊 𝚂𝚊𝚋𝚑𝚢𝚊 𝚜𝚝𝚞𝚍𝚎𝚗𝚝`**\n\n\n"
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

    

