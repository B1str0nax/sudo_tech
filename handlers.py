from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать, выберете действие: ",
                         reply_markup=kb.main)

@router.message(F.text == "Добавление сотрудника")
async def main_menu(message: Message):
    await message.answer('Функция в разработке!...')
