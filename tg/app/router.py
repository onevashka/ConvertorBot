from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"Hello {message.from_user.username}!\nThis bot is made so that you can convert your file to the extension you need.\nRather, send him your file and press the button you need.")