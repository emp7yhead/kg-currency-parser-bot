from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import courses_kb

router = Router()


@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply(
        "Hi!\nI'm kg_currency_bot.!\n\
        I will help you get in touch with \
        currency cource in KG.",
        reply_markup=courses_kb,
    )
