import logging
import sys
import os
import asyncio
from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"Hello {message.from_user.username}!\nThis bot is made so that you can convert your file to the extension you need.\nRather, send him your file and press the button you need.")

async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except:
        print('Exit')
