import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base  # noqa: F401


DB_URL = os.environ.get("DATABASE_CONN_STRING")

engine = create_engine(DB_URL, echo=True)  # type: ignore
Session = sessionmaker(bind=engine)
