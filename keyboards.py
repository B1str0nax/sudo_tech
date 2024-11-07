from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)



main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавление сотрудника', callback_data='add_worker'),
     InlineKeyboardButton(text='Добавление отдела', callback_data='add_department')],
    [InlineKeyboardButton(text='Структура компании', callback_data='company')],
    [InlineKeyboardButton(text='Увольнение сотрудника', callback_data='remove_worker')],
])
