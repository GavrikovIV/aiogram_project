
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина',callback_data='basket'), InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])
#resize_keyboard=True,
#input_message_content='Выберете пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube',
                          url='https://www.youtube.com/watch?v=')]
])

cars = ['Tesla', 'Mercedes', 'BMW']

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
    return keyboard.adjust(2).as_markup()

# async def inline_cars():
#    keyboard = ReplyKeyboardBuilder()
#    for car in cars:
#        keyboard.add(KeyboardButton(text=car))
#        return keyboard.adjust(2).as_markup()

