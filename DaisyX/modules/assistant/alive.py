# COPYRIGHT (C) 2021-2022 BY Daisy X
# modify by madboy482 and alain_champion and LegendX22

import datetime
import re
import time

from telethon import Button, custom, events

from Assist import BOT, PHOTO, VERSION, xbot
from DaisyX import StartTime, bot


@xbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
    DaisyX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
    DaisyX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
    DaisyX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
    DaisyX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
    DaisyX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
    DaisyX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
    DaisyX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
    BUTTON = [
        [
            Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"),
            Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/TeamDaisyX/Daisy-X-UB"),
        ]
    ]
    BUTTON += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="DaisyX")]]
    await xbot.send_file(event.chat_id, PHOTO, caption=DaisyX, buttons=BUTTON)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"SkemX")))
async def callback_query_handler(event):
    # inline by LEGENDX22 and PROBOY22 🔥 #Ported Here By Devil 🔥
    SkemX = [[Button.url("Rᴇᴘᴏ ᴅᴀɪsʏX", "https://github.com/TeamDaisyX/DaisyX-UB")]]
    SkemX += [
        [
            Button.url(
                "Dᴇᴘʟᴏʏ ᴅᴀɪsʏX",
                "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB&template=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB",
            )
        ]
    ]
    SkemX += [
        [
            Button.url("Tᴜᴛᴏʀɪᴀʟ", "https://youtu.be/rGCSSFPsS4Q"),
            Button.url(
                "Sᴛʀɪɴɢ Sᴇssɪᴏɴ", "https://replit.com/@legendx22/ULTRA-X#main.py"
            ),
        ]
    ]
    SkemX += [
        [
            Button.url("Aᴘɪ Iᴅ & Aᴘɪ Hᴀsʜ", "https://t.me/DaisyXScrapperBot"),
            Button.url("Rᴇᴅɪs", "https://redislabs.com"),
        ]
    ]
    SkemX += [
        [
            Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", "https://t.me/DaisyXOT"),
            Button.url("Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", "https://t.me/DaisySupport_Official"),
        ]
    ]
    SkemX += [[custom.Button.inline("«« Aʟɪᴠᴇ", data="Skem")]]
    await event.edit(text=f"Aʟʟ Dᴇᴛᴀɪʟs Oғ Rᴇᴘᴏs", buttons=SkemX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"Skem")))
async def callback_query_handler(event):
    # inline by LEGENDX22 and PROBOY22 🔥
    DaisyX = f"Hᴇʟʟᴏ !! Tʜɪs ɪs **{BOT}**\n\n"
    DaisyX += "**Aʟʟ sʏsᴛᴇᴍs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ...**\n\n"
    DaisyX += f"**{BOT} Vᴇʀsɪᴏɴ** : `{VERSION}`\n\n"
    DaisyX += f"**Usᴇʀ** : @{bot.me.username}\n\n"
    DaisyX += "**Fᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ...**\n\n"
    DaisyX += "**Tᴇʟᴇᴛʜᴏɴ** : `1.20`\n\n"
    DaisyX += "~~ **Tʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ** !!"
    BUTTONS = [
        [
            Button.url("Mᴀsᴛᴇʀ", f"https://t.me/{bot.me.username}"),
            Button.url(f"{BOT} Rᴇᴘᴏ", "https://github.com/ULTRA-OP/ULTRA-X"),
        ]
    ]
    BUTTONS += [[custom.Button.inline("Rᴇᴘᴏsɪᴛᴏʀɪᴇs »»", data="DaisyX")]]
    await event.edit(text=DaisyX, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo")))
async def repo(event):
    await xbot.send_message(
        event.chat,
        "**Hᴇʀᴇ Is Tʜᴇ Rᴇᴘᴏ Fᴏʀ ᴅαιѕу χ Usᴇʀʙᴏᴛ** \n\nFᴏʀ Aɴʏ Hᴇʟᴘ :- @DaisyXOT",
        buttons=[
            [
                Button.url("⚜️ Rᴇᴘᴏ ⚜️", "https://github.com/TeamDaisyX/Daisy-X-UB"),
                Button.url(
                    "🔰 Dᴇᴘʟᴏʏ 🔰",
                    "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB&template=https%3A%2F%2Fgithub.com%2FTeamDaisyX%2FDaisy-X-UB",
                ),
            ]
        ],
    )


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@xbot.on(events.NewMessage(pattern=None))
async def ok(event):
    msg = str(event.text)
    if not msg == "/ping":
        return

    start_time = datetime.datetime.now()
    message = await event.reply("_.._.._Pinging_.._.._")
    end_time = datetime.datetime.now()
    pingtime = end_time - start_time
    telegram_ping = str(round(pingtime.total_seconds(), 2)) + "s"
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(
        "<b><i>☞ Pᴏɴɢ !!</i></b>\n"
        "<b>➥ Tɪᴍᴇ Tᴀᴋᴇɴ:</b> <code>{}</code>\n"
        "<b>➥ Sᴇʀᴠɪᴄᴇ Uᴘᴛɪᴍᴇ:</b> <code>{}</code>".format(telegram_ping, uptime),
        parse_mode="html",
    )
