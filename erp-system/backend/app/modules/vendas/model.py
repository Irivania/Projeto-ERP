# model.py: Define os modelos de dados (banco de dados) do módulo de vendas.

from sqlalchemy import Column, Integer, Float
from app.database.base import Base

class Venda(Base):
	__tablename__ = "vendas"
	id = Column(Integer, primary_key=True)
	total = Column(Float)
