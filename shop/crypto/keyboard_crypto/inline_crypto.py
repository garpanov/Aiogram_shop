from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_board = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Спреди', callback_data='spread')],
                                                     [InlineKeyboardButton(text='Фаст-бот', callback_data='fire_news')],
                                                   [InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_spread = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='💳 Сплатити 💳', callback_data='payment_spread')],
                                                     [InlineKeyboardButton(text='‹ Назад', callback_data='crypto'),
                                                      InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_payment_spread = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='За ⭐️', callback_data='stars_spread')],
                                                              [InlineKeyboardButton(text='USDT 💲', callback_data='usdt_spread')],
                                                              [InlineKeyboardButton(text='‹ Назад', callback_data='spread'),
                                                               InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_spread_stars = InlineKeyboardMarkup(inline_keyboard=([[InlineKeyboardButton(text='Сплатити 1250 ⭐️', pay=True)],
                                                            [InlineKeyboardButton(text='‹ Назад', callback_data='payment_spread'),
                                                             InlineKeyboardButton(text='« Меню', callback_data='first')]]))

board_fire_news = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='💳 Сплатити 💳', callback_data='payment_fire_news')],
                                                     [InlineKeyboardButton(text='‹ Назад', callback_data='crypto'),
                                                      InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_payment_fire_news = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='За ⭐️', callback_data='stars_fire_news')],
                                                              [InlineKeyboardButton(text='USDT 💲', callback_data='usdt_fire_news')],
                                                              [InlineKeyboardButton(text='‹ Назад', callback_data='fire_news'),
                                                               InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_fire_news_stars = InlineKeyboardMarkup(inline_keyboard=([[InlineKeyboardButton(text='Сплатити 820 ⭐️', pay=True)],
                                                            [InlineKeyboardButton(text='‹ Назад', callback_data='payment_fire_news'),
                                                             InlineKeyboardButton(text='« Меню', callback_data='first')]]))
# text='Сплатити 1250 ⭐️', pay=True