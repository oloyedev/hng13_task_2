import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

# Try Railway DATABASE_URL first
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    from .config import settings
    password = quote_plus(settings.DB_PASSWORD)
    DATABASE_URL = (
        f"mysql+pymysql://{settings.DB_USERNAME}:{password}"
        f"@{settings.DB_HOST_NAME}:{settings.DB_PORT}/{settings.DB_NAME}"
    )

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
