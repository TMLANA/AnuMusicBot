from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"**😍 مرحبًا ، أنا مساعدAnuVcBot لتشغيل الموسيقى في الدردشة الصوتية الجماعية.  إذا كنت ترغب في تشغيل الموسيقى في الدردشة الصوتية الجماعية ، فأضفني  واجعل المسؤول بكامل القوة.  اشكرك ...**")
  return                        
