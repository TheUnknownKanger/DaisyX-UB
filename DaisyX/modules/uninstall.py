# (c) Copyright 2021-2022 DaisyX
# modify by @LEGENDX22
# credits shivam thanks bruh

import os

from DaisyX import CMD_HELP
from DaisyX.events import remove_plugin
from DaisyX.utils import admin_cmd, remove_plugin


@bot.on(admin_cmd(pattern=r"^uninstall (?P<shortname>\w+)$"))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./ULTRA/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**Uɴɪɴsᴛᴀʟʟᴇᴅ** `{shortname}` **Sᴜᴄᴄᴇssғᴜʟʟʏ**")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))


CMD_HELP.update(
    {
        "uninstall": "**Plugin : **`uninstall`\
    \n\n**Syntax : **`uninstall`\
    \n**Function : **use this plugin without . and small later"
    }
)
