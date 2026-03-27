# Conexão com o banco de dados
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# URL do banco de dados (ajuste conforme necessário)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")

engine = create_engine(
	DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
