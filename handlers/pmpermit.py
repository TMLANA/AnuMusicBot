from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"**😍 Hey I am Assistant Of @AnuVcBot For Playing Music in Group Voice Chat. If You Want to Play Music in Your Group Voice Chat Then Add Me & @AnuVcBot And Make Admin With Full Power. Thank You ...**")
  return                        
