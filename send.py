import asyncio, os
from telethon import TelegramClient
from telethon.sessions import StringSession

API_ID   = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION  = os.environ["SESSION"]
GROUP    = int(os.environ["GROUP"])
MESSAGE  = os.environ["MESSAGE"]

async def main():
    async with TelegramClient(StringSession(SESSION), API_ID, API_HASH) as client:
        await client.send_message(GROUP, MESSAGE)
        print("Отправлено!")

asyncio.run(main())
