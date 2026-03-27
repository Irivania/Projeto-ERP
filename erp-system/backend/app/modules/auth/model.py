# model.py: Define os modelos de dados (banco de dados) do módulo de autenticação.

from sqlalchemy import Column, Integer, String
from app.database.base import Base

class User(Base):
	__tablename__ = "users"
	id = Column(Integer, primary_key=True)
	username = Column(String, unique=True, index=True)
	senha_hash = Column(String)
	role = Column(String, default="user")  # user ou admin
	consentimento = Column(Integer, default=0)  # 0 = não, 1 = sim
