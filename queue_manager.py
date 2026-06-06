import asyncio

class QueueManager:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def add_task(self, task):
        await self.queue.put(task)

queue_manager = QueueManager()
