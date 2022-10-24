from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_avg = KeyboardButton(
    text='Get average course',
)
button_best = KeyboardButton(
    text='Get best course',
)
button_recomended = KeyboardButton(
    text='Get recomended course',
)

courses_kb = ReplyKeyboardMarkup(
    keyboard=[
        [button_avg, button_best, button_recomended],
    ],
    resize_keyboard=True,
)
