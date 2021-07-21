from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["دعوة المساعد"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>أضفني كمسؤول عن مجموعتك أولاً</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "AnuVcBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"انضممت هنا كما طلبت")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@MUSICEDL بالفعل هوه بالمجموعة</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 خطاء انتـــظر 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for userbot! Make sure user is not banned in group."
            "\n\n أو أضف @MUSICEDL يدويًا إلى مجموعتك وحاول مرة أخرى</b>",
        )
        return
    await message.reply_text(
            "<b>المساعد بالدردشة : @MUSICEDL | مطور البوت : @cDDDD</b>",
        )
    
@USER.on_message(filters.group & filters.command(["طرد المساعد"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>لا يمكن للمستخدم مغادرة مجموعتك!  قد يكون معطل او محظور."
            "\n\nأو اطردني يدويًا من مجموعتك</b>",
        )
        return
