from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper_funcs.utils import not_subscribed
from config import FORCE_SUB

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢 ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**What Are You Trying To Do, Mate?. ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
