from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Добавление сотрудника'),
     KeyboardButton(text='Добавление отдела')],
    [KeyboardButton(text='Структура компании')],
    [KeyboardButton(text='Увольнение сотрудника')],
])

company_department = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Директорат', callback_data='dep_Директорат')],
    [InlineKeyboardButton(text='Юристы', callback_data='dep_Юристы')],
    [InlineKeyboardButton(text='Бухгалтерия', callback_data='dep_Бухгалтерия')],
    [InlineKeyboardButton(text='ПЕО', callback_data='dep_ПЕО')],
    [InlineKeyboardButton(text='Менеджеры', callback_data='dep_Менеджеры')],
    [InlineKeyboardButton(text='ПТО', callback_data='dep_ПТО')],
    [InlineKeyboardButton(text='МТО', callback_data='dep_МТО')],
    [InlineKeyboardButton(text='IT', callback_data='dep_IT')],
])

async def company_department_builder():
    keyboard = InlineKeyboardBuilder()
    departments = {1: "Directorate", 2: "Uristi", 3: "Buh", 4: "Peo", 5: "Manager", 6:"PTO", 7: "MTO", 8: "IT"}
    for department_id, department in departments.items():
        keyboard.add(InlineKeyboardButton(text=department, callback_data=f'dep_{department_id}'))
    keyboard.add(InlineKeyboardButton(text='На главную', callback_data=f'back'))
    return keyboard.adjust(2).as_markup()
