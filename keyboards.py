from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🏷️ Продаж нерухомості')],
        [KeyboardButton(text='💰 Купівля нерухомості')],
        [KeyboardButton(text='🔑 Оренда житла'),
         KeyboardButton(text='💬 Допомога')]
    ],

    resize_keyboard=True,
    input_field_placeholder='Оберіть пункт меню ...'
)

buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🏙 Купівля квартири', callback_data='buy_apartment')],
        [InlineKeyboardButton(text='🏠 Купівля будинку', callback_data='buy_house')]
    ]
)

sell = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🏙 Продаж квартири', callback_data='sell_apartment')],
        [InlineKeyboardButton(text='🏠 Продаж будинку', callback_data='sell_house')]
    ]
)

rent = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🏡 Оренда будинку', callback_data='rent_house')],
        [InlineKeyboardButton(text='🔑 Оренда квартири', callback_data='rent_apartment')]
    ]
)

district = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Сихівський район 🌳', callback_data='district_Sihiv')],
        [InlineKeyboardButton(text='Галицький район 🏰', callback_data='district_Halych')],
        [InlineKeyboardButton(text='Залізничний район 🚉', callback_data='district_Zaliz')],
        [InlineKeyboardButton(text='Франківський район 🏞️', callback_data='district_Franko')],
        [InlineKeyboardButton(text='Личаківський район 🍀', callback_data='district_Luchakiv')],
        [InlineKeyboardButton(text='Шевченківський район 🌆', callback_data='district_Shevchenk')],
        [InlineKeyboardButton(text='Будь-який район 🎲', callback_data='district_random')]
    ]
)

apartment_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='1-кім квартира', callback_data='apartment_1')],
        [InlineKeyboardButton(text='2-кім квартира', callback_data='apartment_2')],
        [InlineKeyboardButton(text='3-кім квартира', callback_data='apartment_3')],
        [InlineKeyboardButton(text='4-кім квартира', callback_data='apartment_4')],
        [InlineKeyboardButton(text='Квартира-студія', callback_data='apartment_studio')]
    ]
)

house_floor = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Один поверх', callback_data='one_floor')],
        [InlineKeyboardButton(text='Два поверхи', callback_data='two_floors')],
        [InlineKeyboardButton(text='Три поверхи', callback_data='three_floors')]
    ]
)

house_rooms = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Одна кімната', callback_data='one_room')],
        [InlineKeyboardButton(text='Дві кімнати', callback_data='two_rooms')],
        [InlineKeyboardButton(text='Три кімнати і більше', callback_data='three_rooms_or_more')]
    ]
)

