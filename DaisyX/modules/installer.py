# maded by shivam
# ported by Devil
from pathlib import Path

from DaisyX import CMD_LIST
from DaisyX.utils import load_module, register

DELETE_TIMEOUT = 5
import os


@register(pattern="^!install", outgoing=True)
async def install(event):
    a = "Installing."
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "./DaisyX/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "Commands found in {}\n".format(
                        (os.path.basename(downloaded_file_name))
                    )
                    for i in CMD_LIST[shortname]:
                        string += "  •  " + i
                        string += "\n"
                        if b == 1:
                            a = "Installing.."
                            b = 2
                        else:
                            a = "Installing..."
                            b = 1
                        await event.edit(a)
                    return await event.edit(
                        f"Installed module\n{shortname}\n\n{string}"
                    )
                return await event.edit(
                    f"Installed module {os.path.basename(downloaded_file_name)}"
                )
            else:
                os.remove(downloaded_file_name)
                return await event.edit(
                    f"Failed to Install \nError\nModule already installed or unknown formet"
                )
        except Exception as e:
            await event.edit(f"Failed to Install \nError\n{str(e)}")
            return os.remove(downloaded_file_name)
