from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_board = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🛒 Каталог', callback_data='to_category')],
                                                    [InlineKeyboardButton(text='💡 Інфо', callback_data='info_start'),
                                                     InlineKeyboardButton(text='🧾 Відгуки', url='t.me/DevSatoshiReviews')]])