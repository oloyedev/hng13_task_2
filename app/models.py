from .database import Base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, text
from sqlalchemy.sql import func


class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    name = Column(String(100), nullable=False, index=True)
    capital = Column(String(100), nullable=True, index=True)
    region = Column(String(100), nullable=True, index=True)
    population = Column(Integer, nullable=False)

    currency_code = Column(String(10), nullable=True, index=True)
    exchange_rate = Column(Float, nullable=True)
    estimated_gdp = Column(Float, nullable=True)

    flag_url = Column(String(255), nullable=True)

    last_refreshed_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )
