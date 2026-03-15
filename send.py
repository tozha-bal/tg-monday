import asyncio, os, logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pytz

logging.basicConfig(level=logging.INFO)

API_ID   = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION  = os.environ["SESSION"]
GROUP    = os.environ["GROUP"]
MESSAGE  = os.environ["MESSAGE"]

tz = pytz.timezone("Europe/Moscow")
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

async def send_message():
    logging.info("Отправляю...")
    await client.send_message(GROUP, MESSAGE)
    logging.info("Отправлено!")

async def main():
    await client.start()
    logging.info("Авторизован. Жду понедельника...")
    scheduler = AsyncIOScheduler(timezone=tz)
    scheduler.add_job(send_message, "cron", day_of_week="mon", hour=9, minute=0)
    scheduler.start()
    await asyncio.Event().wait()

asyncio.run(main())

