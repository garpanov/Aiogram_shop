from aiogram import Router, F
from aiogram.types import CallbackQuery

from shop.education.keyboard_education.inline_education import *

router_education = Router()

@router_education.callback_query(F.data == 'education_start')
async def cmd_education_start(callback: CallbackQuery):
	await callback.message.delete()
	await callback.message.answer("Materials (безкоштовно, для ознайомлення)", reply_markup=board_start_education)

@router_education.callback_query(F.data == 'return_education')
async def cmd_education_return(callback: CallbackQuery):
	await callback.message.edit_text("Materials (безкоштовно, для ознайомлення)", reply_markup=board_start_education)

@router_education.callback_query(F.data == 'education_bots')
async def cmd_education_bots(callback: CallbackQuery):
	await callback.message.edit_text('🤖 Чи замислювались ви, як працюють Telegram/Discord боти під капотом '
	                                 '(з технічної сторони)? \nУ цьому розділі коротко та простими словами розписана '
	                                 'їх поверхнева робота 🚀\n\nhttps://telegra.ph/YAK-PRACYUYUT-BOTI-V-TELEGRAM-І-DISCORD-03-12',
	                                 reply_markup=board_return_education)

@router_education.callback_query(F.data == 'education_sites')
async def cmd_education_sites(callback: CallbackQuery):
	await callback.message.edit_text("🔧 Як працює сайт?\n🛒 Як сайт знає, що ви хочете купити?\n📈 Що таке SEO і чому "
	                                 "ваш сайт має бути оптимізований для нього?\n\nВідповіді на ці запитання ви "
	                                 "дізнаєтесь вже в цьому розділі!\nhttps://telegra.ph/Vnutrіshnya-kuhnya-sajta-03-12 📚",
	                                 reply_markup=board_return_education)

@router_education.callback_query(F.data == 'education_scraping')
async def cmd_education_scraping(callback: CallbackQuery):
	await callback.message.edit_text("💡 Дізнайтесь, як автоматизовано збирати інформацію з інтернету, що для цього "
	                                 "потрібно і як ці дані можуть стати корисними для вашого сайту або бізнесу🌐\n\n"
	                                 "https://telegra.ph/VEB-SKRAPІNG-ZSEREDINI-03-12",
	                                 reply_markup=board_return_education)

@router_education.callback_query(F.data == 'education_blockchain')
async def cmd_education_blockchain(callback: CallbackQuery):
	await callback.message.edit_text("🏆 Кріпта, децентралізація, прозорість і безпека — це все про блокчейн\n"
	                                 "Як насправді працює концепт документа (whitepaper 📜)?\n\n"
	                                 "https://telegra.ph/TEHNІCHNIJ-BІK-BLOKCHEJNU-03-12",
	                                 reply_markup=board_return_education)