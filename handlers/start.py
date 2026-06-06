from pyrogram import filters

def register_start(app):
    @app.on_message(filters.command("start"))
    async def start(_, message):
        await message.reply("Send a TXT file containing video URLs.")
