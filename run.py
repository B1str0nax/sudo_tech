import asyncio
from aiogram import Bot, Dispatcher

from handlers import router



async def main():
    bot = Bot(token='7367933630:AAFMJEzWJ56aD8IAb3t5CSzuiIPpS-EgYls')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')