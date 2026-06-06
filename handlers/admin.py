from pyrogram import filters
from config import OWNER_ID

def register_admin(app):

    @app.on_message(filters.command("stats"))
    async def stats(_, message):
        if message.from_user.id != OWNER_ID:
            return
        await message.reply("Statistics module placeholder")

    @app.on_message(filters.command("broadcast"))
    async def broadcast(_, message):
        if message.from_user.id != OWNER_ID:
            return
        await message.reply("Broadcast module placeholder")
