from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

board_start_education = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='🌟 TG/DS бот під капотом 🌟',
                                                                                    callback_data='education_bots')],
                                                              [InlineKeyboardButton(text='🔥 Внутрішня кухня сайта 🔥',
                                                                                    callback_data='education_sites')],
                                                              [InlineKeyboardButton(text='🎁 Веб-скрапінг зсередини 🎁',
                                                                                    callback_data='education_scraping')],
                                                              [InlineKeyboardButton(text='🧬 Технічний бік блокчейну 🧬',
                                                                                    callback_data='education_blockchain')],
                                                              [InlineKeyboardButton(text='‹ Назад',
                                                                                    callback_data='to_category'),
                                                               InlineKeyboardButton(text='« Меню', callback_data='first')]])

board_return_education = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='‹ Назад',
                                                                                     callback_data='return_education'),
                                                               InlineKeyboardButton(text='« Меню', callback_data='first')]])