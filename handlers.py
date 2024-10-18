from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import app.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привіт!👋 \n'
                         'Ласкаво просимо до нашого ріелторського бота! 🏡\n'
                         'Ми тут, щоб допомогти вам знайти ідеальне житло або продати вашу нерухомість.\n'
                         'Чим можемо допомогти сьогодні? 🤔', reply_markup=kb.main)

@router.message(F.text == '💬 Допомога')
async def cmd_help(message: Message):
    await message.answer('💬 Потрібна допомога? Ми завжди поруч! 🦸\n'
                         'Напишіть, з якою проблемою ви зіткнулися, і ми з радістю вам допоможемо. 🤝')
# Купівля нерухомості

@router.message(F.text == '💰 Купівля нерухомості')
async def buy(message: Message):
    await message.answer('🏡 Купівля нерухомості — це серйозний крок!\n'
                         'Оберіть, що саме вас цікавить:', reply_markup=kb.buy)

@router.callback_query(F.data == 'buy_apartment')
async def buy_apartment(callback: CallbackQuery):
    await callback.message.answer('🏙 Ви шукаєте квартиру? Прекрасний вибір! \n'
                                  'Скільки кімнат ви бажаєте мати? 🛏:', reply_markup=kb.apartment_type)

@router.callback_query(F.data.in_(['apartment_1', 'apartment_2', 'apartment_3', 'apartment_4', 'apartment_studio']))
async def apartment_rooms(callback: CallbackQuery):
    await callback.message.answer('✅ Гаразд! Ви обрали квартиру. \n'
                                  '📍 Тепер оберіть район, який вам підходить:', reply_markup=kb.district)

@router.callback_query(F.data == 'buy_house')
async def buy_house(callback: CallbackQuery):
    await callback.message.answer('🏠 Оберіть бажаний тип будинку:\n'
                                  'Скільки поверхів має бути у вашому домі? 🏢', reply_markup=kb.house_floor)

@router.callback_query(F.data.in_(['one_floor', 'two_floors', 'three_floors']))
async def select_house_type(callback: CallbackQuery):
    await callback.message.answer('✨ Чудово! Ви обрали тип будинку. \n'
                                  '🏠 Скільки кімнат вам потрібно? 🛏', reply_markup=kb.house_rooms)

@router.callback_query(F.data.in_(['one_room', 'two_rooms', 'three_rooms_or_more']))
async def select_house_rooms(callback: CallbackQuery):
    await callback.message.answer('📍 Чудовий вибір! Кількість кімнат обрано. \n'
                                  '🏙 Тепер оберіть бажаний район міста:', reply_markup=kb.district)
# Закінчується купівля нерухомості

# Оренда житла
@router.message(F.text == '🔑 Оренда житла')
async def rent(message: Message):
    await message.answer('🔑 Оренда житла — це вигідне рішення! \n'
                         'Ви шукаєте квартиру чи будинок? 🏘', reply_markup=kb.rent)

@router.callback_query(F.data == 'rent_apartment')
async def rent_apartment(callback: CallbackQuery):
    await callback.message.answer('🏙 Оренда квартири? Який тип квартири вас цікавить? 🛏:', reply_markup=kb.apartment_type)

@router.callback_query(F.data.in_(['apartment_1', 'apartment_2', 'apartment_3', 'apartment_4', 'apartment_studio']))
async def select_apartment_rooms(callback: CallbackQuery):
    await callback.message.answer('✅ Гаразд! Ви обрали тип квартири. \n'
                                  '📍 Тепер оберіть район для оренди:', reply_markup=kb.district)

@router.callback_query(F.data == 'rent_house')
async def rent_house(callback: CallbackQuery):
    await callback.message.answer('🏠 Оренда будинку? Прекрасно! Скільки поверхів вам потрібно? 🏢', reply_markup=kb.house_floor)

@router.callback_query(F.data.in_(['one_floor', 'two_floors', 'three_floors']))
async def select_house_floors(callback: CallbackQuery):
    await callback.message.answer('✅ Ви обрали кількість поверхів у будинку. \n'
                                  '📍 Тепер оберіть бажаний район для оренди:', reply_markup=kb.district)
# Закінчується оренда житла

# Продаж нерухомості
@router.message(F.text == '🏷️ Продаж нерухомості')
async def buy(message: Message):
    await message.answer('💵 Продаж нерухомості — це серйозний крок!\n'
                         'Оберіть, що саме ви плануєте продавати:', reply_markup=kb.sell)
@router.callback_query(F.data == 'sell_apartment')
async def sell_apartment(callback: CallbackQuery):
    await callback.message.answer('🏙 Ви хочете продати квартиру? Чудово!\n'
                                  'Скільки кімнат має ваша квартира? 🛏:', reply_markup=kb.apartment_type)

@router.callback_query(F.data.in_(['apartment_1', 'apartment_2', 'apartment_3', 'apartment_4', 'apartment_studio']))
async def sell_apartment_rooms(callback: CallbackQuery):
    await callback.message.answer('✅ Ви обрали квартиру для продажу.\n'
                                  '📍 Тепер оберіть район, в якому знаходиться квартира:', reply_markup=kb.district)

@router.callback_query(F.data == 'sell_house')
async def sell_house(callback: CallbackQuery):
    await callback.message.answer('🏠 Ви хочете продати будинок? Прекрасно! Скільки поверхів у вашому будинку? 🏢', reply_markup=kb.house_floor)

@router.callback_query(F.data.in_(['one_floor', 'two_floors', 'three_floors']))
async def select_sell_house_type(callback: CallbackQuery):
    await callback.message.answer('✨ Чудово! Ви обрали тип будинку. \n'
                                  '🏠 Скільки кімнат у вашому будинку? 🛏', reply_markup=kb.house_rooms)

@router.callback_query(F.data.in_(['one_room', 'two_rooms', 'three_rooms_or_more']))
async def select_sell_house_rooms(callback: CallbackQuery):
    await callback.message.answer('✅ Чудовий вибір! Кількість кімнат обрана. \n'
                                  '📍 Тепер оберіть район, в якому знаходиться ваш будинок:', reply_markup=kb.district)
