from . import keyboard as kb
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums import ChatAction


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Hello', reply_markup=kb.main)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"Hello {message.from_user.username}!\nThis bot is made so that you can convert your file to the extension you need.\nRather, send him your file and press the button you need.")


@router.message(F.document)
async def answer_file(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_DOCUMENT)
    await message.reply(f'you new file')
    
@router.message(F.text == 'PDF')
async def answer_pdf(message: Message):
    await message.answer(text=f'Send your document')

@router.message(F.text == 'DOCX')
async def answer_docx(message: Message):
    await message.answer(text=f'Send your document')

@router.message(F.text == 'PPTX')
async def answer_pptx(message: Message):
    await message.answer(text=f'Send your document')