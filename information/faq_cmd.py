from aiogram import Router, F
from aiogram.types import CallbackQuery

from information.board_category_info import board_info, board_return_info, board_support_info

info_router = Router()

@info_router.callback_query(F.data == 'info_return_info')
async def cmd_info_return(callback: CallbackQuery):
	await callback.message.edit_text('🚩 Допоміжна інформація', reply_markup=board_info)

@info_router.callback_query(F.data == 'faq')
async def cmd_faq(callback: CallbackQuery):
	await callback.message.edit_text('Список <b>FAQ</b> ❗\n\n<b>1. Які методи оплати приймаються?</b>\n'
	                                 'Ми надаємо можливість здійснити оплату тільки за допомогою USDT\n\n'
	                                 '2. <b>Чи включає покупка технічну підтримку та оновлення продукту?</b>\n'
	                                 'Ми надаємо безкоштовну технічну підтримку у разі виникнення технічних проблем '
	                                 '(багів), що сталися через нашу необережність. Оновлення продукту проводиться за '
	                                 'додаткову плату.\n\n'
	                                 '3. <b>Чи є знижки при купівлі кількох продуктів?</b>\nТак, знижка залежатиме від '
	                                 'обсягу замовлення.\n\n'
	                                 '4. <b>Чи можу я отримати повернення коштів?</b>\nПовернення коштів можливе, якщо '
	                                 'розробка продукту ще не розпочалась.\n\n'
	                                 '5. <b>Скільки часу займає розробка?</b>\nЧас розробки залежить від обсягу продукту '
	                                 'та складності функціоналу. Зазвичай, розробка Telegram або Discord ботів займає '
	                                 'до 7 днів. У той час як розробка сайтів може тривати до трьох тижнів, в залежності від '
	                                 'вимог і складності дизайну чи інтеграцій.',
	                                 reply_markup=board_return_info, parse_mode='HTML')

@info_router.callback_query(F.data == 'support')
async def cmd_support(callback: CallbackQuery):
	await callback.message.edit_text('❗ Переконайтесь, що вашого питання немає в <b>FAQ</b>\n\nЯкщо у вас виникли питання або '
	                                 'проблеми, ви завжди можете звернутися до нашого адміна, і ми з радістю вам '
	                                 'допоможемо вирішити всі питання: @Garpanov', reply_markup=board_support_info, parse_mode='HTML')