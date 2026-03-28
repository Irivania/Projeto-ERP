# model.py: Define os modelos de dados (banco de dados) do módulo de estoque.

from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Produto(Base):
	__tablename__ = "produtos"
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	quantidade = Column(Integer)
