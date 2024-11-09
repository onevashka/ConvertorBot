import logging
import asyncio
import sys
import os
from config import TOKEN
from aiogram import Bot, Dispatcher
from app.router import router


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


bot = Bot(token=TOKEN)
dp = Dispatcher()
dp.include_router(router=router)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print('Exit')
