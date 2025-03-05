import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
import os

from board_for_start import start_board
from shop.board_category_shop import category_board
from shop.crypto.query_crypto.handlers_crypto import router_spread
from shop.it.query_shop.handlers_shop import shop_router
from information.faq_cmd import info_router
from information.board_category_info import board_info
from dotenv import load_dotenv
load_dotenv()

bot = Bot(os.getenv('TG_KEY'))
ds = Dispatcher()
ds.include_router(router_spread)
ds.include_router(shop_router)
ds.include_router(info_router)

@ds.callback_query(F.data == 'first')
async def start_again(callback: CallbackQuery):
    await callback.message.delete()
    input_file = FSInputFile('public/shop_photo.jpg')
    await callback.message.answer_photo(photo=input_file, caption="Вітаємо тебе в магазині Satoshi 🇺🇦\nДе ти зможеш "
                                                                  "придбати бота, сайт та корисні інструменти, пов'язані "
                                                                  "з кріптою \n\n"
                                                                  "Від: <a href='https://t.me/devSatoshimain'>@D.E.V Satoshi</a> 💎\n"
                                                                  "Зв'язок: @ShadowCryps",
                                        parse_mode='HTML', reply_markup=start_board)

@ds.message(CommandStart())
async def start(message: Message):
    input_file = FSInputFile('public/shop_photo.jpg')
    await message.answer_photo(photo=input_file, caption="Вітаємо тебе в магазині Satoshi 🇺🇦\nДе ти зможеш "
                                                                  "придбати бота, сайт та корисні інструменти, пов'язані "
                                                                  "з кріптою \n\n"
                                                                  "Від: <a href='https://t.me/devSatoshimain'>@D.E.V Satoshi</a> 💎\n"
                                                                    "Зв'язок: @ShadowCryps 🛠️",
                                        parse_mode='HTML', reply_markup=start_board)
@ds.callback_query(F.data == "to_category")
async def cmd_to_category(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Оберіть категорію 👇', reply_markup=category_board)

@ds.callback_query(F.data == 'info_start')
async def info_start(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('🚩 Допоміжна інформація', reply_markup=board_info)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await ds.start_polling(bot, drop_pending_updates=True, allowed_updates=[])

if __name__ == '__main__':
    asyncio.run(main())