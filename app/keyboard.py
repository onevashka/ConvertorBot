from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура для выбора исходного формата
source_format = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='PDF')],
        [KeyboardButton(text='DOCX')],
        [KeyboardButton(text='PPTX')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите формат из которого нужно будет конвертировать!'
)

# Клавиатура для выбора целевого формата
target_format = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='PDF')],
        [KeyboardButton(text='DOCX')],
        [KeyboardButton(text='PPTX')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите формат в который нужно будет конвертировать!'
)
