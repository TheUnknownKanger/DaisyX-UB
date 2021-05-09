import re

from telethon import Button, custom, events
from telethon.tl.custom import Button

from Assist.DAISYX import xbot
from DaisyX import bot
from DaisyX.utils import admin_cmd, sudo_cmd


@xbot.on(events.InlineQuery(pattern=r"repo"))
async def inline_id_handler(event: events.InlineQuery.Event):

    DAISY = event.builder
    X = [[custom.Button.inline("🔥 Cʟɪᴄᴋ Hᴇʀᴇ 🔥", data="obhai")]]
    event.text

    result = DAISY.article(
        "ᴅᴀɪsʏX",
        text="**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Sᴜᴘᴘᴏʀᴛ\n\n© @DaisyXOT**",
        buttons=X,
        link_preview=False,
    )
    await event.answer([result])


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"obhai")))
async def callback_query_handler(event):
    await event.edit(
        text=f"**ᴅᴀɪsʏX's Rᴇᴘᴏ, Dᴇᴘʟᴏʏ ᴀɴᴅ Gʀᴏᴜᴘ Lɪɴᴋ\n\n© @DaisyXOT**",
        buttons=[
            [
                Button.url(
                    f"⚜️ Rᴇᴘᴏ ⚜️", url="https://github.com/TeamDaisyX/Daisy-X-UB"
                ),
                Button.url(
                    f"🌚 Sᴜᴘᴘᴏʀᴛ Cʜᴀᴛ 🌝", url="https://t.me/DaisySupport_Official"
                ),
            ],
            [
                Button.url(
                    f"🔰 Dᴇᴘʟᴏʏ 🔰",
                    url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB&template=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB",
                ),
                Button.url(
                    f"💠 Sᴛʀɪɴɢ 💠", url="https://repl.it/@SpEcHiDe/GenerateStringSession"
                ),
            ],
        ],
    )


# (c) Copyright 2021-2022 TeamDaisyX
# Made by Devil (@Lucifeermorningstar) and @RoseHaterX


@bot.on(admin_cmd(pattern="repo"))
@bot.on(sudo_cmd(pattern="repo ? (.*) ", allow_sudo=True))
async def repo(event):
    buttons = [Button.url(f"⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/TeamDaisyX/Daisy-X-UB")]
    await event.edit("**DAISYX UB**", buttons=buttons)
