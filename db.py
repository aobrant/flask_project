import atexit
from sqlalchemy import Column, String, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/advert'

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)


class Element(Base):

    __tablename__ = 'app_notice'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False, unique=True, index=True)
    description = Column(String)
    owner = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


Base.metadata.create_all(bind=engine)