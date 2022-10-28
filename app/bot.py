import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from handlers import currency_handler, default_handler

logging.basicConfig(level=logging.DEBUG)


async def main():
    bot = Bot(token=os.getenv('API_TOKEN'))
    dp = Dispatcher()

    dp.include_router(default_handler.router)
    dp.include_router(currency_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
