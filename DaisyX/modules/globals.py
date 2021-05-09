from Skem import SUDOERS
from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from DaisyX.modules.sql_helper.mute_sql import is_muted, mute, unmute
from DaisyX.utils import admin_cmd, sudo_cmd


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
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
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
            return await event.edit("**SOMETHING W3NT WRONG 🤔**", str(err))
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@borg.on(admin_cmd(pattern="gban ?(.*)"))
@borg.on(sudo_cmd("gban ?(.*)", allow_sudo=True))
async def gspider(ULTRA):
    lol = ULTRA
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("GBanning This Retard DumbAss😁😁")
    else:
        friday = await lol.edit("Wait Processing.....")
    me = await ULTRA.client.get_me()
    await friday.edit(f"Global Ban Is Coming ! Wait And Watch You bitch😎🔥")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await ULTRA.get_chat()
    a = b = 0
    if ULTRA.is_private:
        user = ULTRA.chat
        reason = ULTRA.pattern_match.group(1)
    else:
        ULTRA.chat.title
    try:
        user, reason = await get_full_user(ULTRA)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id in SUDOERS:
            return await friday.edit(
                f"**Didn't, Your Father Teach You ? That You Can't Gban My Creator😑😑🖕**"
            )
        try:
            from DaisyX.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await ULTRA.client(BlockRequest(user))
        except:
            pass
        testULTRA = [
            d.entity.id
            for d in await ULTRA.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testULTRA:
            try:
                await ULTRA.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await friday.edit(
                    f"**GBANNING [{user.first_name}](tg://user?id={user.id})**\n\n__Please be Patient..This process takes time.__"
                )
            except:
                b += 1
    else:
        await friday.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await friday.edit(f"**Error! User probably already gbanned.**")
    except:
        pass
    await friday.edit(
        f"**Successfully GBanned [{user.first_name}](tg://user?id={user.id}) // Total Affected Chats :** `{a}` "
    )
    return


@borg.on(admin_cmd(pattern="ungban ?(.*)"))
async def gspider(ULTRA):
    lol = ULTRA
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        friday = await lol.reply("`Wait Let Me Process`")
    else:
        friday = await lol.edit("Just a Second ")
    me = await ULTRA.client.get_me()
    await friday.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await ULTRA.get_chat()
    a = b = 0
    if ULTRA.is_private:
        user = ULTRA.chat
        reason = ULTRA.pattern_match.group(1)
    else:
        ULTRA.chat.title
    try:
        user, reason = await get_full_user(ULTRA)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await friday.edit("**SOMETHING W3NT WRONG 🤔**")
    if user:
        if user.id in SUDOERS:
            return await friday.edit(
                "**You Cant gban him... as a result you can not ungban him... He is My Creator!**"
            )
        try:
            from DaisyX.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await ULTRA.client(UnblockRequest(user))
        except:
            pass
        testULTRA = [
            d.entity.id
            for d in await ULTRA.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testULTRA:
            try:
                await ULTRA.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await friday.edit(
                    f"**UNGBANNING [{user.first_name}](tg://user?id={user.id})**\n\n__Please be Patient..This process takes time.__"
                )
            except:
                b += 1
    else:
        await friday.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await friday.edit("**Error! User probably already ungbanned.**")
    except:
        pass
    return await friday.edit(
        f"**Successfully UnGBanned // USER - [{user.first_name}](tg://user?id={user.id}) IN CHATS :** `{a}`"
    )


@borg.on(ChatAction)
async def handler(rkG):
    client = borg
    if rkG.user_joined or rkG.user_added:
        try:
            from DaisyX.modules.sql_helper.gmute_sql import is_gmuted

            guser = await rkG.get_user()
            gmuted = is_gmuted(guser.id)
        except:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await rkG.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                rkG.chat_id, guser.id, view_messages=False
                            )
                            await rkG.reply(
                                f"**Gbanned User Joined!!** \n"
                                f"**➥ Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**➥ Action **  : `Banned`"
                            )
                        except:
                            rkG.reply("`No Permission To Ban`")
                            return


@bot.on(admin_cmd(pattern="gkick"))
@bot.on(sudo_cmd("gkick ?(.*)", allow_sudo=True))
async def kick(kick):
    xxx = await kick.edit("`Gʟᴏʙᴀʟʟʏ ᴋɪᴄᴋɪɴɢ ᴛʜɪs ɴᴏᴏʙ ᴋɪᴅᴅᴏ`")
    ids = (await kick.get_reply_message()).sender_id
    name = (await bot.get_entity(ids)).first_name
    ohk = (await bot.get_entity(ids)).id
    t = 0
    async for p in bot.iter_dialogs():
        if p.is_group or p.is_channel:
            try:
                await bot.kick_participant(p.id, ids)
                t += 1
            except:
                pass
    await xxx.edit(
        f"**Gʟᴏʙᴀʟʟʏ Kɪᴄᴋᴇᴅ [{name}](tg://user?id={ohk}) \\ Cʜᴀᴛs Aғғᴇᴄᴛᴇᴅ: {t}**"
    )


# @command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
@borg.on(sudo_cmd("gmute ?(.*)", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("**ɢᴍᴜᴛɪɴɢ ᴛʜɪs ᴜsᴇʀ...**")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to gmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("тнιѕ ρєяѕση ιѕ αℓяєα∂у gмυтє∂")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("тнιѕ ρєяѕση gσт gмυтє∂ ѕυ¢¢єѕѕƒυℓℓу")


# @command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
@borg.on(sudo_cmd("ungmute ?(.*)", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("тяуιηg тσ υηgмυтιηg тнιѕ ρєяѕση....\n\n 🙃🏆")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to ungmute them."
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("тнιѕ ρєяѕση ιѕ ησт gмυтє∂")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit(
            "тнιѕ ρєяѕση gσт υηgмυтє∂ ѕυ¢¢єѕѕƒυℓℓу ησω нє/ѕнє ¢αη ѕρєαк ƒяєєℓу"
        )


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


from telethon.errors.rpcerrorlist import YouBlockedUserError

from Assist.DAISYX import MASTER

LEGEND = MASTER
PROBOY = "@tgscanrobot"
# MADE BY LEGENDX22 🔥🔥


@borg.on(admin_cmd("ginfo ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    LEGENDX = event.pattern_match.group(1)
    if "@" in LEGENDX:
        async with borg.conversation(PROBOY) as conv:
            try:

                await event.edit(
                    f"ωαιт ¢нє¢кιηg тнє ∂єтαιℓѕ σƒ тнιѕ ρєяѕση ѕтαятє∂ ву {LEGEND}"
                )
                await conv.send_message("/start")
                await conv.get_response()  # made by LEGENDX22
                await conv.send_message(f"{LEGENDX}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startsawith("This human"):
                    return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()  # made by LEGENDX22
            except YouBlockedUserError:
                await event.edit("Error: @tgscanrobot unblock and retry!")
    elif LEGENDX == "":
        OP = await event.get_reply_message()
        PRO = OP.sender.id
        async with borg.conversation(PROBOY) as conv:
            try:  # made by LEGENDX22 🔥
                # made by LEGENDX22
                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response()  # made by LEGENDX22
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                    return await event.edit("no details Found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError:  # made by LEGENDX22
                await event.edit("Error: unblock @tgscanrobot and try again!")
    else:
        async with borg.conversation(PROBOY) as conv:
            try:  # made by LEGENDX22 🔥

                await event.edit(f"тнιѕ υѕєя ∂єтαιℓѕ ¢нє¢кιηg ву {LEGEND}")
                await conv.send_message("/start")
                await conv.get_response()
                await conv.send_message(f"{PRO}")
                TEAMX = await conv.get_response()
                TEAMX = TEAMX.message
                if TEAMX.startswith("This human"):
                    return await event.edit("no details found")
                await borg.send_message(event.chat_id, TEAMX)
                await event.delete()
            except YouBlockedUserError:
                await event.edit("Error: unblock  @tgscanrobot `and try again!")


from .. import HELP

HELP(
    NAME="ginfo", HELP=".ginfo <tag or username>", FUCK=True, debug=False, amazing=None
)

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
