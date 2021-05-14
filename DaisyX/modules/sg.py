# -0,0 +1,96 @@
# Made by legendx22
# Retrieves the name history and the username history of the replied user.
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from DaisyX import CMD_HELP
from DaisyX.utils import admin_cmd


@borg.on(admin_cmd(pattern="sg ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("Reply to any user message.")
        return
    reply_message = await event.get_reply_message()
    chat = "Sangmatainfo_bot"
    sender = reply_message.sender.id
    if reply_message.sender.bot:
        await event.edit("Reply to actual users message.")
        return
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            # await conv.send_message("/search_id {}".format(sender))
            response1 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response2 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response3 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await conv.send_message("/search_id {}".format(sender))
            response1 = await response1
            response2 = await response2
            response3 = await response3
        except YouBlockedUserError:
            await event.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        if response1.text.startswith("No records found"):
            await event.edit("chutiye ne kabhi username change hi nhi kiya… ")
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response2.message)

            await event.client.send_message(event.chat_id, response3.message)


CMD_HELP.update(
    {
        "sg": "__**PLUGIN NAME :** sg__\
    \n\n📌** CMD ★** `.sg`\
    \n**USAGE   ★  **Retrieves the name and username history of the replied user even if he has forwarded message privacy..! This may not always work as perfect it should be..if doesn't then try once again.."
    }
)
