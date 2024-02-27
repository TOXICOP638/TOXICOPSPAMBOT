import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph/file/1b04a4a84ad51aa9887a2.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 𝐓𝐄𝐀𝐌_𝐂𝐑𝐈𝐌𝐈𝐍𝐀𝐋𝐒 𝐇𝐄𝐑𝐄 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍** : `4.0.0`\n"
DEADLY += f"• **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍** : `{version.__version__}`\n"
DEADLY += f"• **𝐓𝐎𝐗𝐈𝐂 𝐕𝐄𝐑𝐒𝐈𝐎𝐍**  : `{Toxicversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/HEROKU_CC_STORE"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/DEADLY_SPAM_BOT")], [Button.url("• ʀᴇᴘᴏ •", "https://github.com/Team-Deadly/DEADLY-SPAMBOT")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze) 
  else:
      await event.reply("**ʙɴᴀʏᴇɢᴀ ᴋʏᴀ ᴀᴘɴᴇ ʙᴀᴀᴘ ᴊᴀɪꜱᴇ ʙᴏᴛ 😂!**") 
