import asyncio
import ssl
import sys

from aiogram.utils.executor import start_webhook
from aiohttp import web

import aiogram
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app, SendMessage
from aiogram.types import ChatType, ParseMode, ContentTypes
from aiogram.utils.markdown import hbold, bold, text, link
TOKEN = '6619757261:AAH6MTKIObecDWDdsaYkpzRivFcCzfrs0To'
WEBHOOK_HOST = 'https://08a4-178-218-201-17.ngrok-free.app'  # Domain name or IP addres which your bot is located.
WEBHOOK_PORT = 80  # Telegram Bot API allows only for usage next ports: 443, 80, 88 or 8443
WEBHOOK_URL_PATH = '/webhook'  # Part of URL
WEBHOOK_URL = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3002

loop = asyncio.get_event_loop()
bot = Bot(TOKEN, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

async def on_startup(app):
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()

        await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_URL_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

