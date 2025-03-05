from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_start_shop = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Telegram бот', callback_data='tg_bot_info')],
                                                          [InlineKeyboardButton(text='Discord бот', callback_data='ds_bot_info')],
                                                          [InlineKeyboardButton(text='Сайт', callback_data='sites_info')],
                                                          [InlineKeyboardButton(text='« Меню', callback_data='first')]])

inline_it_shop_return = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='‹ Назад', callback_data='shop'),
                                                               InlineKeyboardButton(text='« Меню', callback_data='first')]])