id = 777
ID = 777
try:
  from userbot import bot
except:
  pass
try:
  import telethon
except:
  os.system("pip install telethon")
from telethon.tl.functions.channels import JoinChannelRequest as joinchat

async def join(chat):
  await bot (joinchat(chat))


def text(event):
  if event.text != "":
    try:
      res = event.text.split(" ", 1)[1]
      return res
    except:
      return None
  else:
    res = "Give me Some text"
    return res