from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import register_start
from handlers.admin import register_admin

app = Client(
    "TxtVideoBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_start(app)
register_admin(app)

app.run()
