from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

board_info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='📍 FAQ', callback_data='faq')],
                                                   [InlineKeyboardButton(text='☎️ Підтримка', callback_data='support')],
                                                   [InlineKeyboardButton(text='📝 Умови обслуговування', url='https://telegra.ph/Umovi-obslugovuvannya-Terms-of-Service-03-02')],
                                                   [InlineKeyboardButton(text='‹ Меню', callback_data='first')]])

board_return_info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='‹ Назад', callback_data='info_return_info'),
                                                           InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_support_info = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='📍 FAQ', callback_data='faq')],
                                                           [InlineKeyboardButton(text='‹ Назад', callback_data='info_return_info'),
                                                            InlineKeyboardButton(text='« Меню', callback_data='first')]])