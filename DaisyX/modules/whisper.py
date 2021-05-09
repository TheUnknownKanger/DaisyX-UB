import os
import re

from telethon import Button, events

from Assist import id, xbot


@xbot.on(events.InlineQuery(pattern="wspr"))
async def inline_proboy(event):
    DAISYX = event.text[5:]
    DAISYX, INUKA = DAISYX.split("@")
    os.system("rm -rf wspr.txt")
    f = open("wspr.txt", "a")
    f.write(DAISYX + "\n" + INUKA)
    f.close()
    DEVIL = event.builder
    ALAIN = [[Button.inline("🔐 Sʜᴏᴡ", data="secret")]]
    ALAIN += [[Button.switch_inline("Rᴇᴘʟʏ", query="wspr", same_peer=True)]]
    SKEM = DEVIL.article(
        title=f"Wʜɪsᴘᴇʀ Fᴏʀ @{INUKA}",
        text=f"<b>📩 Sᴇᴄʀᴇᴛ Msɢ</b> Tᴏ <b>@{INUKA}</b>. Oɴʟʏ Hᴇ/Sʜᴇ Cᴀɴ Oᴘᴇɴ Iᴛ..",
        buttons=ALAIN,
        parse_mode="html",
    )
    await event.answer([ALAIN])


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret")))
async def wspr(event):
    try:
        f = open("wspr.txt")
        DEVIL = f.readlines()[0]
        f.close()
        pro = open("wspr.txt")
        DAISYX = pro.readlines()[1].lower()
        pro.close()
        bot = await xbot.get_me()
        sender = f"{event.sender.username}".lower()
        me = f"{borg.me.username}".lower()
        if sender == DAISYX or sender == me or event.sender_id == id:
            await event.answer(DEVIL, alert=True)
        else:
            await event.answer(
                "Yes You, Little Shit, Why're u seeing my msg??", alert=False
            )
    except:
        await event.answer(
            f"Use @{bot.username} wspr <msg> <@ sender username>\n\nAnd ofc, remove those <>",
            alert=True,
        )
