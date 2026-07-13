from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker,Session
from typing import Generator

DATABASE_URL = (
    "postgresql+psycogp://postgres:tusharjain@localhost:5432/RoundOneDB"
)

engine = create_engine(
    DATABASE_URL,
    pool_size=12,
    max_overflow=8,
    pool_pre_ping=True,
    pool_recycle=1800
)


