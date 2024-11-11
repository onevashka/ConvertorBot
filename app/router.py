from . import keyboard as kb
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router, F
from aiogram.enums import ChatAction
from .services import DOCX
from .finite_state_machine import ConvertState
from aiogram.fsm.context import FSMContext


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(text='Hello', reply_markup=kb.source_format)
    await state.set_state(ConvertState.choose_source_format)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(f"Hello {message.from_user.username}!\nThis bot is made so that you can convert your file to the extension you need.\nRather, send him your file and press the button you need.")


@router.message(F.document)
async def answer_file(message: Message):
    await message.bot.send_chat_action(chat_id=message.from_user.id,
                                        action=ChatAction.UPLOAD_DOCUMENT)
    await message.reply(f'you new file')


@router.message(F.text.in_({'PDF','DOCX','PPTX'}), ConvertState.choose_source_format)
async def choose_source_format(message: Message, state: FSMContext):
    await state.update_data(source_format=message.text)
    await message.answer(f'You choose source format {message.text}')
    await state.set_state(ConvertState.choose_target_format)

@router.message(F.text.in_({'PDF','DOCX','PPTX'}), ConvertState.choose_target_format)
async def choose_target_format(message: Message, state: FSMContext):
    await state.update_data(target_format=message.text)
    await message.answer(f'You choose target format {message.text}')
    await state.set_state(ConvertState.wait_for_state)

@router.message(F.document, ConvertState.wait_for_state)
async def wait_for_state(message: Message, state: FSMContext):
    user_data = await state.get_data()

    source_format = user_data.get('source_format')
    target_format = user_data.get('target_format')
    document = message.document

    file_path = await document.download(destination=f'.\\document\\{document.file_name}')

    if source_format == 'DOCX':
        if target_format == 'PDF':
            pass
        elif target_format == 'PPTX':
            pass
    elif source_format == 'PDF':
        if target_format == 'DOCX':
            pass
        elif target_format == 'PPTX':
            pass
    elif source_format == 'PPTX':
        if target_format == 'DOCX':
            pass
        elif target_format == 'PDF':
            pass

    await state.clear()
    await message.answer("Conversion complete! You can start a new conversion anytime by choosing the formats again.")

