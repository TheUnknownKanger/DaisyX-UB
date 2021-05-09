# COPYRIGHT (C) 2021-2022 BY DaisyX
# Made by LegendX
from telethon import Button, events

from Assist import xbot

from .. import CMD_HELP
from ..utils import admin_cmd
from ..utils import edit_or_reply as eor
from ..utils import sudo_cmd


@borg.on(admin_cmd(pattern="btn (.*)"))
@borg.on(sudo_cmd(pattern="btn", allow_sudo=True))
async def Buttons(event):
    await eor(event, "`Mᴀᴋɪɴɢ Yᴏᴜʀ Bᴜᴛᴛᴏɴ ᴡᴇɪᴛ ᴍᴀsᴛᴇʀ !!!`")
    ULTRAX = Var.TG_BOT_USER_NAME_BF_HER
    pro = event.text[7:]
    pro, boy = pro.split("|")
    f = open("Button.txt", "w")  # by LEGENDX22, PROBOYX
    f.write(f"{pro}\n{boy}")
    f.close()
    LEGENDX = await bot.inline_query(ULTRAX, "BUTTON")
    await LEGENDX[0].click(event.chat_id)
    await event.delete()


@xbot.on(events.InlineQuery(pattern="BUTTON"))
async def file(event):
    f = open("Button.txt")
    ok = f.readlines()[0]
    f.close()
    PROBOYX = open("Button.txt")
    bc = PROBOYX.readlines()[1]
    PROBOYX.close()
    LEGENDX = event.builder
    DEVIL = [[Button.url(f"{ok}", f"{bc}")]]
    INUKA = LEGENDX.article(title="Button by DaisyX", text=f"{ok}", buttons=DEVIL)
    await event.answer([INUKA])


CMD_HELP.update(
    {
        "buttons": ".btn <button name>|<link>\n`.btn DaisyX|https://t.me/DAISYXOT`\nmake sure your name and link no have Useless spece"
    }
)
