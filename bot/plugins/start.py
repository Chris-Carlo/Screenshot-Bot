from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton

from ..config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(Filters.private & Filters.command("start"))
async def start(c, m):
    
    if not await c.db.is_user_exist(m.chat.id):
        await c.db.add_user(m.chat.id)
        await c.send_message(
            Config.LOG_CHANNEL,
            f"New User [{m.from_user.first_name}](tg://user?id={m.chat.id}) started."
        )
    
    await m.reply_text(
        text=f"Hi there {m.from_user.first_name}.\n\nI am Screenshot Generator Bot. I can provide screenshots from your video files with out downloading the entire file. For more details click /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Group', url='https://t.me/CinemaCompanyGroup'),
                    InlineKeyboardButton('Channel', url='https://t.me/CCALLMOVIESCHANNEL')
                ],
                [
                    InlineKeyboardButton('Support', url='https://t.me/darklester'),
                    InlineKeyboardButton('Creator', url='https://t.me/Chris_Carlo')
                ]
            ]
        )
    )
