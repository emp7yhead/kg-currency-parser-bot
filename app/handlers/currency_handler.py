import os
from aiogram import Router
from aiogram.types import Message
from aiogram.filters.text import Text
from utils import TableHandler, parse_url_for_table, update_indexes

URL = os.getenv('URL')

router = Router()


@router.message(Text(text='Get average course', ignore_case=True))
async def send_average_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_average()
    await message.reply(f'{update_indexes(table)}')


@router.message(Text(text='Get best course', ignore_case=True))
async def send_best_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_best_course()
    await message.reply(f'{update_indexes(table)}')


@router.message(Text(text='Get recomended course', ignore_case=True))
async def send_recomended_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_national_bank_course()
    await message.reply(f'{update_indexes(table)}')
