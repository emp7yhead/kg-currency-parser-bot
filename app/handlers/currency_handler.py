from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from tables import TableHandler, parse_url_for_table, update_indexes

URL = 'https://valuta.kg/'

router = Router()


@router.message(
    Command(commands=['average'])
)
async def send_average_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_average()
    table_with_indexes = update_indexes(table)
    await message.reply(f'{table_with_indexes}')


@router.message(
    Command(commands=['best'])
)
async def send_best_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_best_course()
    table_with_indexes = update_indexes(table)
    await message.reply(f'{table_with_indexes}')


@router.message(
    Command(commands=['recommended'])
)
async def send_recommended_table(message: Message):
    parsed_tables = parse_url_for_table(URL)
    table = TableHandler(parsed_tables).get_national_bank_course()
    table_with_indexes = update_indexes(table)
    await message.reply(f'{table_with_indexes}')
