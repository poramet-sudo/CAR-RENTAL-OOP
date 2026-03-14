from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ใช้ฐานข้อมูล SQLite ชื่อ car_rental.db (ไฟล์จะถูกสร้างขึ้นมาอัตโนมัติ)
SQLALCHEMY_DATABASE_URL = "sqlite:///./car_rental.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()