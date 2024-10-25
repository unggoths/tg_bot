from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://xintrea:123321@localhost/tgbot"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_connection():
    """Створює нове з'єднання до бази даних."""
    return SessionLocal()  # Повертаємо новий сеанс

def close_connection(conn):
    """Закриває з'єднання до бази даних."""
    if conn:
        conn.close()  # Закриваємо сеанс

async def async_main():
    """Функція для асинхронної ініціалізації бази даних, якщо потрібно."""
    # Додайте вашу асинхронну логіку, якщо це потрібно
    pass
