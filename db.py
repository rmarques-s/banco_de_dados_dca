from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/biblioteca_db?client_encoding=latin1"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)