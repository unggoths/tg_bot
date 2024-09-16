import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    bot = Bot(token='7545582976:AAFrEdvIOkIn_tzE36JAEeHkf_L0jN8_J5o')
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is disabled')

