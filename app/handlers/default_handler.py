from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards import courses_kb
from handlers.const import GREETING

router = Router()


@router.message(Command(commands=['start']))
async def send_welcome(message: Message):
    await message.reply(
        GREETING,
        reply_markup=courses_kb,
    )
