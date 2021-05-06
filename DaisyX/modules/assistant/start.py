# (c) Copyright 2021-2022 DaisyX
# By RoseLoverX


import asyncio
import io
import os
import re

from telethon import Button, custom, events
from telethon.tl.functions.users import GetFullUserRequest

from DaisyX import bot
from DaisyX.functions.DaisyX import PHOTO
from DaisyX.functions.DaisyX import devs as DEVS
from DaisyX.functions.DaisyX import xbot
from DaisyX.modules.sql_helper.blacklist_ass import (
    add_nibba_in_db,
    is_he_added,
    removenibba,
)
from DaisyX.modules.sql_helper.bot_users_sql import his_userid
from DaisyX.modules.sql_helper.idadder_sql import (
    add_usersid_in_db,
    already_added,
    get_all_users,
)

# await function async def ke baad lagega


@xbot.on(events.NewMessage(pattern="/start$"))
async def start(event):
    pro = await bot.get_me()
    boy = pro.id
    iam = await xbot.get_me()
    bot_id = iam.first_name
    bot_username = iam.username
    replied_user = await xbot(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    devlop = await bot.get_me()
    hmmwow = devlop.first_name
    event.chat_id
    mypic = PHOTO
    starttext = f"Hello, **{firstname}**!!\nNice To Meet You 🤗 !!\nI guess, that you know me, Uhh you don't, np..\nWell I'm **{bot_id}**.\n\n**A Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ Oғ** [{hmmwow}](tg://user?id={boy})\n\n                           **Pᴏᴡᴇʀᴇᴅ Bʏ** [ᴅᴀɪsʏX](t.me/DaisyXOT)\n\n**Yᴏᴜ Cᴀɴ Cʜᴀᴛ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ Tʜʀᴏᴜɢʜ Tʜɪs Bᴏᴛ.**\n**Iғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Assɪᴛᴀɴᴛ Yᴏᴜ Cᴀɴ Dᴇᴘʟᴏʏ Fʀᴏᴍ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ.**"
    if event.sender_id == boy:
        await xbot.send_message(
            event.chat_id,
            message=f"Hi Master, It's Me {bot_id}, Your Assistant !! \nWhat You Wanna Do today ?",
            buttons=[
                [custom.Button.inline("Bᴏᴛ Usᴇʀs 🔥", data="users")],
                [custom.Button.inline("Hᴇʀᴏᴋᴜ Mᴇɴᴜ ⚙️", data="ass_back")],
                [
                    Button.url(
                        "Iɴᴠɪᴛᴇ Mᴇ Tᴏ A Gʀᴏᴜᴘ 👥", f"t.me/{bot_username}?startgroup=true"
                    )
                ],
            ],
        )
    else:
        if already_added(event.sender_id):
            pass
        elif not already_added(event.sender_id):
            add_usersid_in_db(event.sender_id)
        await xbot.send_file(
            event.chat_id,
            file=mypic,
            caption=starttext,
            link_preview=False,
            buttons=[
                [
                    custom.Button.url(
                        "Dᴇᴘʟᴏʏ Yᴏᴜʀ Oᴡɴ ᴅᴀɪsʏX",
                        "http://GitHub.com/TeamDaisyX/Daisy-X-UB",
                    )
                ],
                [Button.url("Sᴜᴘᴘᴏʀᴛ", "t.me/DaisySupport_Official")],
            ],
        )
        if os.path.exists(mypic):
            os.remove(mypic)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"users")))
async def users(event):
    pro = await bot.get_me()
    boy = pro.id
    wrong = "sorry you cant access this"
    if not event.sender_id == boy:
        return await event.answer(wrong, alert=False)
    if event.is_group or event.is_private:
        await event.delete()
        total_users = get_all_users()
        users_list = "Lɪsᴛ Oғ Tᴏᴛᴀʟ Usᴇʀs Iɴ Bᴏᴛ. \n\n"
        for ultrappl in total_users:
            users_list += ("=> {} \n").format(int(ultrappl.chat_id))
        with io.BytesIO(str.encode(users_list)) as tedt_file:
            tedt_file.name = "userlist.txt"
            await xbot.send_file(
                event.chat_id,
                tedt_file,
                force_document=True,
                caption="**Tᴏᴛᴀʟ Usᴇʀs Iɴ Yᴏᴜʀ Bᴏᴛ.**",
                allow_cache=False,
            )
    else:
        pass


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmds")))
async def users(event):
    Pro = "The button is under construction...\nSorry for inconvenience, Will update soon....\nThanks..."
    await event.answer(Pro, alert=True)
    # @LEGENDX, #@PROBOY add cmd List Here
    # later bro


@xbot.on(events.NewMessage(pattern="/broadcast ?(.*)"))
async def sedlyfsir(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id in DEVS:
        if not event.sender_id == boy:
            return
    msgtobroadcast = event.text.split(" ", maxsplit=1)[1]
    userstobc = get_all_users()
    error_count = 0
    sent_count = 0
    if msgtobroadcast == None:
        await event.reply("`Wait. What? Broadcast None?`")
        return
    elif msgtobroadcast == "":
        await event.reply("`Give Something to Broadcast ☺️`")
        return
    for uzers in userstobc:
        try:
            sent_count += 1
            await xbot.send_message(int(uzers.chat_id), msgtobroadcast)
            await asyncio.sleep(0.2)
        except:
            error_count += 1
    await xbot.send_message(
        event.chat_id,
        f"**Broadcast Completed in {sent_count} Group/Users..**\n__➥ Error :__ {error_count}\n__➥ Total Number Was :__ {len(userstobc)}",
    )


@xbot.on(events.NewMessage(pattern="/stats"))
async def _(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id == boy:
        return await event.reply("you cant access this")
    all = get_all_users()
    await event.reply(f"**Stats Of Your Bot**\nTotal Users In Bot => {len(all)}")


@xbot.on(events.NewMessage(pattern="/block ?(.*)"))
async def ok(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id == boy:
        return
    if event.sender_id == boy:
        msg = await event.get_reply_message()
        user_id, reply_message_id = his_userid(msg.id)
    if is_he_added(user_id):
        await event.reply("Already Blacklisted")
    elif not is_he_added(user_id):
        add_nibba_in_db(user_id)
        await event.reply("Blacklisted This Dumb Person")
        await xbot.send_message(
            user_id, "You Have Been Blacklisted And You Can't Message My Master Now."
        )


@xbot.on(events.NewMessage(pattern="/unblock ?(.*)"))
async def gey(event):
    pro = await bot.get_me()
    boy = pro.id
    if not event.sender_id == boy:
        return
    if event.sender_id == boy:
        msg = await event.get_reply_message()
        msg.id
        event.raw_text
        user_id, reply_message_id = his_userid(msg.id)
    if not is_he_added(user_id):
        await event.reply("Not Even. Blacklisted🚶")
    elif is_he_added(user_id):
        removenibba(user_id)
        await event.reply("DisBlacklisted This Dumb Person")
        await xbot.send_message(
            user_id, "Congo! You Have Been Unblacklisted By My Master."
        )
