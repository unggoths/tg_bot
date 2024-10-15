from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привіт!👋 \n'
                         'Вітаємо вас у нашому ріелторському боті! 🏡'
                         'Ми тут, щоб допомогти вам знайти ідеальне житло або продати вашу нерухомість.')

@router.message(F.text == '💬 Допомога')
async def cmd_help(message: Message):
    await message.answer('💬 Ви звернулись за допомогою. \n'
                         'З чим саме у вас стались проблеми? 🧐')
# Купівля нерухомості
@router.message(F.text == '💰 Купівля нерухомості')
async def buy(message: Message):
    await message.answer('Виберіть зі списку:', reply_markup=kb.buy)

@router.message(F.data == 'buy_apartment')
async def buy_apartment(callback: CallbackQuery):
    await callback.message.answer('Вкажість кількість кімнат у квартирі:', reply_markup=kb.apartment_type)

@router.callback_query(F.data == 'buy_apartment')
async def buy_apartment(callback: CallbackQuery):
    await callback.message.answer('Оберіть бажаний район міста:', reply_markup=kb.district)

@router.callback_query(F.data == 'buy_house')
async def buy_house(callback: CallbackQuery):
    await callback.message.answer('Оберіть бажаний тип будинку:', reply_markup=kb.house_floor)

@router.callback_query(F.data.in_(['one_floor', 'two_floors', 'three_floors']))
async def select_house_type(callback: CallbackQuery):
    await callback.message.answer('Оберіть кількість кімнат у будинку:', reply_markup=kb.house_rooms)
#Закінчується купівля нерухомості

#Оренда житла
@router.callback_query(F.data == 'rent_apartment')
async def rent_apartment(callback: CallbackQuery):
    await callback.message.answer('Будь ласка, оберіть тип квартири:', reply_markup=kb.apartment_type)

@router.callback_query(F.data == 'rent_house')
async def rent_house(callback: CallbackQuery):
    await callback.message.answer('Будь ласка, вкажіть кількість поверхів у будинку:', reply_markup=kb.house_floor)
#Закінчується оренда житла