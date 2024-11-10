from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(text='PDF')],
    [KeyboardButton(text='DOCX')],
    [KeyboardButton(text='PPTX')],

    resize_keyboard=true,
    input_field_placeholder='Выберите формат'

])