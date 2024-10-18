from sqlalchemy import BIGINT, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')
async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger, unique=True)
    # Відношення для зв'язку з таблицею PropertySelection
    selections = relationship("PropertySelection", back_populates="user")


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Floor(Base):
    __tablename__ = 'floors'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String)


class PropertyType(Base):
    """Тип нерухомості: квартира, будинок тощо"""
    __tablename__ = 'property_types'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class District(Base):
    """Райони міста"""
    __tablename__ = 'districts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class RoomCount(Base):
    """Кількість кімнат у нерухомості"""
    __tablename__ = 'room_counts'

    id: Mapped[int] = mapped_column(primary_key=True)
    count: Mapped[int] = mapped_column(BIGINT)


class PropertySelection(Base):
    """Вибір користувача щодо нерухомості (купівля, оренда, продаж)"""
    __tablename__ = 'property_selections'

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship("User", back_populates="selections")

    property_type_id: Mapped[int] = mapped_column(ForeignKey('property_types.id'))
    property_type = relationship("PropertyType")

    room_count_id: Mapped[int] = mapped_column(ForeignKey('room_counts.id'))
    room_count = relationship("RoomCount")

    floor_id: Mapped[int] = mapped_column(ForeignKey('floors.id'))
    floor = relationship("Floor")

    district_id: Mapped[int] = mapped_column(ForeignKey('districts.id'))
    district = relationship("District")

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category = relationship("Category")

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
