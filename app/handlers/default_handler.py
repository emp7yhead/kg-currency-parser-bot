from aiogram import Router
from aiogram.types import Message
from keyboards import courses_kb

from aiogram.filters import Command

router = Router()


@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply(
        "Hi!\nI'm kg_currency_bot.!\nI will help you get in touch with currency cource in KG.",
        reply_markup=courses_kb
    )
