
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router  # Правильний імпорт з app
from database.models import create_connection, close_connection  # Змінено на правильний імпорт

async def main():
    conn = create_connection()  # Викликаємо функцію для створення з'єднання
    try:
        bot = Bot(token='7545582976:AAFrEdvIOkIn_tzE36JAEeHkf_L0jN8_J5o')  # Замініть на ваш токен
        dp = Dispatcher()

        dp.include_router(router)
        await dp.start_polling(bot)
    finally:
        close_connection(conn)  # Закриваємо з'єднання

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot is disabled')
