from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command


import keyboards as kb

router = Router()

@router.callback_query(F.data == 'back')
@router.message(CommandStart())
async def cmd_start(message: Message):
    if isinstance(message, Message):
        await message.answer("Добро пожаловать, выберете действие: ",
                            reply_markup=kb.main)
    else:
        await message.answer('')
        await message.message.delete()
        await message.message.answer("Добро пожаловать, выберете действие: ",
                            reply_markup=kb.main)



@router.message(F.text == 'Структура компании')
async def company_department(message: Message):
    await message.answer('Выберете отдел: ',
                         reply_markup=await kb.company_department_builder())

@router.callback_query(F.data.startswith('dep_'))
async def company_department_show(callback: CallbackQuery):
    await callback.answer('Вы выбрали пункт')
    await callback.message.answer(f'Вы выбрали {callback.data}',
                                  reply_markup=ReplyKeyboardRemove())