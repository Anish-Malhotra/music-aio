from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True)
    encrypted_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())
