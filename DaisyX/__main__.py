import glob
import os
from pathlib import Path
from sys import argv

from telethon import Button, TelegramClient

from DaisyX.utils import load_module, load_pro

os.system("pip install telethon==1.20")
os.system("pip install google_trans_new")
try:
    print("DaisyX X UB IS STARTING WITH TELETHON")
except:
    pass
TOKEN = os.enivron.get("TG_BOT_TOKEN_BF_HER")
NAME = TOKEN.split(":")[0]

bot = TelegramClient(NAME, os.environ.get("APP_ID"), os.environ.get("API_HASH"))

# Telethon
bot.start(bot_token=TOKEN)

# Xbot Client
xbot = TelegramClient("DaisyX", APP_ID, API_HASH).start(bot_token=token)


TOKEN = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
import telethon.utils

EXTRA_PLUGS = os.environ.get("EXTRA_PLUGS", False)


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


ONLINE_ALERT = os.environ.get("ONLINE_ALERT")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if os.environ.get("TG_BOT_USER_NAME_BF_HER") is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=os.environ.get("APP_ID"),
            api_hash=os.environ.get("API_HASH"),
        ).start(bot_token=os.environ.get("TG_BOT_TOKEN_BF_HER"))
        print("Initialisation finished with no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(os.environ.get("TG_BOT_USER_NAME_BF_HER")))
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


if EXTRA_PLUGS == True:
    os.system(
        "git clone https://github.com/TeamDaisyX/DaisyX-Extra.git ./DaisyX/modules/"
    )
    path = "DaisyX/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            try:
                load_module(plugin_name.replace(".py", ""))
                if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                    print("INSTALLING ALL MODULES", plugin_name)
            except:
                pass

else:
    path = "DaisyX/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            load_module(shortname.replace(".py", ""))


import os

print("DaisyX is Up and Awake! ©️ TeamDaisyX 2021")


async def legend():
    pro = await xbot.get_me()
    legend = await bot.get_me()
    LEGENDX = f"""
**Sᴏᴍᴇᴛʜɪɴɢ Hᴀᴘᴘᴇɴᴇᴅ ! Lᴇᴛs Cʜᴇᴄᴋ** 🤔 

`☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎ ☟︎︎︎`

**Dɪɴɢ Dᴏɴɢ...** `.\./.\` **Tɪɴɢ Tᴏɴɢ...** `./.\./` **ᴅᴀɪsʏX Hᴀs Bᴇᴇɴ Dᴇᴘʟᴏʏᴇᴅ !!**

**Pɪɴɢ Pᴏɴɢ...**

**➥ Mᴀsᴛᴇʀ** `➪` **@{legend.username}**
**➥ Assɪsᴛᴀɴᴛ** `➪` **@{pro.username}**
**➥ Sᴜᴘᴘᴏʀᴛ** `➪` **@DaisySupport_Official**
**➥ Cʜᴀɴɴᴇʟ** `➪` **@DaisyXUpdates**

**Cʜᴇᴄᴋ ᴍᴏɪ Pɪɴɢ ᴛɪᴍᴇ ʙʏ** `.ping` **[Fᴏʀ UsᴇʀBᴏᴛ] or** `/ping` **[Fᴏʀ Assɪsᴛᴀɴᴛ]**
"""
    if ONLINE_ALERT:
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
