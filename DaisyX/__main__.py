import os
from sys import argv

from DaisyX import bot, xbot
from DaisyX.functions.run import run_cmd
os.system("pip install telethon==1.19.0")
import os

os.system("pip install google_trans_new")
import glob
import os
from pathlib import Path

from telethon import Button, TelegramClient

from DaisyX.utils import load_module, load_pro, load_extra
from var import Var

TOKEN = os.environ.get("TG_BOT_TOKEN", None)
import telethon.utils

EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)

async def xtra_load():
    await run_cmd("bash main_utils/other_plugins.sh")
    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


ONLINE_ALERT = os.environ.get("ONLINE_ALERT", True)
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

import glob

path = "DaisyX/modules/assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_pro(shortname.replace(".py", ""))


if "LEGENDX" != "DEVIL":
    path = "DaisyX/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))
            

            
else:
    print("fuck off kanger chala Ka madarchod")
import os

print("Assistant of RAVANA is Up and Awake! \n©️ ℝ𝔸𝕍𝔸ℕ𝔸")


async def legend():
    pro = await xbot.get_me()
    legend = await bot.get_me()
    if EXTRA_PLUGS != False:
      print("LoAdInG XtRa PlUgInS.. ")
      await xtra_load()
      path = "ExtraPlugins/*.py"
      files = glob.glob(path)
      for name in files:
        with open(name) as f:
          path1 = Path(f.name)
          shortname = path1.stem
          load_extra(shortname.replace(".py", ""))   
      print("X-TrA pLuGiNs LoAdEd")
    LEGENDX = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **DAISYX Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{legend.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
    if ONLINE_ALERT is True:
        try:
            PROBOYX = [[Button.inline("Hᴇʀᴏᴋᴜ Vᴀʀs", data="ass_back")]]
            await xbot.send_message(bot.me.id, LEGENDX, buttons=PROBOYX)
        except:
            pass
    else:
        print("YOUR BOT DEPLOYED SUCCESSFULLY")


bot.loop.run_until_complete(legend())
if len(argv) not in (1, 3, 4):
    bot.disconnect()

else:
    bot.run_until_disconnected()
