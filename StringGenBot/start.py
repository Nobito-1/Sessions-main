from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""⎉︙مرحـباً بـك عزيـزي  {msg.from_user.mention} فـي بـوت اسـتـخـراج الـجـلـسـات لسـورس المطور زين 
⎉︙يمكنك استخراج الجلسات الـتالية
⎉︙بايروجرام v1 للميوزك والتليثون الإصدار القديم
⎉︙بايروجرام v2 للميوزك والتليثون الاصدار الجديد
⎉︙تريمكس (تليثون)  للحسابات & للبوتات

⎉︙بواسطـة : [𝗦𝗢𝗨𝗥𝗖𝗘 𝗬𝗢𝗨𝗦𝗘𝗙 ](t.me/j0_oc) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="‹ بـدء إسـتـخـراج جـلـسـة ›", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("𓏺𝗪𝗢𝗥𝗟𝗗 𝗬𝗢𝗨𝗦𝗘𝗙", url="https://t.me/j0_oc"),
                    InlineKeyboardButton("𓏺𝘽𝘼𝙍 𝙔𝙊𝙐𝙎𝙀𝙁", url="https://t.me/L_H_1F")
                ],
                [
                    InlineKeyboardButton("𓏺𝗗𝗘𝗩 𝙔𝙊𝙐𝙎𝙀𝙁", user_id=1688364211)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
