import asyncio
import os
import logging
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import default_handler, currency_handler

logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=os.getenv('API_TOKEN'))
    dp = Dispatcher()

    dp.include_router(default_handler.router)
    dp.include_router(currency_handler.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
