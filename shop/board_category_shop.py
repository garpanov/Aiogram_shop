from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

category_board = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Технічні додатки 🧑‍💻', callback_data='shop_start')],
                                                       [InlineKeyboardButton(text='Кріпто інструменти 🤖', callback_data='crypto_start')],
                                                       [InlineKeyboardButton(text='‹ Назад', callback_data='first')]])