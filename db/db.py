from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from config import DB_USER, DB_PASSWORD, DB_NAME, DB_HOST, DB_PORT

Base = declarative_base()


class Quiz(Base):
    __tablename__ = 'quiz'

    id = Column(Integer, primary_key=True, unique=True)
    prev_ids = Column(Integer, default=None)
    question = Column(String(512), nullable=False)
    answer = Column(String(128), nullable=False)
    created_at = Column(String(32), nullable=False)


engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
