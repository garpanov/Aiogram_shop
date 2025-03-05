from aiogram import Router, F
from aiogram.types import CallbackQuery, LabeledPrice, PreCheckoutQuery, Message

from shop.crypto.keyboard_crypto.inline_crypto import *

router_spread = Router()

@router_spread.callback_query(F.data == 'crypto_start')
async def cmd_crypto_start(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Що вас цікавить?', reply_markup=menu_board)

@router_spread.callback_query(F.data == 'crypto')
async def cmd_crypto(callback: CallbackQuery):
	await callback.message.edit_text('Що вас цікавить?', reply_markup=menu_board)

@router_spread.callback_query(F.data == 'spread')
async def cmd_spread(callback: CallbackQuery):
	await callback.message.edit_text("Бот, який постійно аналізує ціни монет на DEX біржах і, якщо знаходить 'спред', "
	                                 "надсилає повідомлення про цю пару для подальшого арбітражу 📈\n\n2️⃣9️⃣💲 / міс.\n\n",
	                                 reply_markup=board_spread)

@router_spread.callback_query(F.data == 'payment_spread')
async def cmd_payment_spread(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Виберіть спосіб сплати 👇', reply_markup=board_payment_spread)

@router_spread.callback_query(F.data == 'stars_spread')
async def cmd_start_spread(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer_invoice(title='Підписка на спред бота',
	                                      description='Сплата за підписку на місяць, в розмірі 1250 ⭐️',
	                                      payload='stars_spread_accept',
	                                      provider_token='',
	                                      currency='XTR',
	                                      prices=[LabeledPrice(label='XTR', amount=1250)],
	                                      reply_markup=board_spread_stars)

@router_spread.pre_checkout_query()
async def cmd_spread_pre_checkout(pre_checkout_query: PreCheckoutQuery):
	await pre_checkout_query.answer(ok=True)

@router_spread.message(F.successful_payment)
async def cmd_succesfful(message: Message):
	playload = message.successful_payment.invoice_payload
	if playload == 'stars_spread_accept':
		await message.answer(text='Дякуємо за купівлю підписки на spread bot \nДля подальших дій зверніться до @ShadowCryps')
	elif playload == 'stars_fire_news_accept':
		await message.answer(text='Дякуємо за покупку fire news bot \nДля подальших дій зверніться до @ShadowCryps')

@router_spread.callback_query(F.data == 'fire_news')
async def cmd_fire_news(callback: CallbackQuery):
	await callback.message.edit_text("Автоматизований бот новин для X видатних людей (Ілон Маск, Трамп тощо), який "
	                                 "відслідковує згадки криптомонет або інших слів, пов'язаних з кріптою 🤖, а "
	                                 "також стежить за великими переведеннями між гаманцями. 👀 Це допоможе швидко "
	                                 "відреагувати на події\n\n1️⃣9️⃣💲 / міс.", reply_markup=board_fire_news)

@router_spread.callback_query(F.data == 'payment_fire_news')
async def cmd_payment_news(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer('Виберіть спосіб сплати 👇', reply_markup=board_payment_fire_news)

@router_spread.callback_query(F.data == 'stars_fire_news')
async def cmd_start_news(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer_invoice(title='Підписка на спред бота',
	                                      description='Сплата за підписку на місяць, в розмірі 820 ⭐️',
	                                      payload='stars_fire_news_accept',
	                                      provider_token='',
	                                      currency='XTR',
	                                      prices=[LabeledPrice(label='XTR', amount=820)],
	                                      reply_markup=board_fire_news_stars)