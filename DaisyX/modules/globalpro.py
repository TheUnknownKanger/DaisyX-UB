# (c) Copyright 2021-2022 DaisyX

# code starting...

marculs = 9
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights, MessageEntityMentionName

from DaisyX import bot as borg
from DaisyX.utils import admin_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        # credit bahut ho gya, yaar as bahut mehnat se bna hai, kang mat krna....
        # Pls kang mat krna pyar se bol rha hu, nhi to DMCA hai hi
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Iᴛ ɪs ɴᴏᴛ ᴘᴏssɪʙʟᴇ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴜsᴇʀ ɪᴅ`")
            # credit bahut ho gya, yaar as bahut mehnat se bna hai, kang mat krna....
            # Pls kang mat krna pyar se bol rha hu, nhi to DMCA hai hi
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):

                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit(
                "`Eʀʀᴏʀ Pʟᴇᴀsᴇ Rᴇᴘᴏʀᴛ Iɴ` **@DaisyXOT**`.`", str(err)
            )

    return user_obj, extra


global hawk, moth
hawk = "admin"
moth = "owner"


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        await event.edit(str(err))
        return None
    return user_obj


# back click kar madharchod # back click kar madharchod # back click kar madharchod
# back click kar madharchod # back click kar madharchod # back click kar madharchod
# back click kar madharchod # back click kar madharchod # back click kar madharchod


@borg.on(admin_cmd(pattern="gpromote ?(.*)"))
async def gben(userbot):
    ultrax = legend = userbot
    i = 0
    await legend.get_sender()
    me = await userbot.client.get_me()
    await ultrax.edit("`Pʀᴏᴍᴏᴛɪɴɢ...`")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        await ultrax.edit("`Aʀᴇ ʏᴏᴜ ᴀ ɴᴏᴏʙ ᴡʜᴏ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ʏᴏᴜʀsᴇʟғ ㋛ !!`")
        return
    try:
        if not rank:
            rank = "ㅤㅤ"
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
            # Reserved, Copyrighted by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
    except:
        return await legend.edit(f"**Sᴏᴍᴇᴛʜɪɴɢ W3ɴᴛ Wʀᴏɴɢ 🧐 !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=True,
            invite_users=True,
            change_info=True,
            ban_users=True,
            # ot, If found in any other repo, be ready for DMCA
            delete_messages=True,
            pin_messages=True,
        )
        for x in telchanel:
            try:
                await userbot.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(
                    f"**Nᴇᴡ Gᴘʀᴏᴍᴏᴛɪᴏɴ !!**\n\n**Usᴇʀ** :- __[{user.first_name}](tg://user?id={user.id})__\n**Aғғᴇᴄᴛᴇᴅ Cʜᴀᴛs** :- `{i}`"
                )
            except:
                pass
    else:
        await ultrax.edit(f"`Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ Gᴘʀᴏᴍᴏᴛᴇ ᴛʜᴇᴍ...`")
    return await ultrax.edit(
        f"**Nᴇᴡ Gᴘʀᴏᴍᴏᴛɪᴏɴ !!**\n\n**Usᴇʀ** :- __[{user.first_name}](tg://user?id={user.id})__\n**Aғғᴇᴄᴛᴇᴅ Cʜᴀᴛs** :- `{i}`"
        #
    )


# back click kar madharchod # back click kar madharchod

# credit bahut ho gya, yaar as bahut mehnat se bna hai, kang mat krna....
# Pls kang mat krna pyar se bol rha hu, nhi to DMCA hai hi

# jana lavde back click kar

# Copyright (C) 2021 By Team UltraX

# ~ LegendX
# ~ ProBoyX
# ~ Alain
# ~ MadBoy
# ~ RoseLoverX

# Global Promote and Demote Plugin by Team UltraX for UltraX UserBot
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
# Mobile me back option he uspe click karde madhachod kang kiya to dekh
# Mobile me back option he uspe click karde madhachod kang kiya to dekh


# Kang with Credits, else gey
# I knew u will kang and remove credits, duffer!!

# Last Warn - Undo the removed part else be ready for DMCA by LegendX


@borg.on(admin_cmd(pattern="gdemote ?(.*)"))
async def gben(userbot):
    ultrax = legend = userbot
    i = 0
    await ultrax.get_sender()
    me = await userbot.client.get_me()
    await legend.edit("`Dᴇᴍᴏᴛɪɴɢ...`")
    # credit bahut ho gya, yaar as bahut mehnat se bna hai, kang mat krna....
    # Pls kang mat krna pyar se bol rha hu, nhi to DMCA hai hi
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await userbot.get_chat()
    if userbot.is_private:
        user = userbot.chat
        #
        rank = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, rank = await get_full_user(userbot)
    except:
        pass
    if me == user:
        await ultrax.edit("`Aʀᴇ ʏᴏᴜ ᴀ ɴᴏᴏʙ ᴡʜᴏ ᴡᴀɴᴛ ᴛᴏ ᴅᴇᴍᴏᴛᴇ ʏᴏᴜʀsᴇʟғ ㋛ !!`")
        #

        return
    try:
        if not rank:
            rank = "ㅤㅤ"
    except:
        # by ULTRA-X, only for ULTRA-X UserBot, If found in any other repo, be ready for DMCA
        return await legend.edit(f"**Sᴏᴍᴇᴛʜɪɴɢ W3ɴᴛ Wʀᴏɴɢ 🧐 !!**")
    if user:
        telchanel = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        rgt = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None,
        )
        for x in telchanel:
            try:
                await userbot.client(EditAdminRequest(x, user, rgt, rank))
                i += 1
                await legend.edit(
                    f"`Gʟᴏʙʙᴀʟʏ Dᴇᴍᴏᴛᴇᴅ` **[{user.first_name}](tg://user?id={user.id})** `Iɴ` **{i}** `Cʜᴀᴛs.`"
                )
            except:
                pass
    else:
        await ultrax.edit(f"`Rᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴛᴏ Gᴘʀᴏᴍᴏᴛᴇ ᴛʜᴇᴍ...`")
