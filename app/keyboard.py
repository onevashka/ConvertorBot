from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


source_format = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(text='PDF')],
    [KeyboardButton(text='DOCX')],
    [KeyboardButton(text='PPTX')],

    resize_keyboard=True,
    input_field_placeholder='Выберите формат из которого нужно будет конвертировать!'

])

target_format = ReplyKeyboardMarkup(keyboard=[

    [KeyboardButton(text='PDF')],
    [KeyboardButton(text='DOCX')],
    [KeyboardButton(text='PPTX')],

    resize_keyboard=True,
    input_field_placeholder='Выберите формат в который нужно будет конвертировать!'



])