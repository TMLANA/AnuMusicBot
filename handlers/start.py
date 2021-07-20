from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CQ8QTWQACCD9gpSGtPso-JueMmC6tCptx2H6VjAACngEAAmpqaFeIQbV46r_aFh8E")
    await message.reply_text(
        f"""<b>مرحبا {message.from_user.first_name}!
\nI يمكن تشغيل الموسيقى في الدردشة الصوتية لمجموعتك
مساعد الموسيقى @MUSICEDL
\nلاضافة البوت المساعد للمجموعة ارسل (دعوة المساعد)
\nلمعرفة اوامر المساعدة ارسل ( اوامر )
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                      "✨ مساعد البوت", url="https://t.me/MUSICEDL",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ اضف البوت لمجموعتك ➕", url="https://t.me/SERRVBOT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("/start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ هل تريد البحث عن فيديو يوتيوب‌‌?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مطور البوت", url="https://t.me/cDDDD"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ نعم", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "لا ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("اوامر")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nتشغيل <song name> - لتشغيل الاغنية التي تطلبها
عرض - عرض قائمة التشغيل
اغنية <song name> - لتنزيل الاغنيه التي تريدها بسرعة
بحث <query> - البحث عن مقاطع الفيديو على youtube مع التفاصيل
ديزر <song name> - قم بتنزيل الأغاني التي تريدها بسرعة عبر deezer
سافان <song name> - قم بتنزيل الأغاني التي تريدها بسرعة عبر saavn
فيديو <song name> - قم بتنزيل مقاطع الفيديو التي تريدها بسرعة
\n*للمشرفين فقط �*
لوحة الموسيقى - افتح لوحة إعدادات مشغل الموسيقى
ايقاف - وقفة تشغيل الأغنية
استئناف - استئناف تشغيل الأغنية
تخطي - تشغيل الأغنية التالية
انهاء - وقف تشغيل الموسيقى
دعوة المساعد - دعوة مساعد إلى الدردشة الخاصة بك
تحديث الادمنية - لتحديث الادمنية بالمجموعة
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "للاستفسار❓", url="https://t.me/cDDDD"
                    )
                ]
            ]
        )
    )    
