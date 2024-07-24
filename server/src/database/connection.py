from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.env import env

engine = create_engine(env.DATABASE_URL)


get_session = sessionmaker(engine, class_=Session)
