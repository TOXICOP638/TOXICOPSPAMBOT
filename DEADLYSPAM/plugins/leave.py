import asyncio
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDOERS
import config
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys

OWNER_ID = config.OWNER_ID
hl = config.CMD_HNDLR

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sleave(?: |$)(.*)" % hl))
async def _(event):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if event.sender_id in SUDOERS:
        deadly = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(event.text) > 7:
            bc = deadly[0]
            Xd = int(bc)           
            blaze = await event.reply("**ᴄᴍɴᴅꜱ ᴅᴀᴀʟ ᴋʀ ɢʟᴛɪ ᴋᴀʀᴅɪ 🥺**")
            try:
                await event.client(LeaveChannelRequest(Xd))
                await blaze.edit("**» ꜰɪʀ ᴍɪʟᴇɴɢᴇ 😈**")
            except Exception as e:
                await event.edit(str(e))   
        if event.is_private:
            await event.reply(f**"» ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ʙᴋᴄʜᴏᴅᴇʀ ʟᴏɢ 🥴😂!**") 
        else:
            await event.reply(usage, parse_mode=None, link_preview=None)   
    else:
        await event.reply("**ʙɴᴀʏᴇɢᴀ ᴋʏᴀ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴊᴀɪꜱᴀ ʙᴏᴛ 🥴🥴😂!**") 
