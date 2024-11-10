import logging
import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.router import router


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print('Exit')
