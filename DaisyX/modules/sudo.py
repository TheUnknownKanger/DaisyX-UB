import heroku3

from var import Var

from ..utils import admin_cmd

LEGENDX = Var.HEROKU_APP_NAME
PROBOYX = Var.HEROKU_API_KEY


@bot.on(admin_cmd(pattern="addsudo"))
async def add_sudo(event):
    Heroku = heroku3.from_key(PROBOYX)
    app = Heroku.app(LEGENDX)
    heroku_var = app.config()
    if event.is_reply:
        id = (await event.get_reply_message()).sender_id
        name = (await bot.get_entity(id)).first_name
        if id in heroku_var:
            await event.edit(f"{name} 𝙸𝚂 ᴀᴅᴅᴇᴅ ᴀs sᴜᴅᴏ ᴜsᴇʀ")
        else:
            pass
        if heroku_var["SUDO_USERS"] == None:
            await event.edit(f" {name} ɪs ᴀᴅᴅᴇᴅ ᴀs sᴜᴅᴏ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ")
            heroku_var["SUDO_USERS"] = id
        else:
            var = heroku_var["SUDO_USERS"]
            await event.edit(
                f" {name} ɪs ᴀᴅᴅᴇᴅ ᴀɴᴅ ᴏʟᴅ ᴜsᴇʀs ʀᴇᴍᴏᴠᴇᴅ ɪғ ʏᴏᴜ ᴀᴅᴅ 2 ᴏʀ ᴍᴏʀʀ ᴛʜᴀʜ 2 ᴜsᴇʀs ᴏɴ sᴜᴅᴏ ɢᴏ ᴛᴏ ʜᴇʀᴏᴋᴜ ᴀᴅᴅ ᴍᴀɴᴜᴀʟʟʏ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ"
            )
            heroku_var["SUDO_USERS"] = id
    else:
        text = event.text.split(" ", maxsplit=1)[1]
        if text in heroku_var:
            await event.edit(f" {name} ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ sᴜᴅᴏ ʟɪsᴛ")
        else:
            pass
        if heroku_var["SUDO_USERS"] == None:
            await event.edit(f" {name} ɪs ᴀᴅᴅᴇᴅ ᴀs sᴜᴅᴏ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢʟɢ")
            heroku_var["SUDO_USERS"] = text
        else:
            var = heroku_var["SUDO_USERS"]
            await event.edit(
                f" {name} ɪs ᴀᴅᴅᴇᴅ ᴀɴᴅ {var} ʀᴇᴍᴏᴠᴇᴅ ɪɴ sᴜᴅᴏ ɪ ᴀᴍ ʀᴇsᴛᴀʀᴛɪɴɢ"
            )
            heroku_var["SUDO_USERS"] = text


@bot.on(admin_cmd(pattern="rmsudo"))
async def remove_sudo(event):
    Heroku = heroku3.from_key(PROBOYX)
    app = Heroku.app(LEGENDX)
    heroku_var = app.config()
    if event.is_reply:
        id = (await event.get_reply_message()).sender_id
        name = (await bot.get_entity(id)).first_name
        if id in heroku_var:
            await event.edit(f"THE {name} IS REMOVED ON SUDO LIST")
            del heroku_var["SUDO_USERS"]
        else:
            pass
        if heroku_var["SUDO_USERS"] == None:
            await event.edit(f"SUDO LIST IS ALREADY IS Empty")
            heroku_var["SUDO_USERS"] = id
