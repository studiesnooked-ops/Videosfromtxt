from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import register_start
from handlers.admin import register_admin

bot = Client(
    "TxtVideoBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def run_bot():
    register_start(bot)
    register_admin(bot)
    bot.run()
