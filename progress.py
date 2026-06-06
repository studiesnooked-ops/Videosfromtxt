import time

async def progress(current, total):
    percent = round(current * 100 / total, 2) if total else 0
    return f"{percent}%"
