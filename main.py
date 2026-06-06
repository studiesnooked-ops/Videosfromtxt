from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.start import register_start
from handlers.admin import register_admin
import threading

# -------------------
# Flask web server (REQUIRED for Render web service)
# -------------------
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running"

# -------------------
# Telegram bot
# -------------------
bot = Client(
    "TxtVideoBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_start(bot)
register_admin(bot)

def run_bot():
    bot.run()

# Run bot in background thread
threading.Thread(target=run_bot).start()

# Run web server (IMPORTANT - keeps Render alive)
app_web.run(host="0.0.0.0", port=10000)
